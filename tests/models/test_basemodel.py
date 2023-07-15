from dgeotoolkit.models.basemodel import DGKTBaseModel


def test_basemodel():
    m = DGKTBaseModel()
    s = m.json_string
    i = 1
