from zipfile import ZipFile

from dgeotoolkit.dstability.dstabilitymodel import DStabilityModel


def test_parse_basic():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample01.stix")


def test_parse_reinforcements():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample02.stix")


def test_complete():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample03.stix")


def test_results():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample04.stix")


def test_serialize_basic():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample01.stix")
    dsm.serialize(path="tests/testdata/output/sample01.stix")

    # check the difference between the original and the created file!
    filenames_org = []
    filenames_out = []
    with ZipFile("tests/testdata/dstability/sample01.stix") as zip:
        for f in zip.filelist:
            if f.filename.find(".json") > -1:
                filenames_org.append(f.filename)

    with ZipFile("tests/testdata/output/sample01.stix") as zip:  # TODO zip weg later
        for f in zip.filelist:
            if f.filename.find(".json") > -1:
                filenames_out.append(f.filename)

    # for debugging
    filenames_org = sorted(filenames_org)
    filenames_out = sorted(filenames_out)

    # we should find the same filenames
    for fname in filenames_org:
        assert filenames_out.index(fname) > -1


def test_serialize_results():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample04.stix")
    dsm.serialize(path="tests/testdata/output/sample04.stix")

    # check the difference between the original and the created file!
    filenames_org = []
    filenames_out = []
    with ZipFile("tests/testdata/dstability/sample04.stix") as zip:
        for f in zip.filelist:
            if f.filename.find(".json") > -1:
                filenames_org.append(f.filename)

    with ZipFile("tests/testdata/output/sample04.stix") as zip:  # TODO zip weg later
        for f in zip.filelist:
            if f.filename.find(".json") > -1:
                filenames_out.append(f.filename)

    # for debugging
    filenames_org = sorted(filenames_org)
    filenames_out = sorted(filenames_out)

    # we should find the same filenames
    for fname in filenames_org:
        assert filenames_out.index(fname) > -1
