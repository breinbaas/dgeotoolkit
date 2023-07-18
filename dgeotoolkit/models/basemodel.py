from pydantic import BaseModel
import inspect
from ..helpers import _next_id


class DGTKDSeriesModel(BaseModel):
    current_id: int = 0

    def next_id(self) -> int:
        """Generate the next id based on the current model"""
        self.current_id += 1
        return str(self.current_id)


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
