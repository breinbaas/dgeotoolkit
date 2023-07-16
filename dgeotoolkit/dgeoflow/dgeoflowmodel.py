from pydantic import BaseModel
from io import BytesIO
from zipfile import ZipFile
from pathlib import Path


from ..shared.dataclasses import *
from ..shared.json_conversions import object_from_str
from ..const import CLASS_PREFIX_DGEOFLOW


class DGeoFlowModel(BaseModel):
    BoundaryConditions: List[DGTKFBoundaryConditions] = []
    Geometries: List[DGTKFGeometry] = []
    MeshProperties: List[DGTKFMeshProperties] = []
    Scenarios: List[DGTKFScenarios] = []
    SoilLayers: List[DGTKFSoilLayers] = []

    ProjectInfo: DGTKFProjectInfo = DGTKFProjectInfo()
    Soils: DGTKFSoils = DGTKFSoils()
    SoilVisualizations: DGTKFSoilVisualizations = DGTKFSoilVisualizations()

    def serialize(self, path: str = "") -> Optional[bytes]:
        pass

    @classmethod
    def parse(cls, flox_path: str) -> "DGeoFlowModel":
        result = DGeoFlowModel()
        with ZipFile(flox_path) as zip:
            boundaryconditions = []
            geometries = []
            meshproperties = []
            scenarios = []
            soillayers = []

            pipelengthresults = []

            for f in zip.filelist:
                if f.filename.find(".json") == -1:
                    continue  # skip checksum

                cname = Path(f.filename).stem.capitalize()
                s = zip.read(f).decode(errors="ignore")

                index = 0
                if cname.find("_") > -1:
                    index = int(cname.split("_")[-1])
                    cname = cname.split("_")[0]

                try:
                    instance = object_from_str(s, cname, CLASS_PREFIX_DGEOFLOW)
                    iname = instance.__class__.__name__.replace(
                        CLASS_PREFIX_DGEOFLOW, ""
                    )

                    if iname in [
                        "ProjectInfo",
                        "Soils",
                        "SoilVisualizations",
                    ]:
                        setattr(result, iname, instance)
                        continue

                    if iname == "PipeLengthResult":
                        pipelengthresults.append(instance)
                        continue

                    if iname == "BoundaryConditions":
                        boundaryconditions.append(instance)
                    elif iname == "Geometry":
                        geometries.append(instance)
                    elif iname == "MeshProperties":
                        meshproperties.append(instance)
                    elif iname == "Scenario":
                        scenarios.append(instance)
                    elif iname == "SoilLayers":
                        soillayers.append(instance)

                except Exception as e:
                    raise ValueError(f"Could not handle {f}, got error '{e}'")
