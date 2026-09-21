# Computational Geometry

Computational geometry algorithms operate on points, lines, segments, polygons, and planar subdivisions.

## Fundamental primitive
For points A,B,C, the orientation sign is the sign of cross(B-A,C-A):
- positive: counter-clockwise;
- negative: clockwise;
- zero: collinear.

This one predicate supports segment intersection, hulls, and many sweep-line algorithms.

## Core algorithms
- Segment intersection.
- Convex hull: Graham scan, monotonic chain.
- Closest pair of points.
- Point-in-polygon: ray casting / winding concepts.
- Line sweep.
- Rotating calipers.
- Polygon area with the shoelace formula.
- Circle/line intersection.
- Range searching and spatial trees.

## Robustness
Geometry code must handle collinearity, duplicate points, integer overflow, floating-point tolerance, and boundary inclusion consistently.

## Complexity
Sorting-based hulls are typically O(n log n). Many geometric algorithms are dominated by sorting or event processing.
