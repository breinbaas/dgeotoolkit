import importlib
import json
from pathlib import Path

from ..const import NAN

import dgeotoolkit.shared.dataclasses

CONVERTED_CLASSNAMES = {
    "Nailpropertiesforsoils": "NailPropertiesForSoilsObject",
    "Projectinfo": "ProjectInfoObject",
    "Soilcorrelations": "SoilCorrelationsObject",
    "Soilvisualizations": "SoilVisualizationsObject",
    "Calculationsettings": "CalculationSettings",
    "Bishopbruteforceresult": "BishopBruteForceResultObject",
    "Soillayers": "SoilLayers",
    "Waternetcreatorsettings": "WaternetCreatorSettingsObject",
    "Statecorrelations": "StateCorrelationsObject",
    "Calculationsettings": "CalculationSettingsObject",
    "Decorations": "DecorationsObject",
    "Loads": "LoadsObject",
    "Reinforcements": "ReinforcementsObject",
    "Soillayers": "SoilLayersObject",
    "States": "StatesObject",
    "Waternets": "WaternetsObject",
    "Soils": "SoilsObject",
    "Geometry": "GeometryObject",
    "Scenario": "ScenarioObject",
}


def json2object(json_string: str, class_name: str):
    json_string = json_string.replace("NaN", f"{NAN}")

    # We rely on the Object keyword to handle pydantic conversions
    # if Deltares somehow decides to use Object in the json we
    # have a problem and need to rename all dataclasses in the
    # shared/dataclasses.py file to some other postfix
    if json_string.find("Object") > -1:
        raise ValueError(
            f"Deltares has added a field called containing the word 'Object' in the json, this will mess up the functionality!"
        )

    try:
        if class_name in CONVERTED_CLASSNAMES.keys():
            class_name = CONVERTED_CLASSNAMES[class_name]
        _Class = getattr(
            importlib.import_module("dgeotoolkit.shared.dataclasses"), class_name
        )
        d = json.loads(json_string)
        instance = _Class(**d)
    except Exception as e:
        raise ValueError(f"Could not convert json to Object, got error; '{e}'")
    return instance


def object_from_str(s: str, class_name: str):
    return json2object(s, class_name)


def object_from_file(path: str):
    cname = Path(path).stem.capitalize()
    return json2object(open(path, "r").read(), cname)


def object_to_json(instance):
    pass
