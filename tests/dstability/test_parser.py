from dgeotoolkit.dstability.parser import DGeoStabilityParser


def test_parse_basic():
    dgp = DGeoStabilityParser()
    dsm = dgp.parse("tests/testdata/dstability/sample01.stix")
    i = 1


def test_parse_reinforcements():
    dgp = DGeoStabilityParser()
    dsm = dgp.parse("tests/testdata/dstability/sample02.stix")


def test_complete():
    dgp = DGeoStabilityParser()
    dsm = dgp.parse("tests/testdata/dstability/sample03.stix")
    i = 1
