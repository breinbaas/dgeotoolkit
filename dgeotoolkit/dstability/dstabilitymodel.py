from pydantic import BaseModel
from zipfile import ZipFile
from pathlib import Path
from io import BytesIO

from ..shared.dataclasses import *
from ..shared.json_conversions import object_from_str
from ..const import CLASS_PREFIX


class DStabilityModel(BaseModel):
    # membernames should match the filenames (not the folder names because the are inconsisten (e.g. geoemtries / geometry))
    CalculationSettings: List[DGKTCalculationSettings] = [DGKTCalculationSettings()]
    Decorations: List[DGKTDecorations] = [DGKTDecorations()]
    Geometry: List[DGKTGeometry] = [DGKTGeometry()]
    Loads: List[DGKTLoads] = [DGKTLoads()]
    Reinforcements: List[DGKTReinforcements] = [DGKTReinforcements()]
    BishopResults: List[DGKTBishopResult] = []
    BishopBruteForceResults: DGKTBishopBruteForceResult = []
    Scenario: List[DGKTScenario] = [DGKTScenario()]
    SoilLayers: List[DGKTSoilLayers] = [DGKTSoilLayers()]
    SpencerResults: List[DGKTSpencer] = []
    SpencerGeneticAlgorithmResults: List[DGKTSpencerGeneticAlgorithmResult] = []
    StateCorrelations: List[DGKTStateCorrelations] = [DGKTStateCorrelations()]
    UpliftVanResults: List[DGKTUpliftVanResult] = []
    UpliftVanParticleSwarmResults: List[DGKTUpliftVanParticleSwarmResult] = []
    States: List[DGKTStates] = [DGKTStates()]
    WaternetCreatorSettings: List[DGKTWaternetCreatorSettings] = [
        (DGKTWaternetCreatorSettings())
    ]
    Waternets: List[DGKTWaternets] = [DGKTWaternets()]
    NailPropertiesForSoils: DGKTNailPropertiesForSoils = DGKTNailPropertiesForSoils()
    ProjectInfo: DGKTProjectInfo = DGKTProjectInfo()
    SoilCorrelations: DGKTSoilCorrelations = DGKTSoilCorrelations()
    Soils: DGKTSoils = DGKTSoils()
    SoilVisualizations: DGKTSoilVisualizations = DGKTSoilVisualizations()

    def serialize(self, path: str = ""):
        # in_memory = StringIO()
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

        if path is not "":
            data = in_memory.read()
            p = Path(path)
            if p.suffix != ".stix":  # TODO > stix after debugging
                path = f"{path}.stix"

            with open(path, "wb") as out:
                out.write(data)

    @classmethod
    def parse(cls, stix_path: str) -> "DStabilityModel":
        result = DStabilityModel()
        with ZipFile(stix_path) as zip:
            # first determine if we have multiple scenarios
            # which can be recognized with the _n postfix
            # if we have them find the largest number
            # this tells us how many scenarios we have
            num_scenarios = 1
            for f in zip.filelist:
                if f.filename.find(".json") > -1 and f.filename.find("_") > -1:
                    num_scenarios = max(
                        num_scenarios, int(Path(f.filename).stem.split("_")[-1]) + 1
                    )

            # now create that many entries in the dsm lists
            calculationsettings = [
                DGKTCalculationSettings() for i in range(num_scenarios)
            ]
            decorations = [DGKTDecorations() for i in range(num_scenarios)]
            geometry = [DGKTGeometry() for i in range(num_scenarios)]
            loads = [DGKTLoads() for i in range(num_scenarios)]
            reinforcements = [DGKTReinforcements() for i in range(num_scenarios)]
            scenarios = [DGKTScenario() for i in range(num_scenarios)]
            soillayers = [DGKTSoilLayers() for i in range(num_scenarios)]
            statecorrelations = [DGKTStateCorrelations() for i in range(num_scenarios)]
            states = [DGKTStates() for i in range(num_scenarios)]
            waternetcreatorsettings = [
                DGKTWaternetCreatorSettings() for i in range(num_scenarios)
            ]
            waternets = [DGKTWaternets() for i in range(num_scenarios)]

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

                index = 0
                if cname.find("_") > -1:
                    index = int(cname.split("_")[-1])
                    cname = cname.split("_")[0]

                try:
                    instance = object_from_str(s, cname)
                    iname = instance.__class__.__name__.replace(CLASS_PREFIX, "")

                    if iname in [
                        "ProjectInfo",
                        "NailPropertiesForSoils",
                        "ProjectInfo",
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
                        calculationsettings[index] = instance
                    elif iname == "Decorations":
                        decorations[index] = instance
                    elif iname == "Geometry":
                        geometry[index] = instance
                    elif iname == "Loads":
                        loads[index] = instance
                    elif iname == "Reinforcements":
                        reinforcements[index] = instance
                    elif iname == "Scenario":
                        scenarios[index] = instance
                    elif iname == "SoilLayers":
                        soillayers[index] = instance
                    elif iname == "StateCorrelations":
                        statecorrelations[index] = instance
                    elif iname == "States":
                        states[index] = instance
                    elif iname == "WaternetCreatorSettings":
                        waternetcreatorsettings[index] = instance
                    elif iname == "Waternets":
                        waternets[index] = instance
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
