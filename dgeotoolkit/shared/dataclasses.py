from typing import List, Optional, Union, Dict
import inspect
import sys

from ..const import NAN, CURRENT_CONTENT_VERSION, DGEOFLOW_VERSION
from ..models.basemodel import DGTKBaseModel, DGTKBaseModelPath


####################
# NEED TO GO FIRST #
####################


##########
# SHARED #
##########
class DGTKPoint(DGTKBaseModel):
    X: float = NAN
    Z: float = NAN


############
# DGEOFLOW #
############


class DGTKFSoil(DGTKBaseModel):
    Id: str = ""
    Name: Optional[str] = ""
    Code: str = ""
    Notes: Optional[str] = ""
    HorizontalPermeability: float = NAN
    VerticalPermeability: float = NAN


class DGTKFSoilVisualization(DGTKBaseModel):
    SoilId: str = ""
    Color: str = ""
    PersistableShadingType: str = ""


class DGTKFFixedHeadBoundaryConditionProperties(DGTKBaseModel):
    HeadLevel: float = NAN


class DGTKFBoundaryCondition(DGTKBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGTKPoint] = []
    FixedHeadBoundaryConditionProperties: DGTKFFixedHeadBoundaryConditionProperties = (
        DGTKFFixedHeadBoundaryConditionProperties()
    )


class DGTKFMeshProperty(DGTKBaseModel):
    LayerId: str = ""
    Label: str = ""
    ElementSize: float = NAN


class DGTKFStage(DGTKBaseModel):
    Id: str = ""
    Label: str = ""
    Notes: Optional[str] = ""
    BoundaryConditionCollectionId: str = ""


class DGTKFPipeTrajectory(DGTKBaseModel):
    Label: str = ""
    Notes: Optional[str] = ""
    D70: float = NAN
    ElementSize: float = NAN
    ErosionDirection: str = ""
    Points: List[DGTKPoint] = []


class DGTKFCriticalHeadSearchSpace(DGTKBaseModel):
    MinimumHeadLevel: float = NAN
    MaximumHeadLevel: float = NAN
    StepSize: float = NAN


class DGTKFSoilLayer(DGTKBaseModel):
    LayerId: str = ""
    SoilId: str = ""


class DGTKFCalculation(DGTKBaseModel):
    Label: str = ""
    Notes: Optional[str] = ""
    CalculationType: str = ""
    PipeTrajectory: DGTKFPipeTrajectory = None
    CriticalHeadId: Optional[str] = None
    CriticalHeadSearchSpace: DGTKFCriticalHeadSearchSpace = (
        DGTKFCriticalHeadSearchSpace()
    )
    MeshPropertiesId: str = ""
    ResultsId: Optional[str] = None


class DGTKFNodes(DGTKBaseModel):
    Nodes: List[DGTKPoint] = []
    IsActive: bool = False
    Height: float = NAN


class DGTKFNodeResult(DGTKBaseModel):
    Point: DGTKPoint = DGTKPoint()
    TotalPorePressure: float = NAN
    HydraulicDischarge: float = NAN
    HydraulicHead: float = NAN


class DGTKFElement(DGTKBaseModel):
    NodeResults: List[DGTKFNodeResult] = []


##############
# DSTABILITY #
##############
class DGTKSCircle(DGTKBaseModel):
    Center: DGTKPoint = DGTKPoint()
    Radius: float = NAN


class DGTKSConsolidation(DGTKBaseModel):
    LayerId: str = ""
    Degree: float = 0


class DGTKSGridEnhancements(DGTKBaseModel):
    ExtrapolateSearchSpace: bool = True


class DGTKLayer(DGTKBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGTKPoint] = []


class DGTKSLayer(DGTKLayer):
    pass


class DGTKFLayer(DGTKLayer):
    pass


