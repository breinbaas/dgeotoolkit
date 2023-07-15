import json
from pathlib import Path

from dgeotoolkit.shared.json_conversions import (
    json2object,
    object_from_file,
    object_from_str,
)
from dgeotoolkit.shared.dataclasses import DGKTLoads


def test_json2object():
    fname = "tests/testdata/loads.json"
    cname = Path(fname).stem.capitalize()

    instance = json2object(open("tests/testdata/loads.json", "r").read(), cname)
    assert type(instance) == DGKTLoads
    json_string = instance.model_dump_json()
    with open("tests/testdata/output/loads.out.json", "w") as outfile:
        outfile.write(json_string)


def test_object_from_file():
    instance = object_from_file("tests/testdata/loads.json")
    assert type(instance) == DGKTLoads


def test_object_from_str():
    s = open("tests/testdata/loads.json", "r").read()
    instance = object_from_str(s, "Loads")
    assert type(instance) == DGKTLoads
