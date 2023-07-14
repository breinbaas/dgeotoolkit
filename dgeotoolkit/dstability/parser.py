from zipfile import ZipFile
from pathlib import Path

from ..dstability.dstabilitymodel import DStabilityModel
from ..shared.dataclasses import *
from ..helpers import case_insensitive_glob
from ..shared.json_conversions import object_from_file, object_from_str


class DGeoStabilityParser:
    def parse(self, stix_path: str) -> DStabilityModel:
        dsm = DStabilityModel()
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
                CalculationSettingsObject() for i in range(num_scenarios)
            ]
            decorations = [DecorationsObject() for i in range(num_scenarios)]
            geometry = [GeometryObject() for i in range(num_scenarios)]
            loads = [LoadsObject() for i in range(num_scenarios)]
            reinforcements = [ReinforcementsObject() for i in range(num_scenarios)]
            scenarios = [ScenarioObject() for i in range(num_scenarios)]
            soillayers = [SoilLayersObject() for i in range(num_scenarios)]
            statecorrelations = [
                StateCorrelationsObject() for i in range(num_scenarios)
            ]
            states = [StatesObject() for i in range(num_scenarios)]
            waternetcreatorsettings = [
                WaternetCreatorSettingsObject() for i in range(num_scenarios)
            ]
            waternets = [WaternetsObject() for i in range(num_scenarios)]

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
                    iname = instance.__class__.__name__.replace("Object", "")

                    if iname in [
                        "ProjectInfo",
                        "BishopBruteForceResult",
                        "NailPropertiesForSoils",
                        "ProjectInfo",
                        "SoilCorrelations",
                        "Soils",
                        "SoilVisualizations",
                    ]:
                        setattr(dsm, iname, instance)
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
                        geometry[index] = instance
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

            dsm.CalculationSettings = calculationsettings
            dsm.Decorations = decorations
            dsm.Geometry = geometry
            dsm.Loads = loads
            dsm.Reinforcements = reinforcements
            dsm.Scenario = scenarios
            dsm.SoilLayers = soillayers
            dsm.StateCorrelations = statecorrelations
            dsm.States = states
            dsm.WaternetCreatorSettings = waternetcreatorsettings
            dsm.Waternets = waternets

        return dsm

    def serialize(self, path: str):
        pass
