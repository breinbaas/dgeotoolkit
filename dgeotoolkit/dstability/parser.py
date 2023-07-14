from zipfile import ZipFile
from pathlib import Path

from ..dstability.dstabilitymodel import DStabilityModel
from ..helpers import case_insensitive_glob
from ..shared.json_conversions import object_from_file, object_from_str


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
        dsm = DStabilityModel()
        with ZipFile(stix_path) as zip:
            for f in zip.filelist:
                if f.filename.find(".json") == -1:
                    continue  # skip checksum
                cname = Path(f.filename).stem.capitalize()
                s = zip.read(f).decode(errors="ignore")

                try:
                    instance = object_from_str(s, cname)
                    iname = instance.__class__.__name__.replace("Object", "")
                    setattr(dsm, iname, instance)
                except Exception as e:
                    raise ValueError(f"Could not handle {f}, got error '{e}'")

        return dsm

    def serialize(self, path: str):
        pass
