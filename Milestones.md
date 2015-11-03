# 1.0 #
## Rationale ##
The 1.0 release is intended to be a basic, usable, implementation of 2D pathfinding. Most basic 2D pathfinding operations must be covered.


## Milestone Targets ##
Items with (?) are more likely to be removed later.

Implement the following pathfinding algorithms in both Python and C/Cython/Pyrex:
  * A`*`
  * D`*`
  * Bidirectional Search
  * Breadth-First Search

Implement the following heuristic functions and metrics in both Python and C/Cython/Pyrex:
  * Manhattan Metric
  * Euclidean Metric
  * Discrete Metric
  * Euclidean Squared heuristic
  * 0 heuristic

Implement the following types of nodes:
  * Tessellating Rectangles
  * Tessellating Triangles
  * Tessellating Hexagons
  * Region Quadtree of Rectangles
  * Region Quadtree of Triangles (?)
  * Region Quadtree of Hexagons (?)

Implement dummy APIs for the following existing libraries:
  * Dijkstar
  * PGU's A`*`

Implement map-loading for the following file formats (more specifics once non-rectangular pathfinding is realized):
  * plaintext
  * image