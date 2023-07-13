from pydantic import BaseModel

from ..shared.dataclasses import *


class DStabilityModel(BaseModel):
    CalculationSettings: CalculationSettingsObject = CalculationSettingsObject()
    Decorations: DecorationsObject = DecorationsObject()
    Geometry: GeometryObject = GeometryObject()
    Loads: LoadsObject = LoadsObject()
    Reinforcements: ReinforcementsObject = ReinforcementsObject()
    BishopBruteForceResult: BishopBruteForceResultObject = (
        BishopBruteForceResultObject()
    )
    Scenario: ScenarioObject = ScenarioObject()
    SoilLayers: SoilLayersObject = SoilLayersObject()
    StateCorrelations: StateCorrelationsObject = StateCorrelationsObject()
    States: StatesObject = StatesObject()
    WaternetCreatorSettings: WaternetCreatorSettingsObject = (
        WaternetCreatorSettingsObject()
    )
    Waternets: WaternetsObject = WaternetsObject()
    NailPropertiesForSoils: NailPropertiesForSoilsObject = (
        NailPropertiesForSoilsObject()
    )
    ProjectInfo: ProjectInfoObject = ProjectInfoObject()
    SoilCorrelations: SoilCorrelationsObject = SoilCorrelationsObject()
    Soils: SoilsObject = SoilsObject()
    SoilVisualizations: SoilVisualizationsObject = SoilVisualizationsObject()
