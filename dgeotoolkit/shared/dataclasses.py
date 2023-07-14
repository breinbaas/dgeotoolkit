from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Union, Dict

from ..const import NAN, CURRENT_CONTENT_VERSION


####################
# NEED TO GO FIRST #
####################
class Point(BaseModel):
    X: float = NAN
    Z: float = NAN


class CircleObject(BaseModel):
    Center: Point = Point()
    Radius: float = NAN


class Consolidation(BaseModel):
    LayerId: str = ""
    Degree: float = 0


class GridEnhancementsObject(BaseModel):
    ExtrapolateSearchSpace: bool = True


class Layer(BaseModel):
    Id: str = ""
    Label: str = ""
    Notes: str = ""
    Points: List[Point] = []


class SearchGridObject(BaseModel):
    Label: str = ""
    Notes: str = ""
    BottomLeft: Optional[Point] = None
    Space: float = 1.0
    NumberOfPointsInX: int = 5
    NumberOfPointsInZ: int = 5


class TangentLinesObject(BaseModel):
    Label: str = ""
    Notes: str = ""
    BottomTangentLineZ: float = 0.0
    Space: float = 1.0
    NumberOfTangentLines: int = 5


class SlipPlaneConstraintsBishop(BaseModel):
    IsSizeConstraintsEnabled: bool = True
    MinimumSlipPlaneDepth: float = 1.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class SlipPlaneUpliftVan(BaseModel):
    FirstCircleCenter: Point = Point()
    FirstCircleRadius: float = 0.0
    SecondCircleCenter: Point = Point()


class UpliftVanObject(BaseModel):
    Label: str = ""
    Notes: str = ""
    SlipPlane: SlipPlaneUpliftVan = SlipPlaneUpliftVan()


class SearchArea(BaseModel):
    Label: str = ""
    Notes: str = ""
    TopLeft: Optional[Point] = Point()
    Width: float = 0.0
    Height: float = 0.0


class TangentAreaObject(BaseModel):
    Label: str = ""
    Notes: str = ""
    TopZ: Optional[float] = None
    Height: float = 0.0


class SlipPlaneConstraintsUpliftVanParticleSwarm(BaseModel):
    IsSizeConstraintsEnabled: bool = False
    MinimumSlipPlaneDepth: float = 0.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class UpliftVanParticleSwarmObject(BaseModel):
    SearchAreaA: SearchArea = SearchArea()
    SearchAreaB: SearchArea = SearchArea()
    TangentArea: TangentAreaObject = TangentAreaObject()
    SlipPlaneConstraints: SlipPlaneConstraintsUpliftVanParticleSwarm = (
        SlipPlaneConstraintsUpliftVanParticleSwarm()
    )
    OptionsType: str = "Default"


class SpencerObject(BaseModel):
    Label: str = ""
    Notes: str = ""
    SlipPlane: Optional[List[Point]] = []


class SlipPlaneConstraintsSpencer(BaseModel):
    IsEnabled: bool = False
    MinimumAngleBetweenSlices: float = 0.0
    MinimumThrustLinePercentageInsideSlices: float = 0.0


class SpencerGeneticObject(BaseModel):
    Label: str = ""
    Notes: str = ""
    SlipPlaneA: Optional[List[Point]] = []
    SlipPlaneB: Optional[List[Point]] = []
    OptionsType: str = "Default"
    SlipPlaneConstraints: SlipPlaneConstraintsSpencer = SlipPlaneConstraintsSpencer()
    OptionsType: str = "Default"


class ForbiddenLine(BaseModel):
    Label: Optional[str] = ""
    Notes: str = ""
    Start: Point = Point()
    End: Point = Point()


class Geotextile(BaseModel):
    Label: Optional[str] = ""
    Notes: str = ""
    Start: Point = Point()
    End: Point = Point()
    TensileStrength: float = 0.0
    ReductionArea: float = 0.0


class Stress(BaseModel):
    Distance: float = 0.0
    Stress: float = 0.0


