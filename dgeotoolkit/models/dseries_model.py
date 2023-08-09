from pydantic import BaseModel
from typing import List, Tuple
from shapely.geometry import Polygon

from ..shared.dataclasses import (
    DGTKGeometry,
    DGTKSoilLayers,
    DGTKLayer,
    DGTKPoint,
    DGTKSoilLayer,
)


class ShapelyGeometry:
    def __init__(
        self,
        points: List[Tuple[float, float]],
        soil_id: str,
        label: str = "",
    ):
        self.polygon = Polygon(points)
        self.soil_id = soil_id
        self.label = label


class DGTKDSeriesModel(BaseModel):
    current_id: int = 0

    Geometry: List[DGTKGeometry] = []
    SoilLayers: List[DGTKSoilLayers] = []

    def next_id(self) -> int:
        """Generate the next id based on the current model"""
        self.current_id += 1
        return str(self.current_id)

    def set_current_scenario(self, index: int = 0):
        if index >= len(self.Scenario):
            raise ValueError(
                f"Trying to set the current scenario to '{index}' but we only have '{len(self.Scenario)}' scenario(s)"
            )
        self._current_scenario_id = index

    def set_current_stage(self, index: int = 0):
        if index >= len(self.Scenario[self._current_scenario_id].Stages):
            raise ValueError(
                f"Trying to set the current state to '{index}' but scenario {self._current_scenario_id} only has '{len(self.Scenario[self._current_scenario_id].Stages)}' stage(s)"
            )
        self._current_scenario_id = index

    def _get_current_scenario(self):
        for s in self.Scenario:
            if s.Id == self._current_scenario_id:
                return s

        raise ValueError(
            f"No scenario with id '{self._current_scenario_id}' in this datastructure"
        )

    def _get_current_stage(self):
        scenario = self._get_current_scenario()
        for s in scenario.Stages:
            if s.Id == self._current_stage_id:
                return s

        raise ValueError(
            f"No stage with id '{self._get_current_stage}' in this datastructure"
        )

    def _get_geometry_by_id(self, id: str):
        for g in self.Geometry:
            if g.Id == id:
                return g

        raise ValueError(f"No geometry with id '{id}' in this datastructure")

    def _get_geometry(self):
        stage = self._get_current_stage()
        return self._get_geometry_by_id(stage.GeometryId)

    def _set_geometry(self, geometry: DGTKGeometry):
        for i, g in enumerate(self.Geometry):
            if g.Id == geometry.Id:
                self.Geometry[i] = geometry
                return

        raise ValueError(
            f"Could not set geometry because the given id '{geometry.Id}' does not correspond with a geometry id in the datastructure"
        )

    def _get_soillayers_by_id(self, id: str) -> SoilLayers:
        for s in self.SoilLayers:
            if s.Id == id:
                return s

        raise ValueError(f"No soillayers with id '{id}' in this datastructure")

    def _get_soillayers(self) -> SoilLayers:
        stage = self._get_current_stage()
        return self._get_soillayers_by_id(stage.SoilLayersId)

    def _set_soillayers(self, soillayers: DGTKSoilLayers):
        for i, s in enumerate(self.SoilLayers):
            if s.Id == soillayers.Id:
                self.SoilLayers[i] = s
                return

        raise ValueError(
            f"Could not set soillayers because the given id '{soillayers.Id}' does not correspond with a geometry id in the datastructure"
        )

    def add_layer(self, points: List[Tuple[float, float]], soil_id: str):
        polygons = self.to_shapely()

        if len(polygons) == 0:  # first layer, easy peasy
            polygons.append(ShapelyGeometry(points=points, soil_id=soil_id))
            self.to_geometry(polygons)
            return

        # check if the new layer touches existing layers

    def to_shapely(self) -> List[ShapelyGeometry]:
        """Convert the current geometry to a set of polygons with soil ids"""
        geometry = self._get_geometry()
        soillayers = self._get_soillayers()

        polygons = []
        for l in geometry.Layers:
            for s in soillayers.SoilLayers:
                if s.LayerId == l.Id:
                    soil_id = s.SoilId
            polygons.append(
                ShapelyGeometry(points=[(p.X, p.Z) for p in l.Points], soil_id=soil_id)
            )

        return polygons

    def to_geometry(self, polygons):
        """Convert the polygons to the current geometry"""
        geometry = self._get_geometry()
        geometry.Layers = []

        soillayers = self._get_soillayers()

        for geom in polygons:
            xx, zz = geom.polygon.exterior.coords.xy
            layer_id = self.next_id()
            # note that shapely polygons are closed but dstab polygon are not
            geometry.Layers.append(
                DGTKLayer(
                    Id=layer_id,
                    Label=geom.label,
                    Points=[DGTKPoint(X=p[0], Z=p[1]) for p in zip(xx, zz)][:-1],
                )
            )
            soillayers.SoilLayers.append(
                DGTKSoilLayer(LayerId=layer_id, SoilId=geom.soil_id)
            )

        # TODO > wat als er een load is, moet dan ook de cons ingesteld worden?
        # TODO > idem voor andere afhankelijkheden

        self._set_geometry(geometry)
        self._set_soillayers(soillayers)
