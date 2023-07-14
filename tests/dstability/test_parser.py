from dgeotoolkit.dstability.parser import DGeoStabilityParser


def test_parse_unpacked():
    dgp = DGeoStabilityParser()
    dsm = dgp.parse_unpacked("tests/testdata/dstability/unpacked")
    i = 1


def test_parse():
    dgp = DGeoStabilityParser()
    dsm = dgp.parse("tests/testdata/dstability/sample01.stix")