class Nail(BaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Location: Point = Point()
    Direction: float = 0.0
    HorizontalSpacing: float = 0.0
    Length: float = 3.0
    Diameter: float = 0.1
    GroutDiameter: float = 0.0
    CriticalAngle: float = 0.0
    MaxPullForce: float = 0.0
    PlasticMoment: float = (0.0,)
    BendingStiffness: float = 0.0
    UseFacing: bool = False
    UseLateralStress: bool = False
    UseShearStress: bool = False
    LateralStresses: List[Stress] = []
    ShearStresses: List[Stress] = []


class StateCorrelation(BaseModel):
    pass


class StatePoint(BaseModel):
    pass


class StateLine(BaseModel):
    pass


class Slice(BaseModel):
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: Point = Point()
    BottomRight: Point = Point()
    TopLeft: Point = Point()
    TopRight: Point = Point()
    CohesionInput: float = 0.0
    DegreeOfConsolidationLoadPorePressure: float = 0.0
    DegreeOfConsolidationPorePressure: float = 0.0
    EffectiveStress: float = 0.0
    HorizontalPorePressure: float = 0.0
    HorizontalSoilQuakeStress: float = 0.0
    HydrostaticPorePressure: float = 0.0
    Label: str = ""
    LoadStress: float = 0.0
    MInput: float = NAN
    NormalStress: float = NAN
    Ocr: float = NAN
    PhiInput: float = NAN
    PiezometricPorePressure: float = NAN
    Pop: float = NAN
    ShearStress: float = NAN
    SInput: float = NAN
    SurfacePorePressure: float = NAN
    TopAngle: float = NAN
    TotalPorePressure: float = NAN
    TotalStress: float = NAN
    VerticalPorePressure: float = NAN
    VerticalSoilQuakeStress: float = NAN
    WaterQuakeStress: float = NAN
    Weight: float = NAN
    Width: float = NAN
    YieldStress: float = NAN
    CohesionOutput: float = NAN
    DilatancyInput: float = NAN
    DilatancyOutput: float = NAN
    PhiOutput: float = NAN
    SuOutput: float = NAN
    UpliftFactor: float = NAN
    ShearStrengthModelType: str = "CPhi"


class SoilLayerConnection(BaseModel):
    LayerId: str = ""
    SoilId: str = ""


class DitchCharacteristicsObject(BaseModel):
    DitchEmbankmentSide: float = NAN
    DitchBottomEmbankmentSide: float = NAN
    DitchBottomLandSide: float = NAN
    DitchLandSide: float = NAN


class EmbankmentCharacteristicsObject(BaseModel):
    EmbankmentToeWaterSide: float = NAN
    EmbankmentTopWaterSide: float = NAN
    EmbankmentTopLandSide: float = NAN
    ShoulderBaseLandSide: float = NAN
    EmbankmentToeLandSide: float = NAN


class StochasticParameter(BaseModel):
    IsProbabilistic: bool = False
    Mean: float = 1.0
    StandardDeviation: float = 0.0


class SuTablePoint(BaseModel):
    EffectiveStress: float = 0.0
    Su: float = 0.0


class SuTableObject(BaseModel):
    StrengthIncreaseExponent: float = 0.0
    StrengthIncreaseExponentStochasticParameter: StochasticParameter = (
        StochasticParameter()
    )
    SuTablePoints: List[SuTablePoint] = []
    IsSuTableProbabilistic: bool = False
    SuTableVariationCoefficient: float = 0.0


class HeadLine(BaseModel):
    Id: str = ""
    Label: str = ""
    Notes: str = ""
    Points: List[Point] = []


class ReferenceLine(BaseModel):
    Id: str = ""
    Label: str = ""
    Notes: str = ""
    TopHeadLineId: str = ""
    BottomHeadLineId: str = ""
    Points: List[Point] = []


class Stage(BaseModel):
    Id: str = ""
    Label: str = ""
    Notes: str = ""
    GeometryId: str = ""
    DecorationsId: str = ""
    SoilLayersId: str = ""
    WaternetId: str = ""
    WaternetCreatorSettingsId: str = ""
    StateId: str = ""
    StateCorrelationsId: str = ""
    LoadsId: str = ""
    ReinforcementsId: str = ""


class Calculation(BaseModel):
    Id: str = ""
    Label: str = ""
    Notes: str = ""
    CalculationSettingsId: str = ""
    ResultId: Optional[str] = ""


class Excavation(BaseModel):
    Label: str = ""
    Notes: str = ""
    Points: List[Point] = []


class Elevation(BaseModel):
    Label: str = ""
    Notes: str = ""
    Points: List[Point] = []
    AddedLayerId: str = ""


#########################
#          A            #
#########################


#########################
#          B            #
#########################
class BishopObject(BaseModel):
    Label: str = ""
    Notes: str = ""
    Circle: CircleObject = CircleObject()


class BishopBruteForceObject(BaseModel):
    SearchGrid: SearchGridObject = SearchGridObject()
    TangentLines: TangentLinesObject = TangentLinesObject()
    GridEnhancements: GridEnhancementsObject = GridEnhancementsObject()
    SlipPlaneConstraints: SlipPlaneConstraintsBishop = SlipPlaneConstraintsBishop()


class BishopBruteForceResultObject(BaseModel):
    Circle: CircleObject = CircleObject()
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[Point] = []
    Slices: List[Slice] = []


#########################
#          C            #
#########################
class CalculationSettingsObject(BaseModel):
    Id: str = ""
    AnalysisType: str = ""
    CalculationType: str = "Deterministic"
    ModelFactorMean: float = 1.0
    ModelFactorStandardDeviation: float = 0.0
    Bishop: BishopObject = BishopObject()
    BishopBruteForce: BishopBruteForceObject = BishopBruteForceObject()
    UpliftVan: UpliftVanObject = UpliftVanObject()
    UpliftVanParticleSwarm: UpliftVanParticleSwarmObject = (
        UpliftVanParticleSwarmObject()
    )
    Spencer: SpencerObject = SpencerObject()
    SpencerGenetic: SpencerGeneticObject = SpencerGeneticObject()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          D            #
#########################
class DecorationsObject(BaseModel):
    Id: str = ""
    Excavations: List[Excavation] = []
    Elevations: List[Elevation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          E            #
#########################
class EarthquakeObject(BaseModel):
    IsEnabled: bool = False
    Label: Optional[str] = ""
    Notes: str = ""
    HorizontalFactor: float = 0.0
    VerticalFactor: float = 0.0
    FreeWaterFactor: float = 0.0
    Consolidations: List[Consolidation] = []


#########################
#          F            #
#########################


#########################
#          G            #
#########################


class GeometryObject(BaseModel):
    Id: str = ""
    Layers: List[Layer] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          H            #
#########################

#########################
#          I            #
#########################

#########################
#          J            #
#########################

#########################
#          K            #
#########################


#########################
#          L            #
#########################
class LayerLoad(BaseModel):
    LayerId: str = ""
    Consolidations: List[Consolidation] = []


class LineLoad(BaseModel):
    pass


class LoadsObject(BaseModel):
    Id: str = ""
    LayerLoads: List[LayerLoad] = []
    UniformLoads: List["UniformLoad"] = []
    LineLoads: List[LineLoad] = []
    Trees: List["Tree"] = []
    Earthquake: EarthquakeObject = EarthquakeObject()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          M            #
#########################


#########################
#          N            #
#########################
class NailPropertiesForSoilsObject(BaseModel):
    NailPropertiesForSoils: List[Dict] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          O            #
#########################


#########################
#          P            #
#########################


class ProjectInfoObject(BaseModel):
    Path: str = ""
    Project: str = ""
    CrossSection: str = ""
    Remarks: str = ""
    Analyst: str = ""
    LastModifier: str = ""
    Date: Optional[str] = ""
    LastModified: str = ""
    Created: str = ""
    ApplicationCreated: str = ""
    ApplicationModified: str = ""
    IsDataValidated: bool = True
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          Q            #
#########################

#########################
#          R            #
#########################


class ReinforcementsObject(BaseModel):
    Id: str = ""
    ForbiddenLines: List[ForbiddenLine] = []
    Geotextiles: List[Geotextile] = []
    Nails: List[Nail] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          S            #
#########################


class ScenarioObject(BaseModel):
    Id: str = ""
    Label: str = ""
    Notes: str = ""
    Stages: List[Stage] = []
    Calculations: List[Calculation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class Soil(BaseModel):
    Id: str = ""
    Name: str = ""
    Notes: str = ""
    Code: str = ""
    IsProbabilistic: bool = False
    VolumetricWeightAbovePhreaticLevel: float = 0.0
    VolumetricWeightBelowPhreaticLevel: float = 0.0
    ShearStrengthModelTypeAbovePhreaticLevel: str = ""
    ShearStrengthModelTypeBelowPhreaticLevel: str = ""
    Cohesion: float = 0.0
    CohesionStochasticParameter: StochasticParameter = StochasticParameter()
    FrictionAngle: float = 0.0
    FrictionAngleStochasticParameter: StochasticParameter = StochasticParameter()
    CohesionAndFrictionAngleCorrelated: bool = False
    Dilatancy: float = 0.0
    DilatancyStochasticParameter: StochasticParameter = StochasticParameter()
    ShearStrengthRatio: float = 0.0
    ShearStrengthRatioStochasticParameter: StochasticParameter = StochasticParameter()
    StrengthIncreaseExponent: float = 0.0
    StrengthIncreaseExponentStochasticParameter: StochasticParameter = (
        StochasticParameter()
    )
    ShearStrengthRatioAndShearStrengthExponentCorrelated: bool = False
    SuTable: SuTableObject = SuTableObject()


class SoilsObject(BaseModel):
    Soils: List[Soil] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class SoilLayersObject(BaseModel):
    SoilLayers: List[SoilLayerConnection] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class SoilCorrelationsObject(BaseModel):
    SoilCorrelations: List[Dict] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class SoilVisualization(BaseModel):
    SoilId: str = ""
    Color: str = ""
    PersistableShadingType: str = ""


class SoilVisualizationsObject(BaseModel):
    SoilVisualizations: List[SoilVisualization] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class Stage(BaseModel):
    Id: str = ""
    Label: str = ""
    Notes: str = ""
    GeometryId: str = ""
    DecorationsId: str = ""
    SoilLayersId: str = ""
    WaternetId: str = ""
    WaternetCreatorSettingsId: str = ""
    StateId: str = ""
    StateCorrelationsId: str = ""
    LoadsId: str = ""
    ReinforcementsId: str = ""
    CalculationSettingsId: str = ""
    ResultId: str = ""
    ContentVersion: str = CURRENT_CONTENT_VERSION


class StatesObject(BaseModel):
    Id: str = ""
    StatePoints: List[StatePoint] = []
    StateLines: List[StateLine] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class StateCorrelationsObject(BaseModel):
    Id: str = ""
    StateCorrelations: List[StateCorrelation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          T            #
#########################


class Tree(BaseModel):
    pass


#########################
#          U            #
#########################


class UniformLoad(BaseModel):
    Label: str = ""
    Notes: str = ""
    Start: float = 0.0
    End: float = 0.0
    Magnitude: float = 0.0
    Spread: float = 0.0
    Consolidations: List[Consolidation] = []


#########################
#          V            #
#########################


#########################
#          W            #
#########################


class WaternetCreatorSettingsObject(BaseModel):
    Id: str = ""
    EmbankmentCharacteristics: EmbankmentCharacteristicsObject = (
        EmbankmentCharacteristicsObject()
    )
    DitchCharacteristics: DitchCharacteristicsObject = DitchCharacteristicsObject()
    IsDitchPresent: bool = False
    EmbankmentSoilScenario: str = "ClayEmbankmentOnClay"
    NormativeWaterLevel: float = NAN
    MeanWaterLevel: float = NAN
    WaterLevelHinterland: float = NAN
    InitialLevelEmbankmentTopWaterSide: float = NAN
    InitialLevelEmbankmentTopLandSide: float = NAN
    UseDefaultOffsets: bool = True
    OffsetEmbankmentTopWaterSide: float = NAN
    OffsetEmbankmentTopLandSide: float = NAN
    OffsetShoulderBaseLandSide: float = NAN
    OffsetEmbankmentToeLandSide: float = NAN
    IsDrainageConstructionPresent: bool = False
    DrainageConstruction: Point = Point()
    AquiferLayerId: Optional[str] = None
    AquiferInsideAquitardLayerId: Optional[str] = None
    AdjustForUplift: bool = False
    IsAquiferLayerInsideAquitard: bool = False
    PleistoceneLeakageLengthOutwards: float = NAN
    AquiferLayerInsideAquitardLeakageLengthOutwards: float = NAN
    PleistoceneLeakageLengthInwards: float = NAN
    AquiferLayerInsideAquitardLeakageLengthInwards: float = NAN
    AquitardHeadWaterSide: float = NAN
    AquitardHeadLandSide: float = NAN
    IntrusionLength: float = NAN
    ContentVersion: str = CURRENT_CONTENT_VERSION


class WaternetsObject(BaseModel):
    Id: str = ""
    UnitWeightWater: float = 9.81
    PhreaticLineId: Optional[str] = None
    HeadLines: List[HeadLine] = []
    ReferenceLines: List[ReferenceLine] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          X            #
#########################

#########################
#          Y            #
#########################

#########################
#          Z            #
#########################
