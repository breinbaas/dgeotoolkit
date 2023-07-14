from pydantic import BaseModel

from ..shared.dataclasses import *


class DStabilityModel(BaseModel):
    CalculationSettings: List[CalculationSettingsObject] = [CalculationSettingsObject()]
    Decorations: List[DecorationsObject] = [DecorationsObject()]
    Geometry: List[GeometryObject] = [GeometryObject()]
    Loads: List[LoadsObject] = [LoadsObject()]
    Reinforcements: List[ReinforcementsObject] = [ReinforcementsObject()]
    BishopBruteForceResult: BishopBruteForceResultObject = [
        (BishopBruteForceResultObject())
    ]
    Scenario: List[ScenarioObject] = [ScenarioObject()]
    SoilLayers: List[SoilLayersObject] = [SoilLayersObject()]
    StateCorrelations: List[StateCorrelationsObject] = [StateCorrelationsObject()]
    States: List[StatesObject] = [StatesObject()]
    WaternetCreatorSettings: List[WaternetCreatorSettingsObject] = [
        (WaternetCreatorSettingsObject())
    ]
    Waternets: List[WaternetsObject] = [WaternetsObject()]
    NailPropertiesForSoils: NailPropertiesForSoilsObject = (
        NailPropertiesForSoilsObject()
    )
    ProjectInfo: ProjectInfoObject = ProjectInfoObject()
    SoilCorrelations: SoilCorrelationsObject = SoilCorrelationsObject()
    Soils: SoilsObject = SoilsObject()
    SoilVisualizations: SoilVisualizationsObject = SoilVisualizationsObject()
