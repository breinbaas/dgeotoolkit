from dgeotoolkit.models.basemodel import DGKTBaseModelPath


def test_basemodel():
    m = DGKTBaseModelPath(path_name="test")
    assert m.json_string.find("path_name") == -1
