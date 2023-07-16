from zipfile import ZipFile
from dgeotoolkit.dgeoflow.dgeoflowmodel import DGeoFlowModel


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


def test_basic():
    dgm = DGeoFlowModel.parse("tests/testdata/dgeoflow/sample01.flox")
    i = 1


# TODO serialize and test
def test_serialize_basic():
    dgm = DGeoFlowModel.parse("tests/testdata/dgeoflow/sample01.flox")
    dgm.serialize(path="tests/testdata/output/sample01.flox")
    check_files(
        "tests/testdata/dgeoflow/sample01.flox", "tests/testdata/output/sample01.flox"
    )
