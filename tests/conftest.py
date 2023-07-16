from zipfile import ZipFile
import pytest


class Helpers:
    @staticmethod
    def check_files(org_stix, created_stix):
        # check the difference between the original and the created file!
        filenames_org = []
        filenames_out = []
        with ZipFile(org_stix) as zip:
            for f in zip.filelist:
                if f.filename.find(".json") > -1:
                    filenames_org.append(f.filename)

        with ZipFile(created_stix) as zip:  # TODO zip weg later
            for f in zip.filelist:
                if f.filename.find(".json") > -1:
                    filenames_out.append(f.filename)

        # for debugging
        filenames_org = sorted(filenames_org)
        filenames_out = sorted(filenames_out)

        # we should find the same filenames
        for fname in filenames_org:
            assert filenames_out.index(fname) > -1


@pytest.fixture
def helpers():
    return Helpers
