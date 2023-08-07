from dgeotoolkit.dstability.dstabilitymodel import DStabilityModel


def test_parse_basic():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample01.stix")


def test_parse_reinforcements():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample02.stix")


def test_complete():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample03.stix")


def test_results():
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample04.stix")


def test_serialize_basic(helpers):
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample01.stix")
    dsm.serialize(path="tests/testdata/output/sample01.stix")
    helpers.check_files(
        "tests/testdata/dstability/sample01.stix", "tests/testdata/output/sample01.stix"
    )


def test_serialize_reinforcements(helpers):
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample02.stix")
    dsm.serialize(path="tests/testdata/output/sample02.stix")
    helpers.check_files(
        "tests/testdata/dstability/sample02.stix", "tests/testdata/output/sample02.stix"
    )


def test_serialize_complete(helpers):
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample03.stix")
    dsm.serialize(path="tests/testdata/output/sample03.stix")
    helpers.check_files(
        "tests/testdata/dstability/sample03.stix", "tests/testdata/output/sample03.stix"
    )


def test_serialize_results(helpers):
    dsm = DStabilityModel.parse("tests/testdata/dstability/sample04.stix")
    dsm.serialize(path="tests/testdata/output/sample04.stix")
    helpers.check_files(
        "tests/testdata/dstability/sample04.stix", "tests/testdata/output/sample04.stix"
    )


def test_empty():
    dsm = DStabilityModel.empty()
    dsm.serialize(path="tests/testdata/output/empty.stix")
