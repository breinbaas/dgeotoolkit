from dgeotoolkit.models.basemodel import DGTKBaseModelPath
from dgeotoolkit.dgeoflow.dgeoflowmodel import DGeoFlowModel
from dgeotoolkit.shared.dataclasses import DGTKFBoundaryConditions, DGTKFMeshProperties


def test_basemodel():
    m = DGTKBaseModelPath(path_name="test")
    assert m.json_string.find("path_name") == -1
