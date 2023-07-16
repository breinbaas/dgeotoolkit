from pydantic import BaseModel


class DGTKBaseModel(BaseModel):
    @property
    def json_string(self):
        sjson = self.model_dump_json(indent=4)
        sjson = sjson.replace("-1000000000.0", '"NaN"')
        return sjson


class DGTKBaseModelPath(DGTKBaseModel):
    path_name: str = ""  # fill in if the class has a seperate folder in the stix file

    @property
    def json_string(self):
        sjson = self.model_dump_json(indent=4, exclude={"path_name"})
        sjson = sjson.replace("-1000000000.0", '"NaN"')
        return sjson
