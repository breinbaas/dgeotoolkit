from pydantic import BaseModel
from io import BytesIO
from zipfile import ZipFile
from pathlib import Path
from datetime import datetime
import re

from ..shared.dataclasses import *
from ..shared.json_conversions import object_from_str
from ..const import CLASS_PREFIX_DGEOFLOW, ALLOWED_PERSISTABLE_SHADING_TYPES
from ..models.dseries_model import DGTKDSeriesModel


class DGeoFlowModel(DGTKDSeriesModel):
    BoundaryConditions: List[DGTKFBoundaryConditions] = []
    Geometry: List[DGTKGeometry] = []
    MeshProperties: List[DGTKFMeshProperties] = []
    Scenario: List[DGTKFScenarios] = []
    SoilLayers: List[DGTKSoilLayers] = []

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

        if path != "":
            data = in_memory.read()
            p = Path(path)
            if p.suffix != ".flox":
                path = f"{path}.flox"

            with open(path, "wb") as out:
                out.write(data)
        else:
            return data

    def add_geometry(self, layers: List[DGTKFLayer] = []):
        next_id = self.next_id()
        self.Geometry.append(
            DGTKFGeometry(
                Id=next_id,
                Layers=layers,
            )
        )
        return next_id

    def add_soil(
        self,
        name: str,
        code: str,
        notes: str = "",
        horizontal_permeability=0.0,
        vertical_permeability=0.0,
    ):
        next_id = self.next_id()
        self.Soils.Soils.append(  # yeah I know.. Soils.Soils but it is what it is in the json!
            DGTKFSoil(
                Id=next_id,
                Name=name,
                Code=code,
                Notes=notes,
                HorizontalPermeability=horizontal_permeability,
                VerticalPermeability=vertical_permeability,
            )
        )
        return next_id

    def has_soil_id(self, soil_id: str) -> bool:
        for soil in self.Soils.Soils:
            if soil.Id == soil_id:
                return True
        return False

    def add_soilvisualization(
        self, soil_id: str, color: str, persistable_shading_type: str
    ):
        if not self.has_soil_id(soil_id):
            raise ValueError(f"DGeoFlowModel has no soil with id='{soil_id}'")

        # TODO check color format

        # check shading type
        if persistable_shading_type not in ALLOWED_PERSISTABLE_SHADING_TYPES:
            raise ValueError(
                f"Invalide PersistableShadingType '{persistable_shading_type}'"
            )

        self.SoilVisualizations.SoilVisualizations.append(  # yeah I know.. again
            DGTKFSoilVisualization(
                SoilId=soil_id,
                Color=color,
                PersistableShadingType=persistable_shading_type,
            ),
        )

    def add_boundary_conditions(self):
        next_id = self.next_id()
        self.BoundaryConditions.append(
            DGTKFBoundaryConditions(
                Id=next_id,
            )
        )
        return next_id

    def add_mesh_properties(self):
        next_id = self.next_id()
        self.MeshProperties.append(
            DGTKFMeshProperties(
                Id=next_id,
            )
        )
        return next_id

    def add_soillayers(self):
        next_id = self.next_id()
        self.SoilLayers.append(
            DGTKSoilLayers(
                Id=next_id,
            )
        )
        return next_id

    def add_scenario(
        self,
        label: str,
        notes: str,
        boundary_conditions_id: str,
        geometry_id: str,
        mesh_properties_id: str,
        soillayers_id: str,
    ):
        stage = DGTKFStage(
            Id=self.next_id(),
            Label="Stage 1",  # TODO
            Notes="",
            BoundaryConditionCollectionId=boundary_conditions_id,
        )
        calculation = DGTKFCalculation(
            Label="Calculation 1",
            Notes="",
            CalculationType="GroundwaterFlow",
            CriticalHeadSearchSpace=DGTKFCriticalHeadSearchSpace(
                MinimumHeadLevel=0.0, MaximumHeadLevel=1.0, StepSize=0.1
            ),
            MeshPropertiesId=mesh_properties_id,
        )
        self.Scenario.append(
            DGTKFScenario(
                Id=self.next_id(),
                Label=label,
                Notes=notes,
                GeometryId=geometry_id,
                SoilLayersId=soillayers_id,
                Stages=[stage],
                Calculations=[calculation],
            )
        )

    @classmethod
    def empty(cls) -> "DGeoFlowModel":
        result = DGeoFlowModel()

        current_date = datetime.now().strftime("%Y-%m-%d")

        # PROJECTINFO
        result.ProjectInfo = DGTKFProjectInfo(
            Path="",
            Project="",
            CrossSection="",
            Remarks="",
            Analyst="",
            LastModifier="",
            Date=None,
            LastModified=current_date,
            Created=current_date,
        )

        # DEFAULT SOILS AND SOILVISUALIZATIONS
        soil_id = result.add_soil(
            name="Clay with silt",
            code="P_Rk_k&s",
            horizontal_permeability=0.1,
            vertical_permeability=0.1,
        )
        result.add_soilvisualization(
            soil_id, color="#80FFCC00", persistable_shading_type="DotD"
        )

        soil_id = result.add_soil(
            name="Clay, deep",
            code="H_Rk_k_deep",
            horizontal_permeability=0.01,
            vertical_permeability=0.01,
        )
        result.add_soilvisualization(
            soil_id, color="#80657F22", persistable_shading_type="DiagonalB"
        )

        soil_id = result.add_soil(
            name="Clay, shallow",
            code="H_Rk_k_shallow",
            horizontal_permeability=0.01,
            vertical_permeability=0.01,
        )
        result.add_soilvisualization(
            soil_id, color="#80999911", persistable_shading_type="DiagonalA"
        )

        soil_id = result.add_soil(
            name="Embankment new",
            code="H_Aa_ht_new",
            horizontal_permeability=0.01,
            vertical_permeability=0.01,
        )
        result.add_soilvisualization(
            soil_id, color="#80FFCC00", persistable_shading_type="DotA"
        )

        soil_id = result.add_soil(
            name="Embankment old",
            code="H_Aa_ht_old",
            horizontal_permeability=0.01,
            vertical_permeability=0.01,
        )
        result.add_soilvisualization(
            soil_id, color="#80DDAA00", persistable_shading_type="DotB"
        )

        soil_id = result.add_soil(
            name="Organic clay",
            code="H_Rk_ko",
            horizontal_permeability=0.01,
            vertical_permeability=0.01,
        )
        result.add_soilvisualization(
            soil_id, color="#80336600", persistable_shading_type="DiagonalC"
        )

        soil_id = result.add_soil(
            name="Peat, deep",
            code="H_vbv_v",
            horizontal_permeability=0.01,
            vertical_permeability=0.01,
        )
        result.add_soilvisualization(
            soil_id, color="#80CC6600", persistable_shading_type="HorizontalB"
        )

        soil_id = result.add_soil(
            name="Peat, shallow",
            code="H_vhv_v",
            horizontal_permeability=0.01,
            vertical_permeability=0.01,
        )
        result.add_soilvisualization(
            soil_id, color="#80EEBB88", persistable_shading_type="HorizontalA"
        )

        soil_id = result.add_soil(
            name="Sand with clay",
            code="H_Ro_z&k",
            horizontal_permeability=1.0,
            vertical_permeability=1.0,
        )
        result.add_soilvisualization(
            soil_id, color="#80BB8800", persistable_shading_type="DotA"
        )

        soil_id = result.add_soil(
            name="Sand, permeable",
            code="Sand, permeable",
            horizontal_permeability=45.0,
            vertical_permeability=45.0,
        )
        result.add_soilvisualization(
            soil_id, color="#80DDAA00", persistable_shading_type="DotD"
        )

        soil_id = result.add_soil(
            name="Sand",
            code="Sand",
            horizontal_permeability=30.0,
            vertical_permeability=30.0,
        )
        result.add_soilvisualization(
            soil_id, color="#80DDAA00", persistable_shading_type="DotC"
        )

        soil_id = result.add_soil(
            name="Sand, less permeable",
            code="Sand, less permeable",
            horizontal_permeability=15.0,
            vertical_permeability=15.0,
        )
        result.add_soilvisualization(
            soil_id, color="#80DDAA00", persistable_shading_type="DotB"
        )

        # BOUNDARYCONDITIONS
        boundary_conditions_id = result.add_boundary_conditions()

        # GEOMETRY
        geometry_id = result.add_geometry()

        # MESHPROPERTIES
        mesh_properties_id = result.add_mesh_properties()

        # SOILLAYERS
        soillayers_id = result.add_soillayers()

        # SCENARIOS
        result.add_scenario(
            label="Scenario 1",
            notes="",
            boundary_conditions_id=boundary_conditions_id,
            geometry_id=geometry_id,
            mesh_properties_id=mesh_properties_id,
            soillayers_id=soillayers_id,
        )

        result._current_scenario_id = result.Scenario[0].Id
        result._current_stage_id = result.Scenario[0].Stages[0].Id

        return result

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

                # find Id and check for the highest one
                pattern = r'"Id": "(\d+)"'
                matches = re.findall(pattern, s)
                for m in matches:
                    if int(m) > result.current_id:
                        result.current_id = int(m)

                if cname.find("_") > -1:
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
