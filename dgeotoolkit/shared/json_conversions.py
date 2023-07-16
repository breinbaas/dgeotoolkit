import importlib
import json
from pathlib import Path

from ..const import NAN, CLASS_PREFIX_DSTABILITY

import dgeotoolkit.shared.dataclasses

CONVERTED_CLASSNAMES = {
    "Nailpropertiesforsoils": "NailPropertiesForSoils",
    "Projectinfo": "ProjectInfo",
    "Soilcorrelations": "SoilCorrelations",
    "Soilvisualizations": "SoilVisualizations",
    "Calculationsettings": "CalculationSettings",
    "Bishopbruteforceresult": "BishopBruteForceResult",
    "Bishopresult": "BishopResult",
    "Spencerresult": "SpencerResult",
    "Spencergeneticalgorithmresult": "SpencerGeneticAlgorithmResult",
    "Upliftvanresult": "UpliftVanResult",
    "Upliftvanparticleswarmresult": "UpliftVanParticleSwarmResult",
    "Soillayers": "SoilLayers",
    "Waternetcreatorsettings": "WaternetCreatorSettings",
    "Statecorrelations": "StateCorrelations",
    "Calculationsettings": "CalculationSettings",
    "Decorations": "Decorations",
    "Loads": "Loads",
    "Reinforcements": "Reinforcements",
    "Soillayers": "SoilLayers",
    "States": "States",
    "Waternets": "Waternets",
    "Soils": "Soils",
    "Geometry": "Geometry",
    "Scenario": "Scenario",
    "Boundaryconditions": "BoundaryConditions",
    "Meshproperties": "MeshProperties",
    "Pipelengthresult": "PipeLengthResult",
}


def json2object(json_string: str, class_name: str, class_prefix: str):
    json_string = json_string.replace("NaN", f"{NAN}")

    # We rely on the DGKT keyword to handle pydantic conversions
    # and fix some json naming issues in the stix
    # if Deltares somehow decides to use Object in the json we
    # have a problem and need to rename all dataclasses in the
    # shared/dataclasses.py file to some other postfix
    if json_string.find(class_prefix) > -1:
        raise ValueError(
            f"Deltares has added a field called containing the prefix 'DGKT' in the json, this will mess up the functionality!"
        )

    try:
        if class_name in CONVERTED_CLASSNAMES.keys():
            class_name = CONVERTED_CLASSNAMES[class_name]
        class_name = f"{class_prefix}{class_name}"
        _Class = getattr(
            importlib.import_module("dgeotoolkit.shared.dataclasses"), class_name
        )
        d = json.loads(json_string)
        instance = _Class(**d)
    except Exception as e:
        raise ValueError(f"Could not convert json to Object, got error; '{e}'")
    return instance


def object_from_str(s: str, class_name: str, class_prefix: str):
    return json2object(s, class_name, class_prefix)
