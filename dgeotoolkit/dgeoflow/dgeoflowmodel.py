from pydantic import BaseModel
from io import BytesIO
from zipfile import ZipFile
from pathlib import Path


from ..shared.dataclasses import *
from ..shared.json_conversions import object_from_str
from ..const import CLASS_PREFIX_DGEOFLOW


class DGeoFlowModel(BaseModel):
    BoundaryConditions: List[DGTKFBoundaryConditions] = []
    Geometry: List[DGTKFGeometry] = []
    MeshProperties: List[DGTKFMeshProperties] = []
    Scenario: List[DGTKFScenarios] = []
    SoilLayers: List[DGTKFSoilLayers] = []

    ProjectInfo: DGTKFProjectInfo = DGTKFProjectInfo()
    Soils: DGTKFSoils = DGTKFSoils()
    SoilVisualizations: DGTKFSoilVisualizations = DGTKFSoilVisualizations()

    PipeLengthResults: List[DGTKFPipeLengthResult] = []
    GroundWaterFlowResults: List[DGTKFGroundWaterFlowResult] = []
    # TODO > nog een resultaat toevoegen

    def serialize(self, path: str = "") -> Optional[bytes]:
        """Serialize a dgeoflow model to a file or bytesIO object (for webservices)

        Args:
            path (str, optional): The path of the file (including filename). Defaults to "".

        Returns:
            Optional[bytes]: If the path is set it will create the file, if not it will return the data as bytes
        """
        in_memory = BytesIO()
        zip = ZipFile(in_memory, "w")

        # 'loose' files
        for memname in [
            "ProjectInfo",
            "Soils",
            "SoilVisualizations",
        ]:
            instance = getattr(self, memname)
            zip.writestr(f"{memname.lower()}.json", instance.json_string)

        # result files are handled here
        # can be optimized, ugly code but it works
        for memname in ["PipeLengthResults", "GroundWaterFlowResults"]:
            instances = getattr(self, memname)
            if memname == "PipeLengthResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/pipelength/pipelengthresult.json",
                            instance.json_string,
                        )
                    else:
                        zip.writestr(
                            f"results/pipelength/pipelengthpresult_{i}.json",
                            instance.json_string,
                        )
            elif memname == "GroundWaterFlowResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/groundwaterflow/groundwaterflowresult.json",
                            instance.json_string,
                        )
                    else:
                        zip.writestr(
                            f"results/groundwaterflow/groundwaterflowpresult_{i}.json",
                            instance.json_string,
                        )

        for memname in [
            "BoundaryConditions",
            "Geometry",
            "MeshProperties",
            "Scenario",
            "SoilLayers",
        ]:
            instances = getattr(self, memname)
            for i, instance in enumerate(instances):
                if i == 0:
                    fname = f"{memname.lower()}.json"
                else:
                    fname = f"{memname.lower()}_{i}.json"
                zip.writestr(f"{instance.path_name}/{fname}", instance.json_string)

        zip.close()
        in_memory.seek(0)

        if path is not "":
            data = in_memory.read()
            p = Path(path)
            if p.suffix != ".flox":
                path = f"{path}.flox"

            with open(path, "wb") as out:
                out.write(data)
        else:
            return data

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
            groundwaterflowresult = []

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
                    if iname == "GroundWaterFlowResult":
                        groundwaterflowresult.append(instance)
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

        result.BoundaryConditions = boundaryconditions
        result.Geometry = geometries
        result.MeshProperties = meshproperties
        result.Scenario = scenarios
        result.SoilLayers = soillayers

        result.PipeLengthResults = pipelengthresults
        result.GroundWaterFlowResults = groundwaterflowresult
        return result
