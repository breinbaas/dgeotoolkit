from pydantic import BaseModel


class DGKTBaseModel(BaseModel):
    path_name: str = ""  # fill in if the class has a seperate folder in the stix file

    @property
    def json_string(self):
        return self.model_dump_json(indent=4, exclude={"path_name"})
