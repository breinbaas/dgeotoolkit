from dgeotoolkit.models.basemodel import DGTKBaseModelPath


def test_basemodel():
    m = DGTKBaseModelPath(path_name="test")
    assert m.json_string.find("path_name") == -1
