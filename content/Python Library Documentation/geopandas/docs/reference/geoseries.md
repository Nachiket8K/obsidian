---
title: "GeoSeries"
source: "https://geopandas.org/en/latest/docs/reference/geoseries.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# GeoSeries

## Constructor

|  |  |
| --- | --- |
| [`GeoSeries`](api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries")([data, index, crs]) | A Series object designed to store shapely geometry objects. |

## General methods and attributes

|  |  |
| --- | --- |
| [`GeoSeries.area`](api/geopandas.GeoSeries.area.html#geopandas.GeoSeries.area "geopandas.GeoSeries.area") | Return a `Series` containing the area of each geometry in the `GeoSeries` expressed in the units of the CRS. |
| [`GeoSeries.boundary`](api/geopandas.GeoSeries.boundary.html#geopandas.GeoSeries.boundary "geopandas.GeoSeries.boundary") | Return a `GeoSeries` of lower dimensional objects representing each geometry's set-theoretic boundary. |
| [`GeoSeries.bounds`](api/geopandas.GeoSeries.bounds.html#geopandas.GeoSeries.bounds "geopandas.GeoSeries.bounds") | Return a `DataFrame` with columns `minx`, `miny`, `maxx`, `maxy` values containing the bounds for each geometry. |
| [`GeoSeries.total_bounds`](api/geopandas.GeoSeries.total_bounds.html#geopandas.GeoSeries.total_bounds "geopandas.GeoSeries.total_bounds") | Return a tuple containing `minx`, `miny`, `maxx`, `maxy` values for the bounds of the series as a whole. |
| [`GeoSeries.length`](api/geopandas.GeoSeries.length.html#geopandas.GeoSeries.length "geopandas.GeoSeries.length") | Return a `Series` containing the length of each geometry expressed in the units of the CRS. |
| [`GeoSeries.geom_type`](api/geopandas.GeoSeries.geom_type.html#geopandas.GeoSeries.geom_type "geopandas.GeoSeries.geom_type") | Returns a `Series` of strings specifying the Geometry Type of each object. |
| [`GeoSeries.offset_curve`](api/geopandas.GeoSeries.offset_curve.html#geopandas.GeoSeries.offset_curve "geopandas.GeoSeries.offset_curve")(distance[, ...]) | Return a `LineString` or `MultiLineString` geometry at a distance from the object on its right or its left side. |
| [`GeoSeries.distance`](api/geopandas.GeoSeries.distance.html#geopandas.GeoSeries.distance "geopandas.GeoSeries.distance")(other[, align]) | Return a `Series` containing the distance to aligned other. |
| [`GeoSeries.hausdorff_distance`](api/geopandas.GeoSeries.hausdorff_distance.html#geopandas.GeoSeries.hausdorff_distance "geopandas.GeoSeries.hausdorff_distance")(other[, align, ...]) | Return a `Series` containing the Hausdorff distance to aligned other. |
| [`GeoSeries.frechet_distance`](api/geopandas.GeoSeries.frechet_distance.html#geopandas.GeoSeries.frechet_distance "geopandas.GeoSeries.frechet_distance")(other[, align, ...]) | Return a `Series` containing the Frechet distance to aligned other. |
| [`GeoSeries.representative_point`](api/geopandas.GeoSeries.representative_point.html#geopandas.GeoSeries.representative_point "geopandas.GeoSeries.representative_point")() | Return a `GeoSeries` of (cheaply computed) points that are guaranteed to be within each geometry. |
| [`GeoSeries.exterior`](api/geopandas.GeoSeries.exterior.html#geopandas.GeoSeries.exterior "geopandas.GeoSeries.exterior") | Return a `GeoSeries` of LinearRings representing the outer boundary of each polygon in the GeoSeries. |
| [`GeoSeries.interiors`](api/geopandas.GeoSeries.interiors.html#geopandas.GeoSeries.interiors "geopandas.GeoSeries.interiors") | Return a `Series` of List representing the inner rings of each polygon in the GeoSeries. |
| [`GeoSeries.minimum_bounding_radius`](api/geopandas.GeoSeries.minimum_bounding_radius.html#geopandas.GeoSeries.minimum_bounding_radius "geopandas.GeoSeries.minimum_bounding_radius")() | Return a Series of the radii of the minimum bounding circles that enclose each geometry. |
| [`GeoSeries.minimum_clearance`](api/geopandas.GeoSeries.minimum_clearance.html#geopandas.GeoSeries.minimum_clearance "geopandas.GeoSeries.minimum_clearance")() | Return a `Series` containing the minimum clearance distance, which is the smallest distance by which a vertex of the geometry could be moved to produce an invalid geometry. |
| [`GeoSeries.x`](api/geopandas.GeoSeries.x.html#geopandas.GeoSeries.x "geopandas.GeoSeries.x") | Return the x location of point geometries in a GeoSeries. |
| [`GeoSeries.y`](api/geopandas.GeoSeries.y.html#geopandas.GeoSeries.y "geopandas.GeoSeries.y") | Return the y location of point geometries in a GeoSeries. |
| [`GeoSeries.z`](api/geopandas.GeoSeries.z.html#geopandas.GeoSeries.z "geopandas.GeoSeries.z") | Return the z location of point geometries in a GeoSeries. |
| [`GeoSeries.m`](api/geopandas.GeoSeries.m.html#geopandas.GeoSeries.m "geopandas.GeoSeries.m") | Return the m coordinate of point geometries in a GeoSeries. |
| [`GeoSeries.get_coordinates`](api/geopandas.GeoSeries.get_coordinates.html#geopandas.GeoSeries.get_coordinates "geopandas.GeoSeries.get_coordinates")([include\_z, ...]) | Get coordinates from a [`GeoSeries`](api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") as a [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.3)") of floats. |
| [`GeoSeries.count_coordinates`](api/geopandas.GeoSeries.count_coordinates.html#geopandas.GeoSeries.count_coordinates "geopandas.GeoSeries.count_coordinates")() | Return a `Series` containing the count of the number of coordinate pairs in each geometry. |
| [`GeoSeries.count_geometries`](api/geopandas.GeoSeries.count_geometries.html#geopandas.GeoSeries.count_geometries "geopandas.GeoSeries.count_geometries")() | Return a `Series` containing the count of geometries in each multi-part geometry. |
| [`GeoSeries.count_interior_rings`](api/geopandas.GeoSeries.count_interior_rings.html#geopandas.GeoSeries.count_interior_rings "geopandas.GeoSeries.count_interior_rings")() | Return a `Series` containing the count of the number of interior rings in a polygonal geometry. |
| [`GeoSeries.set_precision`](api/geopandas.GeoSeries.set_precision.html#geopandas.GeoSeries.set_precision "geopandas.GeoSeries.set_precision")(grid\_size[, mode]) | Return a `GeoSeries` with the precision set to a precision grid size. |
| [`GeoSeries.get_precision`](api/geopandas.GeoSeries.get_precision.html#geopandas.GeoSeries.get_precision "geopandas.GeoSeries.get_precision")() | Return a `Series` of the precision of each geometry. |
| [`GeoSeries.get_geometry`](api/geopandas.GeoSeries.get_geometry.html#geopandas.GeoSeries.get_geometry "geopandas.GeoSeries.get_geometry")(index) | Return the n-th geometry from a collection of geometries. |

## Unary predicates

|  |  |
| --- | --- |
| [`GeoSeries.is_closed`](api/geopandas.GeoSeries.is_closed.html#geopandas.GeoSeries.is_closed "geopandas.GeoSeries.is_closed") | Return a `Series` of `dtype('bool')` with value `True` if a LineString's or LinearRing's first and last points are equal. |
| [`GeoSeries.is_empty`](api/geopandas.GeoSeries.is_empty.html#geopandas.GeoSeries.is_empty "geopandas.GeoSeries.is_empty") | Returns a `Series` of `dtype('bool')` with value `True` for empty geometries. |
| [`GeoSeries.is_ring`](api/geopandas.GeoSeries.is_ring.html#geopandas.GeoSeries.is_ring "geopandas.GeoSeries.is_ring") | Return a `Series` of `dtype('bool')` with value `True` for features that are closed. |
| [`GeoSeries.is_simple`](api/geopandas.GeoSeries.is_simple.html#geopandas.GeoSeries.is_simple "geopandas.GeoSeries.is_simple") | Return a `Series` of `dtype('bool')` with value `True` for geometries that do not cross themselves. |
| [`GeoSeries.is_valid`](api/geopandas.GeoSeries.is_valid.html#geopandas.GeoSeries.is_valid "geopandas.GeoSeries.is_valid") | Return a `Series` of `dtype('bool')` with value `True` for geometries that are valid. |
| [`GeoSeries.is_valid_reason`](api/geopandas.GeoSeries.is_valid_reason.html#geopandas.GeoSeries.is_valid_reason "geopandas.GeoSeries.is_valid_reason")() | Return a `Series` of strings with the reason for invalidity of each geometry. |
| [`GeoSeries.is_valid_coverage`](api/geopandas.GeoSeries.is_valid_coverage.html#geopandas.GeoSeries.is_valid_coverage "geopandas.GeoSeries.is_valid_coverage")(\*[, gap\_width]) | Return a `bool` indicating whether a `GeoSeries` forms a valid coverage. |
| [`GeoSeries.invalid_coverage_edges`](api/geopandas.GeoSeries.invalid_coverage_edges.html#geopandas.GeoSeries.invalid_coverage_edges "geopandas.GeoSeries.invalid_coverage_edges")(\*[, gap\_width]) | Return a `GeoSeries` containing edges causing invalid polygonal coverage. |
| [`GeoSeries.has_m`](api/geopandas.GeoSeries.has_m.html#geopandas.GeoSeries.has_m "geopandas.GeoSeries.has_m") | Return a `Series` of `dtype('bool')` with value `True` for features that have a m-component. |
| [`GeoSeries.has_z`](api/geopandas.GeoSeries.has_z.html#geopandas.GeoSeries.has_z "geopandas.GeoSeries.has_z") | Return a `Series` of `dtype('bool')` with value `True` for features that have a z-component. |
| [`GeoSeries.is_ccw`](api/geopandas.GeoSeries.is_ccw.html#geopandas.GeoSeries.is_ccw "geopandas.GeoSeries.is_ccw") | Return a `Series` of `dtype('bool')` with value `True` if a LineString or LinearRing is counterclockwise. |

## Binary predicates

|  |  |
| --- | --- |
| [`GeoSeries.contains`](api/geopandas.GeoSeries.contains.html#geopandas.GeoSeries.contains "geopandas.GeoSeries.contains")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that contains other. |
| [`GeoSeries.contains_properly`](api/geopandas.GeoSeries.contains_properly.html#geopandas.GeoSeries.contains_properly "geopandas.GeoSeries.contains_properly")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that is completely inside `other`, with no common boundary points. |
| [`GeoSeries.crosses`](api/geopandas.GeoSeries.crosses.html#geopandas.GeoSeries.crosses "geopandas.GeoSeries.crosses")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that cross other. |
| [`GeoSeries.disjoint`](api/geopandas.GeoSeries.disjoint.html#geopandas.GeoSeries.disjoint "geopandas.GeoSeries.disjoint")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry disjoint to other. |
| [`GeoSeries.dwithin`](api/geopandas.GeoSeries.dwithin.html#geopandas.GeoSeries.dwithin "geopandas.GeoSeries.dwithin")(other, distance[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that is within a set distance from `other`. |
| [`GeoSeries.geom_equals`](api/geopandas.GeoSeries.geom_equals.html#geopandas.GeoSeries.geom_equals "geopandas.GeoSeries.geom_equals")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry equal to other. |
| [`GeoSeries.geom_equals_exact`](api/geopandas.GeoSeries.geom_equals_exact.html#geopandas.GeoSeries.geom_equals_exact "geopandas.GeoSeries.geom_equals_exact")(other, tolerance) | Return True for all geometries that equal aligned *other* to a given tolerance, else False. |
| [`GeoSeries.geom_equals_identical`](api/geopandas.GeoSeries.geom_equals_identical.html#geopandas.GeoSeries.geom_equals_identical "geopandas.GeoSeries.geom_equals_identical")(other[, align]) | Return True for all geometries that are identical aligned *other*, else False. |
| [`GeoSeries.intersects`](api/geopandas.GeoSeries.intersects.html#geopandas.GeoSeries.intersects "geopandas.GeoSeries.intersects")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that intersects other. |
| [`GeoSeries.overlaps`](api/geopandas.GeoSeries.overlaps.html#geopandas.GeoSeries.overlaps "geopandas.GeoSeries.overlaps")(other[, align]) | Return True for all aligned geometries that overlap *other*, else False. |
| [`GeoSeries.touches`](api/geopandas.GeoSeries.touches.html#geopandas.GeoSeries.touches "geopandas.GeoSeries.touches")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that touches other. |
| [`GeoSeries.within`](api/geopandas.GeoSeries.within.html#geopandas.GeoSeries.within "geopandas.GeoSeries.within")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that is within other. |
| [`GeoSeries.covers`](api/geopandas.GeoSeries.covers.html#geopandas.GeoSeries.covers "geopandas.GeoSeries.covers")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that is entirely covering other. |
| [`GeoSeries.covered_by`](api/geopandas.GeoSeries.covered_by.html#geopandas.GeoSeries.covered_by "geopandas.GeoSeries.covered_by")(other[, align]) | Return a `Series` of `dtype('bool')` with value `True` for each aligned geometry that is entirely covered by other. |
| [`GeoSeries.relate`](api/geopandas.GeoSeries.relate.html#geopandas.GeoSeries.relate "geopandas.GeoSeries.relate")(other[, align]) | Return the DE-9IM intersection matrices for the geometries. |
| [`GeoSeries.relate_pattern`](api/geopandas.GeoSeries.relate_pattern.html#geopandas.GeoSeries.relate_pattern "geopandas.GeoSeries.relate_pattern")(other, pattern[, align]) | Return True if the DE-9IM string code for the relationship between the geometries satisfies the pattern, else False. |

## Set-theoretic methods

|  |  |
| --- | --- |
| [`GeoSeries.clip_by_rect`](api/geopandas.GeoSeries.clip_by_rect.html#geopandas.GeoSeries.clip_by_rect "geopandas.GeoSeries.clip_by_rect")(xmin, ymin, xmax, ymax) | Return a `GeoSeries` of the portions of geometry within the given rectangle. |
| [`GeoSeries.difference`](api/geopandas.GeoSeries.difference.html#geopandas.GeoSeries.difference "geopandas.GeoSeries.difference")(other[, align, grid\_size]) | Return a `GeoSeries` of the points in each aligned geometry that are not in other. |
| [`GeoSeries.intersection`](api/geopandas.GeoSeries.intersection.html#geopandas.GeoSeries.intersection "geopandas.GeoSeries.intersection")(other[, align, grid\_size]) | Return a `GeoSeries` of the intersection of points in each aligned geometry with other. |
| [`GeoSeries.symmetric_difference`](api/geopandas.GeoSeries.symmetric_difference.html#geopandas.GeoSeries.symmetric_difference "geopandas.GeoSeries.symmetric_difference")(other[, ...]) | Return a `GeoSeries` of the symmetric difference of points in each aligned geometry with other. |
| [`GeoSeries.union`](api/geopandas.GeoSeries.union.html#geopandas.GeoSeries.union "geopandas.GeoSeries.union")(other[, align, grid\_size]) | Return a `GeoSeries` of the union of points in each aligned geometry with other. |

## Constructive methods and attributes

|  |  |
| --- | --- |
| [`GeoSeries.boundary`](api/geopandas.GeoSeries.boundary.html#geopandas.GeoSeries.boundary "geopandas.GeoSeries.boundary") | Return a `GeoSeries` of lower dimensional objects representing each geometry's set-theoretic boundary. |
| [`GeoSeries.buffer`](api/geopandas.GeoSeries.buffer.html#geopandas.GeoSeries.buffer "geopandas.GeoSeries.buffer")(distance[, quad\_segs, ...]) | Return a `GeoSeries` of geometries representing all points within a given `distance` of each geometric object. |
| [`GeoSeries.centroid`](api/geopandas.GeoSeries.centroid.html#geopandas.GeoSeries.centroid "geopandas.GeoSeries.centroid") | Return a `GeoSeries` of points representing the centroid of each geometry. |
| [`GeoSeries.concave_hull`](api/geopandas.GeoSeries.concave_hull.html#geopandas.GeoSeries.concave_hull "geopandas.GeoSeries.concave_hull")([ratio, allow\_holes]) | Return a `GeoSeries` of geometries representing the concave hull of vertices of each geometry. |
| [`GeoSeries.convex_hull`](api/geopandas.GeoSeries.convex_hull.html#geopandas.GeoSeries.convex_hull "geopandas.GeoSeries.convex_hull") | Return a `GeoSeries` of geometries representing the convex hull of each geometry. |
| [`GeoSeries.envelope`](api/geopandas.GeoSeries.envelope.html#geopandas.GeoSeries.envelope "geopandas.GeoSeries.envelope") | Return a `GeoSeries` of geometries representing the envelope of each geometry. |
| [`GeoSeries.extract_unique_points`](api/geopandas.GeoSeries.extract_unique_points.html#geopandas.GeoSeries.extract_unique_points "geopandas.GeoSeries.extract_unique_points")() | Return a `GeoSeries` of MultiPoints representing all distinct vertices of an input geometry. |
| [`GeoSeries.force_2d`](api/geopandas.GeoSeries.force_2d.html#geopandas.GeoSeries.force_2d "geopandas.GeoSeries.force_2d")() | Force the dimensionality of a geometry to 2D. |
| [`GeoSeries.force_3d`](api/geopandas.GeoSeries.force_3d.html#geopandas.GeoSeries.force_3d "geopandas.GeoSeries.force_3d")([z]) | Force the dimensionality of a geometry to 3D. |
| [`GeoSeries.make_valid`](api/geopandas.GeoSeries.make_valid.html#geopandas.GeoSeries.make_valid "geopandas.GeoSeries.make_valid")(\*[, method, keep\_collapsed]) | Repairs invalid geometries. |
| [`GeoSeries.minimum_bounding_circle`](api/geopandas.GeoSeries.minimum_bounding_circle.html#geopandas.GeoSeries.minimum_bounding_circle "geopandas.GeoSeries.minimum_bounding_circle")() | Return a `GeoSeries` of geometries representing the minimum bounding circle that encloses each geometry. |
| [`GeoSeries.maximum_inscribed_circle`](api/geopandas.GeoSeries.maximum_inscribed_circle.html#geopandas.GeoSeries.maximum_inscribed_circle "geopandas.GeoSeries.maximum_inscribed_circle")(\*[, ...]) | Return a `GeoSeries` of geometries representing the largest circle that is fully contained within the input geometry. |
| [`GeoSeries.minimum_clearance`](api/geopandas.GeoSeries.minimum_clearance.html#geopandas.GeoSeries.minimum_clearance "geopandas.GeoSeries.minimum_clearance")() | Return a `Series` containing the minimum clearance distance, which is the smallest distance by which a vertex of the geometry could be moved to produce an invalid geometry. |
| [`GeoSeries.minimum_clearance_line`](api/geopandas.GeoSeries.minimum_clearance_line.html#geopandas.GeoSeries.minimum_clearance_line "geopandas.GeoSeries.minimum_clearance_line")() | Return a `GeoSeries` of linestrings whose endpoints define the minimum clearance. |
| [`GeoSeries.minimum_rotated_rectangle`](api/geopandas.GeoSeries.minimum_rotated_rectangle.html#geopandas.GeoSeries.minimum_rotated_rectangle "geopandas.GeoSeries.minimum_rotated_rectangle")() | Return a `GeoSeries` of the general minimum bounding rectangle that contains the object. |
| [`GeoSeries.normalize`](api/geopandas.GeoSeries.normalize.html#geopandas.GeoSeries.normalize "geopandas.GeoSeries.normalize")() | Return a `GeoSeries` of normalized geometries to normal form (or canonical form). |
| [`GeoSeries.orient_polygons`](api/geopandas.GeoSeries.orient_polygons.html#geopandas.GeoSeries.orient_polygons "geopandas.GeoSeries.orient_polygons")(\*[, exterior\_cw]) | Return a `GeoSeries` of geometries with enforced ring orientation. |
| [`GeoSeries.remove_repeated_points`](api/geopandas.GeoSeries.remove_repeated_points.html#geopandas.GeoSeries.remove_repeated_points "geopandas.GeoSeries.remove_repeated_points")([tolerance]) | Return a `GeoSeries` containing a copy of the input geometry with repeated points removed. |
| [`GeoSeries.reverse`](api/geopandas.GeoSeries.reverse.html#geopandas.GeoSeries.reverse "geopandas.GeoSeries.reverse")() | Return a `GeoSeries` with the order of coordinates reversed. |
| [`GeoSeries.sample_points`](api/geopandas.GeoSeries.sample_points.html#geopandas.GeoSeries.sample_points "geopandas.GeoSeries.sample_points")(size[, method, rng]) | Sample points from each geometry. |
| [`GeoSeries.segmentize`](api/geopandas.GeoSeries.segmentize.html#geopandas.GeoSeries.segmentize "geopandas.GeoSeries.segmentize")(max\_segment\_length) | Return a `GeoSeries` with vertices added to line segments based on maximum segment length. |
| [`GeoSeries.shortest_line`](api/geopandas.GeoSeries.shortest_line.html#geopandas.GeoSeries.shortest_line "geopandas.GeoSeries.shortest_line")(other[, align]) | Return the shortest two-point line between two geometries. |
| [`GeoSeries.simplify`](api/geopandas.GeoSeries.simplify.html#geopandas.GeoSeries.simplify "geopandas.GeoSeries.simplify")(tolerance[, ...]) | Return a `GeoSeries` containing a simplified representation of each geometry. |
| [`GeoSeries.simplify_coverage`](api/geopandas.GeoSeries.simplify_coverage.html#geopandas.GeoSeries.simplify_coverage "geopandas.GeoSeries.simplify_coverage")(tolerance, \*[, ...]) | Return a `GeoSeries` containing a simplified representation of polygonal coverage. |
| [`GeoSeries.snap`](api/geopandas.GeoSeries.snap.html#geopandas.GeoSeries.snap "geopandas.GeoSeries.snap")(other, tolerance[, align]) | Snap the vertices and segments of the geometry to vertices of the reference. |
| [`GeoSeries.transform`](api/geopandas.GeoSeries.transform.html#geopandas.GeoSeries.transform "geopandas.GeoSeries.transform")(transformation[, include\_z]) | Return a `GeoSeries` with the transformation function applied to the geometry coordinates. |

## Affine transformations

|  |  |
| --- | --- |
| [`GeoSeries.affine_transform`](api/geopandas.GeoSeries.affine_transform.html#geopandas.GeoSeries.affine_transform "geopandas.GeoSeries.affine_transform")(matrix) | Return a `GeoSeries` with translated geometries. |
| [`GeoSeries.rotate`](api/geopandas.GeoSeries.rotate.html#geopandas.GeoSeries.rotate "geopandas.GeoSeries.rotate")(angle[, origin, use\_radians]) | Return a `GeoSeries` with rotated geometries. |
| [`GeoSeries.scale`](api/geopandas.GeoSeries.scale.html#geopandas.GeoSeries.scale "geopandas.GeoSeries.scale")([xfact, yfact, zfact, origin]) | Return a `GeoSeries` with scaled geometries. |
| [`GeoSeries.skew`](api/geopandas.GeoSeries.skew.html#geopandas.GeoSeries.skew "geopandas.GeoSeries.skew")([xs, ys, origin, use\_radians]) | Return a `GeoSeries` with skewed geometries. |
| [`GeoSeries.translate`](api/geopandas.GeoSeries.translate.html#geopandas.GeoSeries.translate "geopandas.GeoSeries.translate")([xoff, yoff, zoff]) | Return a `GeoSeries` with translated geometries. |

## Linestring operations

|  |  |
| --- | --- |
| [`GeoSeries.interpolate`](api/geopandas.GeoSeries.interpolate.html#geopandas.GeoSeries.interpolate "geopandas.GeoSeries.interpolate")(distance[, normalized]) | Return a point at the specified distance along each geometry. |
| [`GeoSeries.line_merge`](api/geopandas.GeoSeries.line_merge.html#geopandas.GeoSeries.line_merge "geopandas.GeoSeries.line_merge")([directed]) | Return (Multi)LineStrings formed by combining the lines in a MultiLineString. |
| [`GeoSeries.project`](api/geopandas.GeoSeries.project.html#geopandas.GeoSeries.project "geopandas.GeoSeries.project")(other[, normalized, align]) | Return the distance along each geometry nearest to *other*. |
| [`GeoSeries.shared_paths`](api/geopandas.GeoSeries.shared_paths.html#geopandas.GeoSeries.shared_paths "geopandas.GeoSeries.shared_paths")(other[, align]) | Return the shared paths between two geometries. |

## Aggregating and exploding

|  |  |
| --- | --- |
| [`GeoSeries.build_area`](api/geopandas.GeoSeries.build_area.html#geopandas.GeoSeries.build_area "geopandas.GeoSeries.build_area")([node]) | Create an areal geometry formed by the constituent linework. |
| [`GeoSeries.constrained_delaunay_triangles`](api/geopandas.GeoSeries.constrained_delaunay_triangles.html#geopandas.GeoSeries.constrained_delaunay_triangles "geopandas.GeoSeries.constrained_delaunay_triangles")() | Return a [`GeoSeries`](api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") with the constrained Delaunay triangulation of polygons. |
| [`GeoSeries.delaunay_triangles`](api/geopandas.GeoSeries.delaunay_triangles.html#geopandas.GeoSeries.delaunay_triangles "geopandas.GeoSeries.delaunay_triangles")([tolerance, ...]) | Return a `GeoSeries` consisting of objects representing the computed Delaunay triangulation between the vertices of an input geometry. |
| [`GeoSeries.explode`](api/geopandas.GeoSeries.explode.html#geopandas.GeoSeries.explode "geopandas.GeoSeries.explode")([ignore\_index, index\_parts]) | Explode multi-part geometries into multiple single geometries. |
| [`GeoSeries.intersection_all`](api/geopandas.GeoSeries.intersection_all.html#geopandas.GeoSeries.intersection_all "geopandas.GeoSeries.intersection_all")() | Return a geometry containing the intersection of all geometries in the `GeoSeries`. |
| [`GeoSeries.polygonize`](api/geopandas.GeoSeries.polygonize.html#geopandas.GeoSeries.polygonize "geopandas.GeoSeries.polygonize")([node, full]) | Create polygons formed from the linework of a GeoSeries. |
| [`GeoSeries.union_all`](api/geopandas.GeoSeries.union_all.html#geopandas.GeoSeries.union_all "geopandas.GeoSeries.union_all")([method, grid\_size]) | Return a geometry containing the union of all geometries in the `GeoSeries`. |
| [`GeoSeries.voronoi_polygons`](api/geopandas.GeoSeries.voronoi_polygons.html#geopandas.GeoSeries.voronoi_polygons "geopandas.GeoSeries.voronoi_polygons")([tolerance, ...]) | Return a `GeoSeries` consisting of objects representing the computed Voronoi diagram around the vertices of an input geometry. |

## Serialization / IO / conversion

|  |  |
| --- | --- |
| [`GeoSeries.from_arrow`](api/geopandas.GeoSeries.from_arrow.html#geopandas.GeoSeries.from_arrow "geopandas.GeoSeries.from_arrow")(arr, \*\*kwargs) | Construct a GeoSeries from an Arrow array object with a GeoArrow extension type. |
| [`GeoSeries.from_file`](api/geopandas.GeoSeries.from_file.html#geopandas.GeoSeries.from_file "geopandas.GeoSeries.from_file")(filename, \*\*kwargs) | Alternate constructor to create a `GeoSeries` from a file. |
| [`GeoSeries.from_wkb`](api/geopandas.GeoSeries.from_wkb.html#geopandas.GeoSeries.from_wkb "geopandas.GeoSeries.from_wkb")(data[, index, crs, ...]) | Alternate constructor to create a `GeoSeries` from a list or array of WKB objects. |
| [`GeoSeries.from_wkt`](api/geopandas.GeoSeries.from_wkt.html#geopandas.GeoSeries.from_wkt "geopandas.GeoSeries.from_wkt")(data[, index, crs, ...]) | Alternate constructor to create a `GeoSeries` from a list or array of WKT objects. |
| [`GeoSeries.from_xy`](api/geopandas.GeoSeries.from_xy.html#geopandas.GeoSeries.from_xy "geopandas.GeoSeries.from_xy")(x, y[, z, index, crs]) | Alternate constructor to create a [`GeoSeries`](api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of Point geometries from lists or arrays of x, y(, z) coordinates. |
| [`GeoSeries.to_arrow`](api/geopandas.GeoSeries.to_arrow.html#geopandas.GeoSeries.to_arrow "geopandas.GeoSeries.to_arrow")([geometry\_encoding, ...]) | Encode a GeoSeries to GeoArrow format. |
| [`GeoSeries.to_file`](api/geopandas.GeoSeries.to_file.html#geopandas.GeoSeries.to_file "geopandas.GeoSeries.to_file")(filename[, driver, index]) | Write the `GeoSeries` to a file. |
| [`GeoSeries.to_json`](api/geopandas.GeoSeries.to_json.html#geopandas.GeoSeries.to_json "geopandas.GeoSeries.to_json")([show\_bbox, drop\_id, to\_wgs84]) | Return a GeoJSON string representation of the GeoSeries. |
| [`GeoSeries.to_wkb`](api/geopandas.GeoSeries.to_wkb.html#geopandas.GeoSeries.to_wkb "geopandas.GeoSeries.to_wkb")([hex]) | Convert GeoSeries geometries to WKB. |
| [`GeoSeries.to_wkt`](api/geopandas.GeoSeries.to_wkt.html#geopandas.GeoSeries.to_wkt "geopandas.GeoSeries.to_wkt")(\*\*kwargs) | Convert GeoSeries geometries to WKT. |

## Projection handling

|  |  |
| --- | --- |
| [`GeoSeries.crs`](api/geopandas.GeoSeries.crs.html#geopandas.GeoSeries.crs "geopandas.GeoSeries.crs") | The Coordinate Reference System (CRS) as a `pyproj.CRS` object. |
| [`GeoSeries.set_crs`](api/geopandas.GeoSeries.set_crs.html#geopandas.GeoSeries.set_crs "geopandas.GeoSeries.set_crs")(\*\*kwargs) |  |
| [`GeoSeries.to_crs`](api/geopandas.GeoSeries.to_crs.html#geopandas.GeoSeries.to_crs "geopandas.GeoSeries.to_crs")([crs, epsg]) | Return a `GeoSeries` with all geometries transformed to a new coordinate reference system. |
| [`GeoSeries.estimate_utm_crs`](api/geopandas.GeoSeries.estimate_utm_crs.html#geopandas.GeoSeries.estimate_utm_crs "geopandas.GeoSeries.estimate_utm_crs")([datum\_name]) | Return the estimated UTM CRS based on the bounds of the dataset. |

## Missing values

|  |  |
| --- | --- |
| [`GeoSeries.fillna`](api/geopandas.GeoSeries.fillna.html#geopandas.GeoSeries.fillna "geopandas.GeoSeries.fillna")([value, inplace, limit]) | Fill NA values with geometry (or geometries). |
| [`GeoSeries.isna`](api/geopandas.GeoSeries.isna.html#geopandas.GeoSeries.isna "geopandas.GeoSeries.isna")() | Detect missing values. |
| [`GeoSeries.notna`](api/geopandas.GeoSeries.notna.html#geopandas.GeoSeries.notna "geopandas.GeoSeries.notna")() | Detect non-missing values. |

## Overlay operations

|  |  |
| --- | --- |
| [`GeoSeries.clip`](api/geopandas.GeoSeries.clip.html#geopandas.GeoSeries.clip "geopandas.GeoSeries.clip")(mask[, keep\_geom\_type, sort]) | Clip points, lines, or polygon geometries to the mask extent. |

## Plotting

|  |  |
| --- | --- |
| [`GeoSeries.plot`](api/geopandas.GeoSeries.plot.html#geopandas.GeoSeries.plot "geopandas.GeoSeries.plot")(\*args, \*\*kwargs) | Plot a GeoSeries. |
| [`GeoSeries.explore`](api/geopandas.GeoSeries.explore.html#geopandas.GeoSeries.explore "geopandas.GeoSeries.explore")(\*args, \*\*kwargs) | Explore with an interactive map based on folium/leaflet.js.Interactive map based on GeoPandas and folium/leaflet.js. |

## Spatial index

|  |  |
| --- | --- |
| [`GeoSeries.sindex`](api/geopandas.GeoSeries.sindex.html#geopandas.GeoSeries.sindex "geopandas.GeoSeries.sindex") | Generate the spatial index. |
| [`GeoSeries.has_sindex`](api/geopandas.GeoSeries.has_sindex.html#geopandas.GeoSeries.has_sindex "geopandas.GeoSeries.has_sindex") | Check the existence of the spatial index without generating it. |

## Indexing

|  |  |
| --- | --- |
| [`GeoSeries.cx`](api/geopandas.GeoSeries.cx.html#geopandas.GeoSeries.cx "geopandas.GeoSeries.cx") | Coordinate based indexer to select by intersection with bounding box. |

## Interface

|  |  |
| --- | --- |
| [`GeoSeries.__geo_interface__`](api/geopandas.GeoSeries.__geo_interface__.html#geopandas.GeoSeries.__geo_interface__ "geopandas.GeoSeries.__geo_interface__") | Returns a `GeoSeries` as a python feature collection. |

Methods of pandas `Series` objects are also available, although not
all are applicable to geometric objects and some may return a
`Series` rather than a `GeoSeries` result when appropriate. The methods
`isna()` and `fillna()` have been
implemented specifically for `GeoSeries` and are expected to work
correctly.

On this page

[Show Source](../../_sources/docs/reference/geoseries.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/geoseries.html
