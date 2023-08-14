from pydantic import BaseModel
from typing import List, Tuple
from shapely.geometry import Polygon
from shapely.ops import unary_union

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
        layer_id: str = "",
        label: str = "",
    ):
        self.polygon = Polygon(points)
        self.soil_id = soil_id
        self.layer_id = layer_id
        self.label = label


class DGTKDSeriesModel(BaseModel):
    current_id: int = 0

    Geometry: List[DGTKGeometry] = []
    SoilLayers: List[DGTKSoilLayers] = []

    def _update_relations(self, old_layer_ids: List[str]) -> None:
        pass

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

    def to_one_polygon(self):
        polygons = self.to_shapely()
        return unary_union([p.polygon for p in polygons])

    def add_layer(self, points: List[Tuple[float, float]], soil_id: str):
        polygons = self.to_shapely()

        if len(polygons) == 0:  # first layer, easy peasy
            polygons.append(ShapelyGeometry(points=points, soil_id=soil_id))
            self.to_geometry(polygons)
            return

        # multiple layers, check if the new layer touches existing layers
        new_poly = Polygon(points)
        # first create a overlapping polygon from all polygons
        all_poly = self.to_one_polygon()
        # see if it touches at least at one point
        if not new_poly.intersects(all_poly):
            raise ValueError(
                "Trying to add a layer that not touches any of the other layers."
            )

        polygons.append(ShapelyGeometry(points=points, soil_id=soil_id))
        self.to_geometry(polygons)

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
                ShapelyGeometry(
                    points=[(p.X, p.Z) for p in l.Points],
                    soil_id=soil_id,
                    layer_id=l.Id,
                )
            )

        return polygons

    def to_geometry(self, polygons):
        """Convert the polygons to the current geometry"""
        geometry = self._get_geometry()
        soillayers = self._get_soillayers()
        existing_layer_ids = [l.Id for l in geometry.Layers]

        geometry.Layers = []
        soillayers.SoilLayers.clear()

        for geom in polygons:
            xx, zz = geom.polygon.exterior.coords.xy
            layer_id = self.next_id()
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

        # Make sure to do other housekeeping from the child class
        self._set_geometry(geometry)
        self._set_soillayers(soillayers)
        # call the child function to update relationships that
        # are not handled in this class
        self._update_relations(existing_layer_ids)
