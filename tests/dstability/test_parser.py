from dgeotoolkit.dstability.parser import DGeoStabilityParser


def test_read_unpacked():
    dgp = DGeoStabilityParser()
    dsm = dgp.parse_unpacked("tests/testdata/dstability/unpacked")
    i = 1
