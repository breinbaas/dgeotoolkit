from dgeotoolkit.dgeoflow.dgeoflowmodel import DGeoFlowModel


def test_parse_basic():
    dgm = DGeoFlowModel.parse("tests/testdata/dgeoflow/sample01.flox")
    i = 1


def test_serialize_basic(helpers):
    dgm = DGeoFlowModel.parse("tests/testdata/dgeoflow/sample01.flox")
    dgm.serialize(path="tests/testdata/output/sample01.flox")
    helpers.check_files(
        "tests/testdata/dgeoflow/sample01.flox", "tests/testdata/output/sample01.flox"
    )


def test_empty():
    dgm = DGeoFlowModel.empty()
    dgm.serialize(path="tests/testdata/output/empty.flox")
