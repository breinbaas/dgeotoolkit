from pydantic import ConfigDict
from typing import List, Optional, Union, Dict

from ..const import NAN, CURRENT_CONTENT_VERSION
from ..models.basemodel import DGKTBaseModel, DGKTBaseModelPath


####################
# NEED TO GO FIRST #
####################
class DGKTPoint(DGKTBaseModel):
    X: float = NAN
    Z: float = NAN


class DGKTCircle(DGKTBaseModel):
    Center: DGKTPoint = DGKTPoint()
    Radius: float = NAN


class DGKTConsolidation(DGKTBaseModel):
    LayerId: str = ""
    Degree: float = 0


class DGKTGridEnhancements(DGKTBaseModel):
    ExtrapolateSearchSpace: bool = True


class DGKTLayer(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTPoint] = []


class DGKTSearchGrid(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    BottomLeft: Optional[DGKTPoint] = None
    Space: float = 1.0
    NumberOfPointsInX: int = 5
    NumberOfPointsInZ: int = 5


class DGKTTangentLines(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    BottomTangentLineZ: float = 0.0
    Space: float = 1.0
    NumberOfTangentLines: int = 5


class DGKTSlipPlaneConstraintsBishop(DGKTBaseModel):
    IsSizeConstraintsEnabled: bool = True
    MinimumSlipPlaneDepth: float = 1.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class DGKTSlipPlaneUpliftVan(DGKTBaseModel):
    FirstCircleCenter: DGKTPoint = DGKTPoint()
    FirstCircleRadius: float = 0.0
    SecondCircleCenter: DGKTPoint = DGKTPoint()


class DGKTUpliftVan(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlane: DGKTSlipPlaneUpliftVan = DGKTSlipPlaneUpliftVan()


class DGKTSearchArea(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopLeft: Optional[DGKTPoint] = DGKTPoint()
    Width: float = 0.0
    Height: float = 0.0


class DGKTTangentArea(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopZ: Optional[float] = None
    Height: float = 0.0


class DGKTSlipPlaneConstraintsUpliftVanParticleSwarm(DGKTBaseModel):
    IsSizeConstraintsEnabled: bool = False
    MinimumSlipPlaneDepth: float = 0.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class DGKTUpliftVanParticleSwarm(DGKTBaseModel):
    SearchAreaA: DGKTSearchArea = DGKTSearchArea()
    SearchAreaB: DGKTSearchArea = DGKTSearchArea()
    TangentArea: DGKTTangentArea = DGKTTangentArea()
    SlipPlaneConstraints: DGKTSlipPlaneConstraintsUpliftVanParticleSwarm = (
        DGKTSlipPlaneConstraintsUpliftVanParticleSwarm()
    )
    OptionsType: str = "Default"


class DGKTSlipPlaneConstraintsSpencer(DGKTBaseModel):
    IsEnabled: bool = False
    MinimumAngleBetweenSlices: float = 0.0
    MinimumThrustLinePercentageInsideSlices: float = 0.0


class DGKTSpencer(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlane: Optional[List[DGKTPoint]] = []
    SlipPlaneConstraints: DGKTSlipPlaneConstraintsSpencer = (
        DGKTSlipPlaneConstraintsSpencer()
    )


class DGKTSpencerGenetic(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlaneA: Optional[List[DGKTPoint]] = []
    SlipPlaneB: Optional[List[DGKTPoint]] = []
    OptionsType: str = "Default"
    SlipPlaneConstraints: DGKTSlipPlaneConstraintsSpencer = (
        DGKTSlipPlaneConstraintsSpencer()
    )


class DGKTForbiddenLine(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: DGKTPoint = DGKTPoint()
    End: DGKTPoint = DGKTPoint()


class DGKTGeotextile(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: DGKTPoint = DGKTPoint()
    End: DGKTPoint = DGKTPoint()
    TensileStrength: float = 0.0
    ReductionArea: float = 0.0


class DGKTStress(DGKTBaseModel):
    Distance: float = 0.0
    Stress: float = 0.0


class DGKTNail(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Location: DGKTPoint = DGKTPoint()
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
    LateralStresses: List[DGKTStress] = []
    ShearStresses: List[DGKTStress] = []


class DGKTStochasticParameter(DGKTBaseModel):
    IsProbabilistic: bool = False
    Mean: float = 1.0
    StandardDeviation: float = 0.0


class DGKTStateStress(DGKTBaseModel):
    StateType: str = ""
    Pop: float = 0.0
    PopStochasticParameter: DGKTStochasticParameter = DGKTStochasticParameter()
    Ocr: float = 1.0
    YieldStress: float = 0.0


class DGKTStateCorrelation(DGKTBaseModel):
    pass  # TODO


class DGKTStatePoint(DGKTBaseModel):
    Id: str = ""
    LayerId: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    IsProbabilistic: bool = True
    Point: DGKTPoint = DGKTPoint()
    Stress: DGKTStateStress = DGKTStateStress()


class DGKTStateLineValue(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    X: float = NAN
    IsProbabilistic: bool = True
    IsAboveAndBelowCorrelated: bool = True
    Above: DGKTStateStress = DGKTStateStress()
    Below: DGKTStateStress = DGKTStateStress()


class DGKTStateLine(DGKTBaseModel):
    Points: List[DGKTPoint] = []
    Values: List[DGKTStateLineValue] = []


class DGKTSpencerSlice(DGKTBaseModel):
    LeftForce: float = NAN
    LeftForceY: float = NAN
    LeftForceAngle: float = NAN
    RightForce: float = NAN
    RightForceY: float = NAN
    RightForceAngle: float = NAN
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGKTPoint = DGKTPoint()
    BottomRight: DGKTPoint = DGKTPoint()
    TopLeft: DGKTPoint = DGKTPoint()
    TopRight: DGKTPoint = DGKTPoint()
    CohesionInput: float = NAN
    DegreeOfConsolidationLoadPorePressure: float = NAN
    DegreeOfConsolidationPorePressure: float = NAN
    EffectiveStress: float = NAN
    HorizontalPorePressure: float = NAN
    HorizontalSoilQuakeStress: float = NAN
    HydrostaticPorePressure: float = NAN
    Label: Optional[str] = ""
    LoadStress: float = NAN
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
    ShearStrengthModelType: str = ""


class DGKTUpliftVanSlice(DGKTBaseModel):
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGKTPoint = DGKTPoint()
    BottomRight: DGKTPoint = DGKTPoint()
    TopLeft: DGKTPoint = DGKTPoint()
    TopRight: DGKTPoint = DGKTPoint()
    CohesionInput: float = NAN
    DegreeOfConsolidationLoadPorePressure: float = NAN
    DegreeOfConsolidationPorePressure: float = NAN
    EffectiveStress: float = NAN
    HorizontalPorePressure: float = NAN
    HorizontalSoilQuakeStress: float = NAN
    HydrostaticPorePressure: float = NAN
    Label: Optional[str] = ""
    LoadStress: float = NAN
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
    ShearStrengthModelType: str = ""


class DGKTBishopSlice(DGKTBaseModel):
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGKTPoint = DGKTPoint()
    BottomRight: DGKTPoint = DGKTPoint()
    TopLeft: DGKTPoint = DGKTPoint()
    TopRight: DGKTPoint = DGKTPoint()
    CohesionInput: float = 0.0
    DegreeOfConsolidationLoadPorePressure: float = 0.0
    DegreeOfConsolidationPorePressure: float = 0.0
    EffectiveStress: float = 0.0
    HorizontalPorePressure: float = 0.0
    HorizontalSoilQuakeStress: float = 0.0
    HydrostaticPorePressure: float = 0.0
    Label: Optional[str] = ""
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


class DGKTSoilLayerConnection(DGKTBaseModel):
    LayerId: str = ""
    SoilId: str = ""


class DGKTDitchCharacteristics(DGKTBaseModel):
    DitchEmbankmentSide: float = NAN
    DitchBottomEmbankmentSide: float = NAN
    DitchBottomLandSide: float = NAN
    DitchLandSide: float = NAN


class DGKTEmbankmentCharacteristics(DGKTBaseModel):
    EmbankmentToeWaterSide: float = NAN
    EmbankmentTopWaterSide: float = NAN
    EmbankmentTopLandSide: float = NAN
    ShoulderBaseLandSide: float = NAN
    EmbankmentToeLandSide: float = NAN


class DGKTSuTablePoint(DGKTBaseModel):
    EffectiveStress: float = 0.0
    Su: float = 0.0


class DGKTSuTable(DGKTBaseModel):
    StrengthIncreaseExponent: float = 0.0
    StrengthIncreaseExponentStochasticParameter: DGKTStochasticParameter = (
        DGKTStochasticParameter()
    )
    SuTablePoints: List[DGKTSuTablePoint] = []
    IsSuTableProbabilistic: bool = False
    SuTableVariationCoefficient: float = 0.0


class DGKTHeadLine(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTPoint] = []


class DGKTReferenceLine(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopHeadLineId: str = ""
    BottomHeadLineId: str = ""
    Points: List[DGKTPoint] = []


class DGKTStage(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    GeometryId: str = ""
    DecorationsId: str = ""
    SoilLayersId: str = ""
    WaternetId: str = ""
    WaternetCreatorSettingsId: str = ""
    StateId: str = ""
    StateCorrelationsId: str = ""
    LoadsId: str = ""
    ReinforcementsId: str = ""


class DGKTCalculation(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    CalculationSettingsId: str = ""
    ResultId: Optional[str] = ""


class DGKTExcavation(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTPoint] = []


class DGKTElevation(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTPoint] = []
    AddedLayerId: str = ""


class DGKTTree(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Force: float = 0.0
    RootZoneWidth: float = 5.0
    Spread: float = 0.0
    Location: DGKTPoint = DGKTPoint()


#########################
#          A            #
#########################


#########################
#          B            #
#########################
class DGKTBishop(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Circle: DGKTCircle = DGKTCircle()


class DGKTBishopBruteForce(DGKTBaseModel):
    SearchGrid: DGKTSearchGrid = DGKTSearchGrid()
    TangentLines: DGKTTangentLines = DGKTTangentLines()
    GridEnhancements: DGKTGridEnhancements = DGKTGridEnhancements()
    SlipPlaneConstraints: DGKTSlipPlaneConstraintsBishop = (
        DGKTSlipPlaneConstraintsBishop()
    )


class DGKTBishopBruteForceResult(DGKTBaseModelPath):
    path_name: str = "results/bishopbruteforce"
    Circle: DGKTCircle = DGKTCircle()
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTPoint] = []
    Slices: List[DGKTBishopSlice] = []


class DGKTBishopResult(DGKTBaseModelPath):
    path_name: str = "results/bishop"
    Circle: DGKTCircle = DGKTCircle()
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTPoint] = []
    Slices: List[DGKTBishopSlice] = []


#########################
#          C            #
#########################
class DGKTCalculationSettings(DGKTBaseModelPath):
    path_name: str = "calculationsettings"
    Id: str = ""
    AnalysisType: str = ""
    CalculationType: str = "Deterministic"
    ModelFactorMean: float = 1.0
    ModelFactorStandardDeviation: float = 0.0
    Bishop: DGKTBishop = DGKTBishop()
    BishopBruteForce: DGKTBishopBruteForce = DGKTBishopBruteForce()
    UpliftVan: DGKTUpliftVan = DGKTUpliftVan()
    UpliftVanParticleSwarm: DGKTUpliftVanParticleSwarm = DGKTUpliftVanParticleSwarm()
    Spencer: DGKTSpencer = DGKTSpencer()
    SpencerGenetic: DGKTSpencerGenetic = DGKTSpencerGenetic()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          D            #
#########################
class DGKTDecorations(DGKTBaseModelPath):
    path_name: str = "decorations"
    Id: str = ""
    Excavations: List[DGKTExcavation] = []
    Elevations: List[DGKTElevation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          E            #
#########################
class DGKTEarthquake(DGKTBaseModel):
    IsEnabled: bool = False
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    HorizontalFactor: float = 0.0
    VerticalFactor: float = 0.0
    FreeWaterFactor: float = 0.0
    Consolidations: List[DGKTConsolidation] = []


#########################
#          F            #
#########################


#########################
#          G            #
#########################


class DGKTGeometry(DGKTBaseModelPath):
    path_name: str = "geometries"
    Id: str = ""
    Layers: List[DGKTLayer] = []
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
class DGKTLayerLoad(DGKTBaseModel):
    LayerId: str = ""
    Consolidations: List[DGKTConsolidation] = []


class DGKTLineLoad(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Location: DGKTPoint = DGKTPoint()
    Magnitude: float = 10.0
    Spread: float = 0.0
    Angle: float = 0.0
    Consolidations: List[DGKTConsolidation] = []


class DGKTLoads(DGKTBaseModelPath):
    path_name: str = "loads"
    Id: str = ""
    LayerLoads: List[DGKTLayerLoad] = []
    UniformLoads: List["DGKTUniformLoad"] = []
    LineLoads: List[DGKTLineLoad] = []
    Trees: List[DGKTTree] = []
    Earthquake: DGKTEarthquake = DGKTEarthquake()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          M            #
#########################


#########################
#          N            #
#########################
class DGKTNailPropertiesForSoils(DGKTBaseModel):
    NailPropertiesForSoils: List[Dict] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          O            #
#########################


#########################
#          P            #
#########################


class DGKTProjectInfo(DGKTBaseModel):
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


class DGKTResult(DGKTBaseModel):
    pass


class DGKTReinforcements(DGKTBaseModelPath):
    path_name: str = "reinforcements"
    Id: str = ""
    ForbiddenLines: List[DGKTForbiddenLine] = []
    Geotextiles: List[DGKTGeotextile] = []
    Nails: List[DGKTNail] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          S            #
#########################


class DGKTScenario(DGKTBaseModelPath):
    path_name: str = "scenarios"
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Stages: List[DGKTStage] = []
    Calculations: List[DGKTCalculation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSoil(DGKTBaseModel):
    Id: str = ""
    Name: str = ""
    Notes: Optional[str] = ""
    Code: str = ""
    IsProbabilistic: bool = False
    VolumetricWeightAbovePhreaticLevel: float = 0.0
    VolumetricWeightBelowPhreaticLevel: float = 0.0
    ShearStrengthModelTypeAbovePhreaticLevel: str = ""
    ShearStrengthModelTypeBelowPhreaticLevel: str = ""
    Cohesion: float = 0.0
    CohesionStochasticParameter: DGKTStochasticParameter = DGKTStochasticParameter()
    FrictionAngle: float = 0.0
    FrictionAngleStochasticParameter: DGKTStochasticParameter = (
        DGKTStochasticParameter()
    )
    CohesionAndFrictionAngleCorrelated: bool = False
    Dilatancy: float = 0.0
    DilatancyStochasticParameter: DGKTStochasticParameter = DGKTStochasticParameter()
    ShearStrengthRatio: float = 0.0
    ShearStrengthRatioStochasticParameter: DGKTStochasticParameter = (
        DGKTStochasticParameter()
    )
    StrengthIncreaseExponent: float = 0.0
    StrengthIncreaseExponentStochasticParameter: DGKTStochasticParameter = (
        DGKTStochasticParameter()
    )
    ShearStrengthRatioAndShearStrengthExponentCorrelated: bool = False
    SuTable: DGKTSuTable = DGKTSuTable()


class DGKTSoils(DGKTBaseModel):
    Soils: List[DGKTSoil] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSoilLayers(DGKTBaseModelPath):
    Id: str = ""
    path_name: str = "soillayers"
    SoilLayers: List[DGKTSoilLayerConnection] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSoilCorrelations(DGKTBaseModel):
    SoilCorrelations: List[Dict] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSoilVisualization(DGKTBaseModel):
    SoilId: str = ""
    Color: str = ""
    PersistableShadingType: str = ""


class DGKTSoilVisualizations(DGKTBaseModel):
    SoilVisualizations: List[DGKTSoilVisualization] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSpencerResult(DGKTBaseModelPath):
    path_name: str = "results/spencer"
    SlipPlane: List[DGKTPoint] = []
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTPoint] = []
    Slices: List[DGKTSpencerSlice] = []


class DGKTSpencerGeneticAlgorithmResult(DGKTBaseModelPath):
    path_name: str = "results/spencergeneticalgorithm"
    SlipPlane: List[DGKTPoint] = []
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTPoint] = []
    Slices: List[DGKTSpencerSlice] = []


class DGKTStates(DGKTBaseModelPath):
    path_name: str = "states"
    Id: str = ""
    StatePoints: List[DGKTStatePoint] = []
    StateLines: List[DGKTStateLine] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTStateCorrelations(DGKTBaseModelPath):
    path_name: str = "statecorrelations"
    Id: str = ""
    StateCorrelations: List[DGKTStateCorrelation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          T            #
#########################


#########################
#          U            #
#########################


class DGKTUniformLoad(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: float = 0.0
    End: float = 0.0
    Magnitude: float = 0.0
    Spread: float = 0.0
    Consolidations: List[DGKTConsolidation] = []


class DGKTUpliftVanResult(DGKTBaseModelPath):
    path_name: str = "results/upliftvan"
    LeftCenter: DGKTPoint = DGKTPoint()
    RightCenter: DGKTPoint = DGKTPoint()
    TangentLine: float = NAN
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTPoint] = []
    Slices: List[DGKTUpliftVanSlice] = []


class DGKTUpliftVanParticleSwarmResult(DGKTBaseModelPath):
    path_name: str = "results/upliftvanparticleswarm"
    LeftCenter: DGKTPoint = DGKTPoint()
    RightCenter: DGKTPoint = DGKTPoint()
    TangentLine: float = NAN
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTPoint] = []
    Slices: List[DGKTUpliftVanSlice] = []


#########################
#          V            #
#########################


#########################
#          W            #
#########################


class DGKTWaternetCreatorSettings(DGKTBaseModelPath):
    path_name: str = "waternetcreatorsettings"
    Id: str = ""
    EmbankmentCharacteristics: DGKTEmbankmentCharacteristics = (
        DGKTEmbankmentCharacteristics()
    )
    DitchCharacteristics: DGKTDitchCharacteristics = DGKTDitchCharacteristics()
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
    DrainageConstruction: DGKTPoint = DGKTPoint()
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


class DGKTWaternets(DGKTBaseModelPath):
    path_name: str = "waternets"
    Id: str = ""
    UnitWeightWater: float = 9.81
    PhreaticLineId: Optional[str] = None
    HeadLines: List[DGKTHeadLine] = []
    ReferenceLines: List[DGKTReferenceLine] = []
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
