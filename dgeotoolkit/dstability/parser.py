from ..dstability.dstabilitymodel import DStabilityModel
from ..helpers import case_insensitive_glob
from ..shared.json_conversions import object_from_file


class DGeoStabilityParser:
    def parse_unpacked(self, path: str) -> DStabilityModel:
        dsm = DStabilityModel()
        json_files = case_insensitive_glob(path, ".json")
        for json_file in json_files:
            try:
                instance = object_from_file(json_file)
                iname = instance.__class__.__name__.replace("Object", "")
                setattr(dsm, iname, instance)
            except Exception as e:
                raise ValueError(f"Could not handle {json_file}, got error '{e}'")

        return dsm

    def parse(self, stix_path: str) -> DStabilityModel:
        pass

    def serialize(self, path: str):
        pass
