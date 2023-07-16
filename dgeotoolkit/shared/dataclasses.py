from typing import List, Optional, Union, Dict

from ..const import NAN, CURRENT_CONTENT_VERSION
from ..models.basemodel import DGKTBaseModel, DGKTBaseModelPath


####################
# NEED TO GO FIRST #
####################


############
# DGEOFLOW #
############
class DGKTFPoint(DGKTBaseModel):
    X: float = NAN
    Z: float = NAN


class DGKTFSoil(DGKTBaseModel):
    Id: str = ""
    Name: Optional[str] = ""
    Code: str = ""
    Notes: Optional[str] = ""
    HorizontalPermeability: float = NAN
    VerticalPermeability: float = NAN


class DGKTFSoilVisualization(DGKTBaseModel):
    SoilId: str = ""
    Color: str = ""
    PersistableShadingType: str = ""


class DGKTFFixedHeadBoundaryConditionProperties(DGKTBaseModel):
    HeadLevel: float = NAN


class DGKTFBoundaryCondition(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTFPoint] = []
    FixedHeadBoundaryConditionProperties: DGKTFFixedHeadBoundaryConditionProperties = (
        DGKTFFixedHeadBoundaryConditionProperties()
    )


class DGKTFLayer(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTFPoint] = []


class DGKTFMeshProperty(DGKTBaseModel):
    LayerId: str = ""
    Label: str = ""
    ElementSize: float = NAN


class DGKTFStage(DGKTBaseModel):
    Label: str = ""
    Notes: Optional[str] = ""
    BoundaryConditionCollectionId: str = ""


class DGKTFPipeTrajectory(DGKTBaseModel):
    Label: str = ""
    Notes: Optional[str] = ""
    D70: float = NAN
    ElementSize: float = NAN
    ErosionDirection: str = ""
    Points: List[DGKTFPoint] = []


class DGKTFCriticalHeadSearchSpace(DGKTBaseModel):
    MinimumHeadLevel: float = NAN
    MaximumHeadLevel: float = NAN
    StepSize: float = NAN


class DGKTFSoilLayer(DGKTBaseModel):
    LayerId: str = ""
    SoilId: str = ""


class DGKTFCalculation(DGKTBaseModel):
    Label: str = ""
    Notes: Optional[str] = ""
    CalculationType: str = ""
    PipeTrajectory: DGKTFPipeTrajectory = DGKTFPipeTrajectory()
    CriticalHeadId: Optional[str] = ""
    CriticalHeadSearchSpace: DGKTFCriticalHeadSearchSpace = (
        DGKTFCriticalHeadSearchSpace()
    )
    MeshPropertiesId: str = ""
    ResultsId: str = ""


##############
# DSTABILITY #
##############
class DGKTSPoint(DGKTBaseModel):
    X: float = NAN
    Z: float = NAN


class DGKTSCircle(DGKTBaseModel):
    Center: DGKTSPoint = DGKTSPoint()
    Radius: float = NAN


class DGKTSConsolidation(DGKTBaseModel):
    LayerId: str = ""
    Degree: float = 0


class DGKTSGridEnhancements(DGKTBaseModel):
    ExtrapolateSearchSpace: bool = True


class DGKTSLayer(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTSPoint] = []