class DGTKSSearchGrid(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    BottomLeft: Optional[DGTKPoint] = None
    Space: float = 1.0
    NumberOfPointsInX: int = 1
    NumberOfPointsInZ: int = 1


class DGTKSTangentLines(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    BottomTangentLineZ: float = NAN
    Space: float = 0.5
    NumberOfTangentLines: int = 1


class DGTKSSlipPlaneConstraintsBishop(DGTKBaseModel):
    IsSizeConstraintsEnabled: bool = False
    MinimumSlipPlaneDepth: float = 0.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class DGTKSSlipPlaneUpliftVan(DGTKBaseModel):
    FirstCircleCenter: DGTKPoint = DGTKPoint()
    FirstCircleRadius: float = NAN
    SecondCircleCenter: DGTKPoint = DGTKPoint()


class DGTKSUpliftVan(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlane: DGTKSSlipPlaneUpliftVan = DGTKSSlipPlaneUpliftVan()


class DGTKSSearchArea(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopLeft: Optional[DGTKPoint] = None
    Width: float = 0.0
    Height: float = 0.0


class DGTKSTangentArea(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopZ: Optional[float] = None
    Height: float = 0.0


class DGTKSSlipPlaneConstraintsUpliftVanParticleSwarm(DGTKBaseModel):
    IsSizeConstraintsEnabled: bool = False
    MinimumSlipPlaneDepth: float = 0.0
    MinimumSlipPlaneLength: float = 0.0
    IsZoneAConstraintsEnabled: bool = False
    XLeftZoneA: float = 0.0
    WidthZoneA: float = 0.0
    IsZoneBConstraintsEnabled: bool = False
    XLeftZoneB: float = 0.0
    WidthZoneB: float = 0.0


class DGTKSUpliftVanParticleSwarm(DGTKBaseModel):
    SearchAreaA: DGTKSSearchArea = DGTKSSearchArea()
    SearchAreaB: DGTKSSearchArea = DGTKSSearchArea()
    TangentArea: DGTKSTangentArea = DGTKSTangentArea()
    SlipPlaneConstraints: DGTKSSlipPlaneConstraintsUpliftVanParticleSwarm = (
        DGTKSSlipPlaneConstraintsUpliftVanParticleSwarm()
    )
    OptionsType: str = "Default"


class DGTKSSlipPlaneConstraintsSpencer(DGTKBaseModel):
    IsEnabled: bool = False
    MinimumAngleBetweenSlices: float = 120.0
    MinimumThrustLinePercentageInsideSlices: float = 80.0


class DGTKSSpencer(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlane: Optional[List[DGTKPoint]] = None
    SlipPlaneConstraints: DGTKSSlipPlaneConstraintsSpencer = (
        DGTKSSlipPlaneConstraintsSpencer()
    )


class DGTKSSpencerGenetic(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    SlipPlaneA: Optional[List[DGTKPoint]] = None
    SlipPlaneB: Optional[List[DGTKPoint]] = None
    SlipPlaneConstraints: DGTKSSlipPlaneConstraintsSpencer = (
        DGTKSSlipPlaneConstraintsSpencer()
    )
    OptionsType: str = "Default"


class DGTKSForbiddenLine(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: DGTKPoint = DGTKPoint()
    End: DGTKPoint = DGTKPoint()


class DGTKSGeotextile(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: DGTKPoint = DGTKPoint()
    End: DGTKPoint = DGTKPoint()
    TensileStrength: float = 0.0
    ReductionArea: float = 0.0


class DGTKSStress(DGTKBaseModel):
    Distance: float = 0.0
    Stress: float = 0.0


class DGTKSNail(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Location: DGTKPoint = DGTKPoint()
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
    LateralStresses: List[DGTKSStress] = []
    ShearStresses: List[DGTKSStress] = []


class DGTKStochasticParameter(DGTKBaseModel):
    IsProbabilistic: bool = False
    Mean: float = 1.0
    StandardDeviation: float = 0.0


class DGTKSStateStress(DGTKBaseModel):
    StateType: str = ""
    Pop: float = 0.0
    PopStochasticParameter: DGTKStochasticParameter = DGTKStochasticParameter()
    Ocr: float = 1.0
    YieldStress: float = 0.0


class DGTKSStateCorrelation(DGTKBaseModel):
    pass  # TODO


class DGTKSStatePoint(DGTKBaseModel):
    Id: str = ""
    LayerId: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    IsProbabilistic: bool = True
    Point: DGTKPoint = DGTKPoint()
    Stress: DGTKSStateStress = DGTKSStateStress()


class DGTKSStateLineValue(DGTKBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    X: float = NAN
    IsProbabilistic: bool = True
    IsAboveAndBelowCorrelated: bool = True
    Above: DGTKSStateStress = DGTKSStateStress()
    Below: DGTKSStateStress = DGTKSStateStress()


class DGTKSStateLine(DGTKBaseModel):
    Points: List[DGTKPoint] = []
    Values: List[DGTKSStateLineValue] = []


class DGTKSSpencerSlice(DGTKBaseModel):
    LeftForce: float = NAN
    LeftForceY: float = NAN
    LeftForceAngle: float = NAN
    RightForce: float = NAN
    RightForceY: float = NAN
    RightForceAngle: float = NAN
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGTKPoint = DGTKPoint()
    BottomRight: DGTKPoint = DGTKPoint()
    TopLeft: DGTKPoint = DGTKPoint()
    TopRight: DGTKPoint = DGTKPoint()
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


class DGTKSUpliftVanSlice(DGTKBaseModel):
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGTKPoint = DGTKPoint()
    BottomRight: DGTKPoint = DGTKPoint()
    TopLeft: DGTKPoint = DGTKPoint()
    TopRight: DGTKPoint = DGTKPoint()
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


class DGTKSBishopSlice(DGTKBaseModel):
    ArcLength: float = NAN
    BottomAngle: float = NAN
    BottomLeft: DGTKPoint = DGTKPoint()
    BottomRight: DGTKPoint = DGTKPoint()
    TopLeft: DGTKPoint = DGTKPoint()
    TopRight: DGTKPoint = DGTKPoint()
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


class DGTKSoilLayer(DGTKBaseModel):
    LayerId: str = ""
    SoilId: str = ""


class DGTKSDitchCharacteristics(DGTKBaseModel):
    DitchEmbankmentSide: float = NAN
    DitchBottomEmbankmentSide: float = NAN
    DitchBottomLandSide: float = NAN
    DitchLandSide: float = NAN


class DGTKSEmbankmentCharacteristics(DGTKBaseModel):
    EmbankmentToeWaterSide: float = NAN
    EmbankmentTopWaterSide: float = NAN
    EmbankmentTopLandSide: float = NAN
    ShoulderBaseLandSide: float = NAN
    EmbankmentToeLandSide: float = NAN


class DGTKSSuTablePoint(DGTKBaseModel):
    EffectiveStress: float = 0.0
    Su: float = 0.0


class DGTKSSuTable(DGTKBaseModel):
    StrengthIncreaseExponent: float = 1.0
    StrengthIncreaseExponentStochasticParameter: DGTKStochasticParameter = (
        DGTKStochasticParameter(Mean=0.8)
    )
    SuTablePoints: List[DGTKSSuTablePoint] = []
    IsSuTableProbabilistic: bool = False
    SuTableVariationCoefficient: float = 0.0


class DGTKSHeadLine(DGTKBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGTKPoint] = []


class DGTKSReferenceLine(DGTKBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    TopHeadLineId: str = ""
    BottomHeadLineId: str = ""
    Points: List[DGTKPoint] = []


class DGTKSStage(DGTKBaseModel):
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


class DGTKSCalculation(DGTKBaseModel):
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    CalculationSettingsId: str = ""
    ResultId: Optional[str] = ""


class DGTKSExcavation(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGTKPoint] = []


class DGTKSElevation(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Points: List[DGTKPoint] = []
    AddedLayerId: str = ""


class DGTKSTree(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Force: float = 0.0
    RootZoneWidth: float = 5.0
    Spread: float = 0.0
    Location: DGTKPoint = DGTKPoint()


#########################
#          A            #
#########################


#########################
#          B            #
#########################
class DGTKFBoundaryConditions(DGTKBaseModelPath):
    path_name: str = "boundaryconditions"
    Id: str = ""
    BoundaryConditions: List[DGTKFBoundaryCondition] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSBishop(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Circle: DGTKSCircle = DGTKSCircle()


class DGTKSBishopBruteForce(DGTKBaseModel):
    SearchGrid: DGTKSSearchGrid = DGTKSSearchGrid()
    TangentLines: DGTKSTangentLines = DGTKSTangentLines()
    GridEnhancements: DGTKSGridEnhancements = DGTKSGridEnhancements()
    SlipPlaneConstraints: DGTKSSlipPlaneConstraintsBishop = (
        DGTKSSlipPlaneConstraintsBishop()
    )


class DGTKSBishopBruteForceResult(DGTKBaseModelPath):
    path_name: str = "results/bishopbruteforce"
    Circle: DGTKSCircle = DGTKSCircle()
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGTKPoint] = []
    Slices: List[DGTKSBishopSlice] = []


class DGTKSBishopResult(DGTKBaseModelPath):
    path_name: str = "results/bishop"
    Circle: DGTKSCircle = DGTKSCircle()
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGTKPoint] = []
    Slices: List[DGTKSBishopSlice] = []


#########################
#          C            #
#########################
class DGTKSCalculationSettings(DGTKBaseModelPath):
    path_name: str = "calculationsettings"
    Id: str = ""
    AnalysisType: str = "BishopBruteForce"
    CalculationType: str = "Deterministic"
    ModelFactorMean: float = 1.0
    ModelFactorStandardDeviation: float = 0.0
    Bishop: DGTKSBishop = DGTKSBishop()
    BishopBruteForce: DGTKSBishopBruteForce = DGTKSBishopBruteForce()
    UpliftVan: DGTKSUpliftVan = DGTKSUpliftVan()
    UpliftVanParticleSwarm: DGTKSUpliftVanParticleSwarm = DGTKSUpliftVanParticleSwarm()
    Spencer: DGTKSSpencer = DGTKSSpencer()
    SpencerGenetic: DGTKSSpencerGenetic = DGTKSSpencerGenetic()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          D            #
#########################
class DGTKSDecorations(DGTKBaseModelPath):
    path_name: str = "decorations"
    Id: str = ""
    Excavations: List[DGTKSExcavation] = []
    Elevations: List[DGTKSElevation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          E            #
#########################
class DGTKSEarthquake(DGTKBaseModel):
    IsEnabled: bool = False
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    HorizontalFactor: float = 0.0
    VerticalFactor: float = 0.0
    FreeWaterFactor: float = 0.0
    Consolidations: List[DGTKSConsolidation] = []


#########################
#          F            #
#########################


#########################
#          G            #
#########################
class DGTKGeometry(DGTKBaseModelPath):
    path_name: str = "geometries"
    Id: str = ""
    Layers: List[DGTKLayer] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSGeometry(DGTKGeometry):
    pass


class DGTKFGeometry(DGTKGeometry):
    pass


class DGTKFGroundWaterFlowResult(DGTKBaseModel):
    Id: str = ""
    Elements: List[DGTKFElement] = []
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
class DGTKSLayerLoad(DGTKBaseModel):
    LayerId: str = ""
    Consolidations: List[DGTKSConsolidation] = []


class DGTKSLineLoad(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Location: DGTKPoint = DGTKPoint()
    Magnitude: float = 10.0
    Spread: float = 0.0
    Angle: float = 0.0
    Consolidations: List[DGTKSConsolidation] = []


class DGTKSLoads(DGTKBaseModelPath):
    path_name: str = "loads"
    Id: str = ""
    LayerLoads: List[DGTKSLayerLoad] = []
    UniformLoads: List["DGTKSUniformLoad"] = []
    LineLoads: List[DGTKSLineLoad] = []
    Trees: List[DGTKSTree] = []
    Earthquake: DGTKSEarthquake = DGTKSEarthquake()
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          M            #
#########################
class DGTKFMeshProperties(DGTKBaseModelPath):
    path_name: str = "meshproperties"
    Id: str = ""
    MeshProperties: List[DGTKFMeshProperty] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          N            #
#########################
class DGTKSNailPropertyForSoils(DGTKBaseModel):
    SoilId: str = ""
    CompressionRatio: float = 1.0
    RheologicalCoefficient: float = 0.0
    AreBondStressesActive: bool = False
    BondStresses: List[float] = []  # TODO wat is dit voor lijst?


class DGTKSNailPropertiesForSoils(DGTKBaseModel):
    NailPropertiesForSoils: List[DGTKSNailPropertyForSoils] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          O            #
#########################


#########################
#          P            #
#########################
class DGTKFPipeLengthResult(DGTKBaseModel):
    PipeElements: List[DGTKFNodes] = []
    PipeLength: float = NAN
    Id: str = ""
    Elements: List[DGTKFElement] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKFProjectInfo(DGTKBaseModel):
    Path: str = ""
    Project: str = ""
    CrossSection: str = ""
    Remarks: str = ""
    Analyst: str = ""
    LastModifier: str = ""
    Date: Optional[str] = ""
    LastModified: str = ""
    Created: str = ""
    ApplicationCreated: str = DGEOFLOW_VERSION
    ApplicationModified: str = DGEOFLOW_VERSION
    IsDataValidated: bool = True
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSProjectInfo(DGTKBaseModel):
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


class DGTKSReinforcements(DGTKBaseModelPath):
    path_name: str = "reinforcements"
    Id: str = ""
    ForbiddenLines: List[DGTKSForbiddenLine] = []
    Geotextiles: List[DGTKSGeotextile] = []
    Nails: List[DGTKSNail] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          S            #
#########################
class DGTKFScenarios(DGTKBaseModelPath):
    path_name: str = "scenarios"
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    GeometryId: str = ""
    SoilLayersId: str = ""
    Stages: List[DGTKFStage] = []
    Calculations: List[DGTKFCalculation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKFScenario(DGTKBaseModelPath):
    path_name: str = "scenarios"
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    GeometryId: str = ""
    SoilLayersId: str = ""
    Stages: List[DGTKFStage] = []
    Calculations: List[DGTKFCalculation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKFSoilVisualizations(DGTKBaseModel):
    SoilVisualizations: List[DGTKFSoilVisualization] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSScenario(DGTKBaseModelPath):
    path_name: str = "scenarios"
    Id: str = ""
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Stages: List[DGTKSStage] = []
    Calculations: List[DGTKSCalculation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSMohrCoulombClassicShearStrengthModel(DGTKBaseModel):
    Cohesion: float = NAN
    CohesionStochasticParameter: DGTKStochasticParameter = DGTKStochasticParameter()
    FrictionAngle: float = NAN
    FrictionAngleStochasticParameter: DGTKStochasticParameter = (
        DGTKStochasticParameter()
    )
    CohesionAndFrictionAngleCorrelated: bool = False


class DGTKSMohrCoulombAdvancedShearStrengthModel(DGTKBaseModel):
    Cohesion: float = NAN
    CohesionStochasticParameter: DGTKStochasticParameter = DGTKStochasticParameter()
    FrictionAngle: float = NAN
    FrictionAngleStochasticParameter: DGTKStochasticParameter = (
        DGTKStochasticParameter()
    )
    CohesionAndFrictionAngleCorrelated: bool = False
    Dilatancy: float = NAN
    DilatancyStochasticParameter: DGTKStochasticParameter = DGTKStochasticParameter()


class DGTKSSuShearStrengthModel(DGTKBaseModel):
    ShearStrengthRatio: float = NAN
    ShearStrengthRatioStochasticParameter: DGTKStochasticParameter = (
        DGTKStochasticParameter()
    )
    StrengthIncreaseExponent: float = NAN
    StrengthIncreaseExponentStochasticParameter: DGTKStochasticParameter = (
        DGTKStochasticParameter()
    )
    ShearStrengthRatioAndShearStrengthExponentCorrelated: bool = False


class DGTKSSoil(DGTKBaseModel):
    Id: str = ""
    Name: str = ""
    Notes: Optional[str] = ""
    Code: str = ""
    IsProbabilistic: bool = False
    VolumetricWeightAbovePhreaticLevel: float = 0.0
    VolumetricWeightBelowPhreaticLevel: float = 0.0
    ShearStrengthModelTypeAbovePhreaticLevel: str = ""
    ShearStrengthModelTypeBelowPhreaticLevel: str = ""

    MohrCoulombClassicShearStrengthModel: DGTKSMohrCoulombClassicShearStrengthModel = (
        DGTKSMohrCoulombClassicShearStrengthModel()
    )

    MohrCoulombAdvancedShearStrengthModel: DGTKSMohrCoulombAdvancedShearStrengthModel = (
        DGTKSMohrCoulombAdvancedShearStrengthModel()
    )

    SuShearStrengthModel: DGTKSSuShearStrengthModel = DGTKSSuShearStrengthModel()
    SuTable: DGTKSSuTable = DGTKSSuTable()


class DGTKSoils(DGTKBaseModel):
    Soils: List[Union[DGTKSSoil, DGTKFSoil]] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKFSoils(DGTKBaseModelPath):
    Soils: List[DGTKFSoil] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSSoils(DGTKBaseModelPath):
    Soils: List[DGTKSSoil] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSoilLayers(DGTKBaseModelPath):
    Id: str = ""
    path_name: str = "soillayers"
    SoilLayers: List[DGTKSoilLayer] = []
    Soils: DGTKSoils = DGTKSoils()
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSSoilLayers(DGTKSoilLayers):
    pass


class DGTKFSoilLayers(DGTKSoilLayers):
    pass


class DGTKSSoilCorrelations(DGTKBaseModel):
    SoilCorrelations: List[Dict] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSSoilVisualization(DGTKBaseModel):
    SoilId: str = ""
    Color: str = ""
    PersistableShadingType: str = ""


class DGTKSSoilVisualizations(DGTKBaseModel):
    SoilVisualizations: List[DGTKSSoilVisualization] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSSpencerResult(DGTKBaseModelPath):
    path_name: str = "results/spencer"
    SlipPlane: List[DGTKPoint] = []
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGTKPoint] = []
    Slices: List[DGTKSSpencerSlice] = []


class DGTKSSpencerGeneticAlgorithmResult(DGTKBaseModelPath):
    path_name: str = "results/spencergeneticalgorithm"
    SlipPlane: List[DGTKPoint] = []
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGTKPoint] = []
    Slices: List[DGTKSSpencerSlice] = []


class DGTKSStates(DGTKBaseModelPath):
    path_name: str = "states"
    Id: str = ""
    StatePoints: List[DGTKSStatePoint] = []
    StateLines: List[DGTKSStateLine] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


class DGTKSStateCorrelations(DGTKBaseModelPath):
    path_name: str = "statecorrelations"
    Id: str = ""
    StateCorrelations: List[DGTKSStateCorrelation] = []
    ContentVersion: str = CURRENT_CONTENT_VERSION


#########################
#          T            #
#########################


#########################
#          U            #
#########################


class DGTKSUniformLoad(DGTKBaseModel):
    Label: Optional[str] = ""
    Notes: Optional[str] = ""
    Start: float = 0.0
    End: float = 0.0
    Magnitude: float = 0.0
    Spread: float = 0.0
    Consolidations: List[DGTKSConsolidation] = []


class DGTKSUpliftVanResult(DGTKBaseModelPath):
    path_name: str = "results/upliftvan"
    LeftCenter: DGTKPoint = DGTKPoint()
    RightCenter: DGTKPoint = DGTKPoint()
    TangentLine: float = NAN
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGTKPoint] = []
    Slices: List[DGTKSUpliftVanSlice] = []


class DGTKSUpliftVanParticleSwarmResult(DGTKBaseModelPath):
    path_name: str = "results/upliftvanparticleswarm"
    LeftCenter: DGTKPoint = DGTKPoint()
    RightCenter: DGTKPoint = DGTKPoint()
    TangentLine: float = NAN
    Id: str = ""
    FactorOfSafety: float = 0.0
    Points: List[DGTKPoint] = []
    Slices: List[DGTKSUpliftVanSlice] = []


#########################
#          V            #
#########################


#########################
#          W            #
#########################


class DGTKSWaternetCreatorSettings(DGTKBaseModelPath):
    path_name: str = "waternetcreatorsettings"
    Id: str = ""
    EmbankmentCharacteristics: DGTKSEmbankmentCharacteristics = (
        DGTKSEmbankmentCharacteristics()
    )
    DitchCharacteristics: DGTKSDitchCharacteristics = DGTKSDitchCharacteristics()
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
    DrainageConstruction: DGTKPoint = DGTKPoint()
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


class DGTKSWaternets(DGTKBaseModelPath):
    path_name: str = "waternets"
    Id: str = ""
    UnitWeightWater: float = 9.81
    PhreaticLineId: Optional[str] = None
    HeadLines: List[DGTKSHeadLine] = []
    ReferenceLines: List[DGTKSReferenceLine] = []
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
