from dgeotoolkit.dgeoflow.dgeoflowmodel import DGeoFlowModel


def test_basic():
    dgm = DGeoFlowModel.parse("tests/testdata/dgeoflow/sample01.flox")
    i = 1