class DGKTSSearchGrid(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    BottomLeft: Optional[DGKTSPoint] = None
    Space: float = 1.0
    NumberOfPointsInX: int = 5
    NumberOfPointsInZ: int = 5


class DGKTSTangentLines(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    BottomTangentLineZ: float = 0.0
    Space: float = 1.0
    NumberOfTangentLines: int = 5


class DGKTSSlipPlaneConstraintsBishop(DGKTBaseModel):
    IsSizeConstraintsEnabled: bool = True
    MinimumSlipPlaneDepth: float = 1.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class DGKTSSlipPlaneUpliftVan(DGKTBaseModel):
    FirstCircleCenter: DGKTSPoint = DGKTSPoint()
    FirstCircleRadius: float = 0.0
    SecondCircleCenter: DGKTSPoint = DGKTSPoint()


class DGKTSUpliftVan(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlane: DGKTSSlipPlaneUpliftVan = DGKTSSlipPlaneUpliftVan()


class DGKTSSearchArea(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopLeft: Optional[DGKTSPoint] = DGKTSPoint()
    Width: float = 0.0
    Height: float = 0.0


class DGKTSTangentArea(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopZ: Optional[float] = None
    Height: float = 0.0


class DGKTSSlipPlaneConstraintsUpliftVanParticleSwarm(DGKTBaseModel):
    IsSizeConstraintsEnabled: bool = False
    MinimumSlipPlaneDepth: float = 0.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class DGKTSUpliftVanParticleSwarm(DGKTBaseModel):
    SearchAreaA: DGKTSSearchArea = DGKTSSearchArea()
    SearchAreaB: DGKTSSearchArea = DGKTSSearchArea()
    TangentArea: DGKTSTangentArea = DGKTSTangentArea()
    SlipPlaneConstraints: DGKTSSlipPlaneConstraintsUpliftVanParticleSwarm = (
        DGKTSSlipPlaneConstraintsUpliftVanParticleSwarm()
    )
    OptionsType: str = "Default"


class DGKTSSlipPlaneConstraintsSpencer(DGKTBaseModel):
    IsEnabled: bool = False
    MinimumAngleBetweenSlices: float = 0.0
    MinimumThrustLinePercentageInsideSlices: float = 0.0


class DGKTSSpencer(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlane: Optional[List[DGKTSPoint]] = []
    SlipPlaneConstraints: DGKTSSlipPlaneConstraintsSpencer = (
        DGKTSSlipPlaneConstraintsSpencer()
    )


class DGKTSSpencerGenetic(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlaneA: Optional[List[DGKTSPoint]] = []
    SlipPlaneB: Optional[List[DGKTSPoint]] = []
    OptionsType: str = "Default"
    SlipPlaneConstraints: DGKTSSlipPlaneConstraintsSpencer = (
        DGKTSSlipPlaneConstraintsSpencer()
    )


class DGKTSForbiddenLine(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: DGKTSPoint = DGKTSPoint()
    End: DGKTSPoint = DGKTSPoint()


class DGKTSGeotextile(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: DGKTSPoint = DGKTSPoint()
    End: DGKTSPoint = DGKTSPoint()
    TensileStrength: float = 0.0
    ReductionArea: float = 0.0


class DGKTSStress(DGKTBaseModel):
    Distance: float = 0.0
    Stress: float = 0.0


class DGKTSNail(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Location: DGKTSPoint = DGKTSPoint()
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
    LateralStresses: List[DGKTSStress] = []
    ShearStresses: List[DGKTSStress] = []


class DGKTStochasticParameter(DGKTBaseModel):
    IsProbabilistic: bool = False
    Mean: float = 1.0
    StandardDeviation: float = 0.0


class DGKTSStateStress(DGKTBaseModel):
    StateType: str = ""
    Pop: float = 0.0
    PopStochasticParameter: DGKTStochasticParameter = DGKTStochasticParameter()
    Ocr: float = 1.0
    YieldStress: float = 0.0


class DGKTSStateCorrelation(DGKTBaseModel):
    pass  # TODO


class DGKTSStatePoint(DGKTBaseModel):
    Id: str = ""
    LayerId: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    IsProbabilistic: bool = True
    Point: DGKTSPoint = DGKTSPoint()
    Stress: DGKTSStateStress = DGKTSStateStress()


class DGKTSStateLineValue(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    X: float = NAN
    IsProbabilistic: bool = True
    IsAboveAndBelowCorrelated: bool = True
    Above: DGKTSStateStress = DGKTSStateStress()
    Below: DGKTSStateStress = DGKTSStateStress()


class DGKTSStateLine(DGKTBaseModel):
    Points: List[DGKTSPoint] = []
    Values: List[DGKTSStateLineValue] = []


class DGKTSSpencerSlice(DGKTBaseModel):
    LeftForce: float = NAN
    LeftForceY: float = NAN
    LeftForceAngle: float = NAN
    RightForce: float = NAN
    RightForceY: float = NAN
    RightForceAngle: float = NAN
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGKTSPoint = DGKTSPoint()
    BottomRight: DGKTSPoint = DGKTSPoint()
    TopLeft: DGKTSPoint = DGKTSPoint()
    TopRight: DGKTSPoint = DGKTSPoint()
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


class DGKTSUpliftVanSlice(DGKTBaseModel):
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGKTSPoint = DGKTSPoint()
    BottomRight: DGKTSPoint = DGKTSPoint()
    TopLeft: DGKTSPoint = DGKTSPoint()
    TopRight: DGKTSPoint = DGKTSPoint()
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


class DGKTSBishopSlice(DGKTBaseModel):
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGKTSPoint = DGKTSPoint()
    BottomRight: DGKTSPoint = DGKTSPoint()
    TopLeft: DGKTSPoint = DGKTSPoint()
    TopRight: DGKTSPoint = DGKTSPoint()
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


class DGKTSSoilLayerConnection(DGKTBaseModel):
    LayerId: str = ""
    SoilId: str = ""


class DGKTSDitchCharacteristics(DGKTBaseModel):
    DitchEmbankmentSide: float = NAN
    DitchBottomEmbankmentSide: float = NAN
    DitchBottomLandSide: float = NAN
    DitchLandSide: float = NAN


class DGKTSEmbankmentCharacteristics(DGKTBaseModel):
    EmbankmentToeWaterSide: float = NAN
    EmbankmentTopWaterSide: float = NAN
    EmbankmentTopLandSide: float = NAN
    ShoulderBaseLandSide: float = NAN
    EmbankmentToeLandSide: float = NAN


class DGKTSSuTablePoint(DGKTBaseModel):
    EffectiveStress: float = 0.0
    Su: float = 0.0


class DGKTSSuTable(DGKTBaseModel):
    StrengthIncreaseExponent: float = 0.0
    StrengthIncreaseExponentStochasticParameter: DGKTStochasticParameter = (
        DGKTStochasticParameter()
    )
    SuTablePoints: List[DGKTSSuTablePoint] = []
    IsSuTableProbabilistic: bool = False
    SuTableVariationCoefficient: float = 0.0


class DGKTSHeadLine(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTSPoint] = []


class DGKTSReferenceLine(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopHeadLineId: str = ""
    BottomHeadLineId: str = ""
    Points: List[DGKTSPoint] = []


class DGKTSStage(DGKTBaseModel):
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


class DGKTSCalculation(DGKTBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    CalculationSettingsId: str = ""
    ResultId: Optional[str] = ""


class DGKTSExcavation(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTSPoint] = []


class DGKTSElevation(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGKTSPoint] = []
    AddedLayerId: str = ""


class DGKTSTree(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Force: float = 0.0
    RootZoneWidth: float = 5.0
    Spread: float = 0.0
    Location: DGKTSPoint = DGKTSPoint()


#########################
#          A            #
#########################


#########################
#          B            #
#########################
class DGKTFBoundaryConditions(DGKTBaseModelPath):
    path_name: str = "boundaryconditions"
    Id: str = ""
    BoundaryConditions: List[DGKTFBoundaryCondition] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSBishop(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Circle: DGKTSCircle = DGKTSCircle()


class DGKTSBishopBruteForce(DGKTBaseModel):
    SearchGrid: DGKTSSearchGrid = DGKTSSearchGrid()
    TangentLines: DGKTSTangentLines = DGKTSTangentLines()
    GridEnhancements: DGKTSGridEnhancements = DGKTSGridEnhancements()
    SlipPlaneConstraints: DGKTSSlipPlaneConstraintsBishop = (
        DGKTSSlipPlaneConstraintsBishop()
    )


class DGKTSBishopBruteForceResult(DGKTBaseModelPath):
    path_name: str = "results/bishopbruteforce"
    Circle: DGKTSCircle = DGKTSCircle()
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTSPoint] = []
    Slices: List[DGKTSBishopSlice] = []


class DGKTSBishopResult(DGKTBaseModelPath):
    path_name: str = "results/bishop"
    Circle: DGKTSCircle = DGKTSCircle()
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTSPoint] = []
    Slices: List[DGKTSBishopSlice] = []


#########################
#          C            #
#########################
class DGKTSCalculationSettings(DGKTBaseModelPath):
    path_name: str = "calculationsettings"
    Id: str = ""
    AnalysisType: str = ""
    CalculationType: str = "Deterministic"
    ModelFactorMean: float = 1.0
    ModelFactorStandardDeviation: float = 0.0
    Bishop: DGKTSBishop = DGKTSBishop()
    BishopBruteForce: DGKTSBishopBruteForce = DGKTSBishopBruteForce()
    UpliftVan: DGKTSUpliftVan = DGKTSUpliftVan()
    UpliftVanParticleSwarm: DGKTSUpliftVanParticleSwarm = DGKTSUpliftVanParticleSwarm()
    Spencer: DGKTSSpencer = DGKTSSpencer()
    SpencerGenetic: DGKTSSpencerGenetic = DGKTSSpencerGenetic()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          D            #
#########################
class DGKTSDecorations(DGKTBaseModelPath):
    path_name: str = "decorations"
    Id: str = ""
    Excavations: List[DGKTSExcavation] = []
    Elevations: List[DGKTSElevation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          E            #
#########################
class DGKTSEarthquake(DGKTBaseModel):
    IsEnabled: bool = False
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    HorizontalFactor: float = 0.0
    VerticalFactor: float = 0.0
    FreeWaterFactor: float = 0.0
    Consolidations: List[DGKTSConsolidation] = []


#########################
#          F            #
#########################


#########################
#          G            #
#########################
class DGKTFGeometry(DGKTBaseModelPath):
    path_name: str = "geometries"
    Id: str = ""
    Layers: List[DGKTFLayer] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSGeometry(DGKTBaseModelPath):
    path_name: str = "geometries"
    Id: str = ""
    Layers: List[DGKTSLayer] = []
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
class DGKTSLayerLoad(DGKTBaseModel):
    LayerId: str = ""
    Consolidations: List[DGKTSConsolidation] = []


class DGKTSLineLoad(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Location: DGKTSPoint = DGKTSPoint()
    Magnitude: float = 10.0
    Spread: float = 0.0
    Angle: float = 0.0
    Consolidations: List[DGKTSConsolidation] = []


class DGKTSLoads(DGKTBaseModelPath):
    path_name: str = "loads"
    Id: str = ""
    LayerLoads: List[DGKTSLayerLoad] = []
    UniformLoads: List["DGKTSUniformLoad"] = []
    LineLoads: List[DGKTSLineLoad] = []
    Trees: List[DGKTSTree] = []
    Earthquake: DGKTSEarthquake = DGKTSEarthquake()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          M            #
#########################
class DGKTFMeshProperties(DGKTBaseModelPath):
    path_name: str = "meshproperties"
    Id: str = ""
    MeshProperties: List[DGKTFMeshProperty] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          N            #
#########################
class DGKTSNailPropertiesForSoils(DGKTBaseModel):
    NailPropertiesForSoils: List[Dict] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          O            #
#########################


#########################
#          P            #
#########################
class DGKTFProjectInfo(DGKTBaseModel):
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


class DGKTSProjectInfo(DGKTBaseModel):
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


class DGKTSReinforcements(DGKTBaseModelPath):
    path_name: str = "reinforcements"
    Id: str = ""
    ForbiddenLines: List[DGKTSForbiddenLine] = []
    Geotextiles: List[DGKTSGeotextile] = []
    Nails: List[DGKTSNail] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          S            #
#########################
class DGKTFScenarios(DGKTBaseModelPath):
    path_name: str = "scenarios"
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    GeometryId: str = ""
    SoilLayersId: str = ""
    Stages: List[DGKTFStage] = []
    Calculations: List[DGKTFCalculation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTFSoilLayers(DGKTBaseModelPath):
    path_name: str = "soillayers"
    Id: str = ""
    SoilLayers: List[DGKTFSoilLayer] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTFSoils(DGKTBaseModelPath):
    Soils: List[DGKTFSoil] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTFSoilVisualizations(DGKTBaseModel):
    SoilVisualizations: List[DGKTFSoilVisualization] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSScenario(DGKTBaseModelPath):
    path_name: str = "scenarios"
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Stages: List[DGKTSStage] = []
    Calculations: List[DGKTSCalculation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSSoil(DGKTBaseModel):
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
    SuTable: DGKTSSuTable = DGKTSSuTable()


class DGKTSSoils(DGKTBaseModel):
    Soils: List[DGKTSSoil] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSSoilLayers(DGKTBaseModelPath):
    Id: str = ""
    path_name: str = "soillayers"
    SoilLayers: List[DGKTSSoilLayerConnection] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSSoilCorrelations(DGKTBaseModel):
    SoilCorrelations: List[Dict] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSSoilVisualization(DGKTBaseModel):
    SoilId: str = ""
    Color: str = ""
    PersistableShadingType: str = ""


class DGKTSSoilVisualizations(DGKTBaseModel):
    SoilVisualizations: List[DGKTSSoilVisualization] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSSpencerResult(DGKTBaseModelPath):
    path_name: str = "results/spencer"
    SlipPlane: List[DGKTSPoint] = []
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTSPoint] = []
    Slices: List[DGKTSSpencerSlice] = []


class DGKTSSpencerGeneticAlgorithmResult(DGKTBaseModelPath):
    path_name: str = "results/spencergeneticalgorithm"
    SlipPlane: List[DGKTSPoint] = []
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTSPoint] = []
    Slices: List[DGKTSSpencerSlice] = []


class DGKTSStates(DGKTBaseModelPath):
    path_name: str = "states"
    Id: str = ""
    StatePoints: List[DGKTSStatePoint] = []
    StateLines: List[DGKTSStateLine] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGKTSStateCorrelations(DGKTBaseModelPath):
    path_name: str = "statecorrelations"
    Id: str = ""
    StateCorrelations: List[DGKTSStateCorrelation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          T            #
#########################


#########################
#          U            #
#########################


class DGKTSUniformLoad(DGKTBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: float = 0.0
    End: float = 0.0
    Magnitude: float = 0.0
    Spread: float = 0.0
    Consolidations: List[DGKTSConsolidation] = []


class DGKTSUpliftVanResult(DGKTBaseModelPath):
    path_name: str = "results/upliftvan"
    LeftCenter: DGKTSPoint = DGKTSPoint()
    RightCenter: DGKTSPoint = DGKTSPoint()
    TangentLine: float = NAN
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTSPoint] = []
    Slices: List[DGKTSUpliftVanSlice] = []


class DGKTSUpliftVanParticleSwarmResult(DGKTBaseModelPath):
    path_name: str = "results/upliftvanparticleswarm"
    LeftCenter: DGKTSPoint = DGKTSPoint()
    RightCenter: DGKTSPoint = DGKTSPoint()
    TangentLine: float = NAN
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGKTSPoint] = []
    Slices: List[DGKTSUpliftVanSlice] = []


#########################
#          V            #
#########################


#########################
#          W            #
#########################


class DGKTSWaternetCreatorSettings(DGKTBaseModelPath):
    path_name: str = "waternetcreatorsettings"
    Id: str = ""
    EmbankmentCharacteristics: DGKTSEmbankmentCharacteristics = (
        DGKTSEmbankmentCharacteristics()
    )
    DitchCharacteristics: DGKTSDitchCharacteristics = DGKTSDitchCharacteristics()
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
    DrainageConstruction: DGKTSPoint = DGKTSPoint()
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


class DGKTSWaternets(DGKTBaseModelPath):
    path_name: str = "waternets"
    Id: str = ""
    UnitWeightWater: float = 9.81
    PhreaticLineId: Optional[str] = None
    HeadLines: List[DGKTSHeadLine] = []
    ReferenceLines: List[DGKTSReferenceLine] = []
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
