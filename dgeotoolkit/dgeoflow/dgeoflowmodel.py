from pydantic import BaseModel
from typing import Optional, List

from models.basemodel import DGKTBaseModel, DGKTBaseModelPath
from ..const import NAN, CURRENT_CONTENT_VERSION
from ..shared.dataclasses import *


class DGeoFlowModel(BaseModel):
    BoundaryConditions: List[DGKTFBoundaryConditions] = []
    Geometries: List[DGKTFGeometry] = []
    MeshProperties: List[DGKTFMeshProperties] = []
    Scenarios: List[DGKTFScenarios] = []
    SoilLayers: List[DGKTFSoilLayers] = []

    ProjectInfo: DGKTFProjectInfo = DGKTFProjectInfo()
    Soils: DGKTFSoils = DGKTFSoils()
    SoilVisualizations: DGKTFSoilVisualizations = DGKTFSoilVisualizations()
