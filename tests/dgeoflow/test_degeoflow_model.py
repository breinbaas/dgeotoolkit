from dgeotoolkit.dgeoflow.dgeoflowmodel import DGeoFlowModel


def test_basic():
    dgm = DGeoFlowModel.parse("tests/testdata/dgeoflow/sample01.flox")
    i = 1


# TODO serialize and test
def test_serialize_basic(helpers):
    dgm = DGeoFlowModel.parse("tests/testdata/dgeoflow/sample01.flox")
    dgm.serialize(path="tests/testdata/output/sample01.flox")
    helpers.check_files(
        "tests/testdata/dgeoflow/sample01.flox", "tests/testdata/output/sample01.flox"
    )
