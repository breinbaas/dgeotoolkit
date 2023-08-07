from pydantic import BaseModel
from zipfile import ZipFile
from pathlib import Path
from io import BytesIO
import re
from datetime import datetime

from ..shared.dataclasses import *
from ..shared.json_conversions import object_from_str
from ..const import CLASS_PREFIX_DSTABILITY, DSTABILITY_VERSION
from ..models.basemodel import DGTKDSeriesModel


class DStabilityModel(DGTKDSeriesModel):
    # membernames should match the filenames (not the folder names because the are inconsisten (e.g. geoemtries / geometry))
    CalculationSettings: List[DGTKSCalculationSettings] = [DGTKSCalculationSettings()]
    Decorations: List[DGTKSDecorations] = [DGTKSDecorations()]
    Geometry: List[DGTKSGeometry] = [DGTKSGeometry()]
    Loads: List[DGTKSLoads] = [DGTKSLoads()]
    Reinforcements: List[DGTKSReinforcements] = [DGTKSReinforcements()]
    BishopResults: List[DGTKSBishopResult] = []
    BishopBruteForceResults: DGTKSBishopBruteForceResult = []
    Scenario: List[DGTKSScenario] = [DGTKSScenario()]
    SoilLayers: List[DGTKSSoilLayers] = [DGTKSSoilLayers()]
    SpencerResults: List[DGTKSSpencer] = []
    SpencerGeneticAlgorithmResults: List[DGTKSSpencerGeneticAlgorithmResult] = []
    StateCorrelations: List[DGTKSStateCorrelations] = [DGTKSStateCorrelations()]
    UpliftVanResults: List[DGTKSUpliftVanResult] = []
    UpliftVanParticleSwarmResults: List[DGTKSUpliftVanParticleSwarmResult] = []
    States: List[DGTKSStates] = [DGTKSStates()]
    WaternetCreatorSettings: List[DGTKSWaternetCreatorSettings] = [
        (DGTKSWaternetCreatorSettings())
    ]
    Waternets: List[DGTKSWaternets] = [DGTKSWaternets()]
    NailPropertiesForSoils: DGTKSNailPropertiesForSoils = DGTKSNailPropertiesForSoils()
    ProjectInfo: DGTKSProjectInfo = DGTKSProjectInfo()
    SoilCorrelations: DGTKSSoilCorrelations = DGTKSSoilCorrelations()
    Soils: DGTKSSoils = DGTKSSoils()
    SoilVisualizations: DGTKSSoilVisualizations = DGTKSSoilVisualizations()

    def serialize(self, path: str = "") -> Optional[bytes]:
        """Serialize a dstability model to a file or bytesIO object (for webservices)

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
            "NailPropertiesForSoils",
            "SoilCorrelations",
            "Soils",
            "SoilVisualizations",
        ]:
            instance = getattr(self, memname)
            zip.writestr(f"{memname.lower()}.json", instance.json_string)

        # result files are handled here
        # can be optimized, ugly code but it works
        for memname in [
            "BishopResults",
            "BishopBruteForceResults",
            "SpencerResults",
            "SpencerGeneticAlgorithmResults",
            "UpliftVanResults",
            "UpliftVanParticleSwarmResults",
        ]:
            instances = getattr(self, memname)
            if memname == "BishopResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/bishop/bishopresult.json", instance.json_string
                        )
                    else:
                        zip.writestr(
                            f"results/bishop/bishopresult_{i}.json",
                            instance.json_string,
                        )
            elif memname == "BishopBruteForceResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/bishopbruteforce/bishopbruteforceresult.json",
                            instance.json_string,
                        )
                    else:
                        zip.writestr(
                            f"results/bishopbruteforce/bishopbruteforceresult_{i}.json",
                            instance.json_string,
                        )
            elif memname == "SpencerResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/spencer/spencerresult.json", instance.json_string
                        )
                    else:
                        zip.writestr(
                            f"results/bishop/bishopresult_{i}.json",
                            instance.json_string,
                        )
            elif memname == "SpencerGeneticAlgorithmResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/spencergeneticalgorithm/spencergeneticalgorithmresult.json",
                            instance.json_string,
                        )
                    else:
                        zip.writestr(
                            f"results/spencergeneticalgorithm/spencergeneticalgorithmresult_{i}.json",
                            instance.json_string,
                        )
            elif memname == "UpliftVanResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/upliftvan/upliftvanresult.json",
                            instance.json_string,
                        )
                    else:
                        zip.writestr(
                            f"results/upliftvan/upliftvanresult_{i}.json",
                            instance.json_string,
                        )
            elif memname == "UpliftVanParticleSwarmResults":
                for i, instance in enumerate(instances):
                    if i == 0:
                        zip.writestr(
                            "results/upliftvanparticleswarm/upliftvanparticleswarmresult.json",
                            instance.json_string,
                        )
                    else:
                        zip.writestr(
                            f"results/upliftvanparticleswarm/upliftvanparticleswarmresult_{i}.json",
                            instance.json_string,
                        )

        # the subdir files
        for memname in [
            "CalculationSettings",
            "Decorations",
            "Geometry",
            "Loads",
            "Reinforcements",
            "Scenario",
            "SoilLayers",
            "StateCorrelations",
            "States",
            "WaternetCreatorSettings",
            "Waternets",
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
            if p.suffix != ".stix":
                path = f"{path}.stix"

            with open(path, "wb") as out:
                out.write(data)
        else:
            return data

    @classmethod
    def empty(cls) -> "DStabilityModel":
        result = DStabilityModel()
        current_date = datetime.now().strftime("%Y-%m-%d")

        # PROJECTINFO
        result.ProjectInfo = DGTKSProjectInfo(
            Path="",
            Project="",
            CrossSection="",
            Remarks="",
            Analyst="",
            LastModifier="",
            Date=None,
            LastModified=current_date,
            Created=current_date,
            ApplicationCreated=DSTABILITY_VERSION,
            ApplicationModified=DSTABILITY_VERSION,
        )

        # DEFAULT SOILS AND SOILVISUALIZATIONS

        _ = result.add_soil(
            name="Embankment new",
            code="H_Aa_ht_new",
            ydry=19.3,
            ysat=19.3,
            params_above_pl=DGTKSMohrCoulombAdvancedShearStrengthModel(
                Cohesion=7.0,
                FrictionAngle=30.0,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.26,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80FFCC00",
            persitable_shading_type="DotA",
        )

        soil_id = result.add_soil(
            name="Embankment old",
            code="H_Aa_ht_old",
            ydry=18.0,
            ysat=18.0,
            params_above_pl=DGTKSMohrCoulombAdvancedShearStrengthModel(
                Cohesion=7.0,
                FrictionAngle=30.0,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.26,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80DDAA00",
            persitable_shading_type="DotB",
        )

        embankement_dry_su_table = DGTKSSuTable(
            StrengthIncreaseExponent=0.8,
            SuTablePoints=[
                DGTKSSuTablePoint(EffectiveStress=0.0, Su=0.0),
                DGTKSSuTablePoint(EffectiveStress=29.0, Su=29.0),
                DGTKSSuTablePoint(EffectiveStress=40.0, Su=32.0),
                DGTKSSuTablePoint(EffectiveStress=60.0, Su=37.0),
                DGTKSSuTablePoint(EffectiveStress=80.0, Su=42.0),
                DGTKSSuTablePoint(EffectiveStress=100.0, Su=48.0),
                DGTKSSuTablePoint(EffectiveStress=120.0, Su=55.0),
                DGTKSSuTablePoint(EffectiveStress=140.0, Su=62.0),
                DGTKSSuTablePoint(EffectiveStress=160.0, Su=69.0),
                DGTKSSuTablePoint(EffectiveStress=180.0, Su=77.0),
            ],
        )

        _ = result.add_soil(
            name="Embankment dry",
            code="Embankment dry",
            ydry=18.0,
            ysat=18.0,
            params_above_pl=embankement_dry_su_table,
            params_below_pl=embankement_dry_su_table,
            color="#80B8CC00",
            persitable_shading_type="DiagonalD",
        )

        _ = result.add_soil(
            name="Clay, shallow",
            code="H_Rk_k_shallow",
            ydry=14.8,
            ysat=14.8,
            params_above_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.23,
                StrengthIncreaseExponent=0.9,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.23,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80999911",
            persitable_shading_type="DiagonalA",
        )

        _ = result.add_soil(
            name="Clay, deep",
            code="H_Rk_k_deep",
            ydry=15.6,
            ysat=15.6,
            params_above_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.23,
                StrengthIncreaseExponent=0.9,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.23,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80657F22",
            persitable_shading_type="DiagonalB",
        )

        _ = result.add_soil(
            name="Organic clay",
            code="H_Rk_ko",
            ydry=13.9,
            ysat=13.9,
            params_above_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.23,
                StrengthIncreaseExponent=0.9,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.24,
                StrengthIncreaseExponent=0.85,
            ),
            color="#80336600",
            persitable_shading_type="DiagonalC",
        )

        _ = result.add_soil(
            name="Peat, shallow",
            code="H_vhv_v",
            ydry=10.1,
            ysat=10.1,
            params_above_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.3,
                StrengthIncreaseExponent=0.9,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.3,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80EEBB88",
            persitable_shading_type="HorizontalA",
        )

        _ = result.add_soil(
            name="Peat, deep",
            code="H_vbv_v",
            ydry=11.0,
            ysat=11.0,
            params_above_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.27,
                StrengthIncreaseExponent=0.9,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.27,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80CC6600",
            persitable_shading_type="HorizontalB",
        )

        _ = result.add_soil(
            name="Sand",
            code="Sand",
            ydry=18.0,
            ysat=20.0,
            params_above_pl=DGTKSMohrCoulombAdvancedShearStrengthModel(
                Cohesion=0.0,
                FrictionAngle=30.0,
            ),
            params_below_pl=DGTKSMohrCoulombAdvancedShearStrengthModel(
                Cohesion=0.0,
                FrictionAngle=30.0,
            ),
            color="#80DDAA00",
            persitable_shading_type="DotC",
        )

        _ = result.add_soil(
            name="Clay with silt",
            code="P_Rk_k&s",
            ydry=18.0,
            ysat=18.0,
            params_above_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.22,
                StrengthIncreaseExponent=0.9,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.22,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80FFCC00",
            persitable_shading_type="DotD",
        )

        _ = result.add_soil(
            name="Sand with clay",
            code="H_Ro_z&k",
            ydry=18.0,
            ysat=18.0,
            params_above_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.22,
                StrengthIncreaseExponent=0.9,
            ),
            params_below_pl=DGTKSSuShearStrengthModel(
                ShearStrengthRatio=0.22,
                StrengthIncreaseExponent=0.9,
            ),
            color="#80BB8800",
            persitable_shading_type="DotA",
        )

        dilatent_clay_su_table = DGTKSSuTable(
            StrengthIncreaseExponent=0.8,
            SuTablePoints=[
                DGTKSSuTablePoint(EffectiveStress=0.0, Su=0.0),
                DGTKSSuTablePoint(EffectiveStress=39.0, Su=30.0),
                DGTKSSuTablePoint(EffectiveStress=200.0, Su=100.0),
            ],
        )
        _ = result.add_soil(
            name="Dilatent clay",
            code="Dilatent clay",
            ydry=18.0,
            ysat=18.0,
            params_above_pl=dilatent_clay_su_table,
            params_below_pl=dilatent_clay_su_table,
            color="#80218D0D",
            persitable_shading_type="DiagonalD",
        )

        # CALCULATIONSETTINGS
        result.CalculationSettings[0].Id = result.next_id()
        result.Decorations[0].Id = result.next_id()
        result.Geometry[0].Id = result.next_id()
        result.Loads[0].Id = result.next_id()
        result.Reinforcements[0].Id = result.next_id()
        result.Scenario[0].Id = result.next_id()
        result.SoilLayers[0].Id = result.next_id()
        result.StateCorrelations[0].Id = result.next_id()
        result.States[0].Id = result.next_id()
        result.WaternetCreatorSettings[0].Id = result.next_id()
        result.Waternets[0].Id = result.next_id()
        result.Scenario[0].Calculations.append(
            DGTKSCalculation(
                Id=result.next_id(),
                Label="Calculation 1",
                CalculationSettingsId=result.CalculationSettings[0].Id,
            )
        )
        result.Scenario[0].Stages.append(
            DGTKSStage(
                Id=result.next_id(),
                Label="Stage 1",
                GeometryId=result.Geometry[0].Id,
                DecorationsId=result.Decorations[0].Id,
                SoilLayersId=result.SoilLayers[0].Id,
                WaternetId=result.Waternets[0].Id,
                WaternetCreatorSettingsId=result.WaternetCreatorSettings[0].Id,
                StateId=result.States[0].Id,
                StateCorrelationsId=result.StateCorrelations[0].Id,
                LoadsId=result.Loads[0].Id,
                ReinforcementsId=result.Reinforcements[0].Id,
            )
        )

        return result

    def add_soil(
        self,
        name: str,
        code: str,
        ydry: float,
        ysat: float,
        color: str,
        persitable_shading_type: str,
        params_above_pl: Union[
            DGTKSMohrCoulombClassicShearStrengthModel,
            DGTKSMohrCoulombAdvancedShearStrengthModel,
            DGTKSSuShearStrengthModel,
            DGTKSSuTable,
        ],
        params_below_pl: Union[
            DGTKSMohrCoulombClassicShearStrengthModel,
            DGTKSMohrCoulombAdvancedShearStrengthModel,
            DGTKSSuShearStrengthModel,
            DGTKSSuTable,
        ],
        notes: str = "",
        is_probabilistic: bool = False,
    ):
        next_id = self.next_id()
        soil = DGTKSSoil(
            Id=next_id,
            Name=name,
            Notes=notes,
            Code=code,
            IsProbabilistic=is_probabilistic,
            VolumetricWeightAbovePhreaticLevel=ydry,
            VolumetricWeightBelowPhreaticLevel=ysat,
        )

        if type(params_above_pl) == DGTKSMohrCoulombClassicShearStrengthModel:
            soil.ShearStrengthModelTypeAbovePhreaticLevel = "MohrCoulombClassic"
            soil.MohrCoulombClassicShearStrengthModel = params_above_pl
            soil.MohrCoulombAdvancedShearStrengthModel.Cohesion = (
                params_above_pl.Cohesion
            )
            soil.MohrCoulombAdvancedShearStrengthModel.FrictionAngle = (
                params_above_pl.FrictionAngle
            )
        elif type(params_above_pl) == DGTKSMohrCoulombAdvancedShearStrengthModel:
            soil.ShearStrengthModelTypeAbovePhreaticLevel = "MohrCoulombAdvanced"
            soil.MohrCoulombAdvancedShearStrengthModel = params_above_pl
            soil.MohrCoulombClassicShearStrengthModel.Cohesion = (
                params_above_pl.Cohesion
            )
            soil.MohrCoulombClassicShearStrengthModel.FrictionAngle = (
                params_above_pl.FrictionAngle
            )
        elif type(params_above_pl) == DGTKSSuShearStrengthModel:
            soil.ShearStrengthModelTypeAbovePhreaticLevel = "Su"
            soil.SuShearStrengthModel = params_above_pl
        else:
            soil.ShearStrengthModelTypeAbovePhreaticLevel = "SuTable"
            soil.SuTable = params_above_pl

        if type(params_below_pl) == DGTKSMohrCoulombClassicShearStrengthModel:
            soil.ShearStrengthModelTypeBelowPhreaticLevel = "MohrCoulombClassic"
            soil.MohrCoulombClassicShearStrengthModel = params_below_pl
            soil.MohrCoulombAdvancedShearStrengthModel.Cohesion = (
                params_below_pl.Cohesion
            )
            soil.MohrCoulombAdvancedShearStrengthModel.FrictionAngle = (
                params_below_pl.FrictionAngle
            )
        elif type(params_below_pl) == DGTKSMohrCoulombAdvancedShearStrengthModel:
            soil.ShearStrengthModelTypeBelowPhreaticLevel = "MohrCoulombAdvanced"
            soil.MohrCoulombAdvancedShearStrengthModel = params_below_pl
            soil.MohrCoulombClassicShearStrengthModel.Cohesion = (
                params_below_pl.Cohesion
            )
            soil.MohrCoulombClassicShearStrengthModel.FrictionAngle = (
                params_below_pl.FrictionAngle
            )
        elif type(params_below_pl) == DGTKSSuShearStrengthModel:
            soil.ShearStrengthModelTypeBelowPhreaticLevel = "Su"
            soil.SuShearStrengthModel = params_below_pl
        else:
            soil.ShearStrengthModelTypeBelowPhreaticLevel = "SuTable"
            soil.SuTable = params_below_pl

        self.Soils.Soils.append(soil)
        self.SoilVisualizations.SoilVisualizations.append(
            DGTKSSoilVisualization(
                SoilId=next_id,
                Color=color,
                PersistableShadingType=persitable_shading_type,
            )
        )
        self.NailPropertiesForSoils.NailPropertiesForSoils.append(
            DGTKSNailPropertyForSoils(SoilId=next_id)
        )

        return next_id

    @classmethod
    def parse(cls, stix_path: str) -> "DStabilityModel":
        result = DStabilityModel()
        with ZipFile(stix_path) as zip:
            calculationsettings = []
            decorations = []
            geometry = []
            loads = []
            reinforcements = []
            scenarios = []
            soillayers = []
            statecorrelations = []
            states = []
            waternetcreatorsettings = []
            waternets = []

            bishopresults = []
            bishopbruteforceresults = []
            spencerresults = []
            spencergeneticalgorithmresults = []
            upliftvanresults = []
            upliftvanparticleswarmresults = []

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
                    instance = object_from_str(s, cname, CLASS_PREFIX_DSTABILITY)
                    iname = instance.__class__.__name__.replace(
                        CLASS_PREFIX_DSTABILITY, ""
                    )

                    if iname in [
                        "ProjectInfo",
                        "NailPropertiesForSoils",
                        "SoilCorrelations",
                        "Soils",
                        "SoilVisualizations",
                    ]:
                        setattr(result, iname, instance)
                        continue

                    if iname == "BishopBruteForceResult":
                        bishopbruteforceresults.append(instance)
                        continue
                    if iname == "BishopResult":
                        bishopresults.append(instance)
                        continue
                    if iname == "SpencerResult":
                        spencerresults.append(instance)
                        continue
                    if iname == "SpencerGeneticAlgorithmResult":
                        spencergeneticalgorithmresults.append(instance)
                        continue
                    if iname == "UpliftVanResult":
                        upliftvanresults.append(instance)
                        continue
                    if iname == "UpliftVanParticleSwarmResult":
                        upliftvanparticleswarmresults.append(instance)
                        continue

                    if iname == "CalculationSettings":
                        calculationsettings.append(instance)
                    elif iname == "Decorations":
                        decorations.append(instance)
                    elif iname == "Geometry":
                        geometry.append(instance)
                    elif iname == "Loads":
                        loads.append(instance)
                    elif iname == "Reinforcements":
                        reinforcements.append(instance)
                    elif iname == "Scenario":
                        scenarios.append(instance)
                    elif iname == "SoilLayers":
                        soillayers.append(instance)
                    elif iname == "StateCorrelations":
                        statecorrelations.append(instance)
                    elif iname == "States":
                        states.append(instance)
                    elif iname == "WaternetCreatorSettings":
                        waternetcreatorsettings.append(instance)
                    elif iname == "Waternets":
                        waternets.append(instance)
                    else:
                        raise ValueError(f"Unknown classname '{iname}'")

                except Exception as e:
                    raise ValueError(f"Could not handle {f}, got error '{e}'")

            result.CalculationSettings = calculationsettings
            result.Decorations = decorations
            result.Geometry = geometry
            result.Loads = loads
            result.Reinforcements = reinforcements
            result.Scenario = scenarios
            result.SoilLayers = soillayers
            result.StateCorrelations = statecorrelations
            result.States = states
            result.WaternetCreatorSettings = waternetcreatorsettings
            result.Waternets = waternets
            result.BishopResults = bishopresults
            result.BishopBruteForceResults = bishopbruteforceresults
            result.SpencerResults = spencerresults
            result.SpencerGeneticAlgorithmResults = spencergeneticalgorithmresults
            result.UpliftVanResults = upliftvanresults
            result.UpliftVanParticleSwarmResults = upliftvanparticleswarmresults

        return result
