import json
from pathlib import Path

from dgeotoolkit.shared.json_conversions import (
    json2object,
    object_from_str,
)
from dgeotoolkit.shared.dataclasses import DGTKSLoads
from dgeotoolkit.const import CLASS_PREFIX_DSTABILITY


def test_json2object():
    fname = "tests/testdata/loads.json"
    cname = Path(fname).stem.capitalize()

    instance = json2object(
        open("tests/testdata/loads.json", "r").read(), cname, CLASS_PREFIX_DSTABILITY
    )
    assert type(instance) == DGTKSLoads
    json_string = instance.model_dump_json()
    with open("tests/testdata/output/loads.out.json", "w") as outfile:
        outfile.write(json_string)


def test_object_from_str():
    s = open("tests/testdata/loads.json", "r").read()
    instance = object_from_str(s, "Loads", CLASS_PREFIX_DSTABILITY)
    assert type(instance) == DGTKSLoads
