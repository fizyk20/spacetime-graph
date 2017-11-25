# spacetime-graph

This repository contains some scripts which I use to generate animated spacetime diagrams.

The diagram is defined by creating a `Scene` object and adding primitive objects to it (I have a plan to improve this system a bit - add more natural objects like a coordinate system or a moving body).

Currently available objects:

* `Scene` - represents a collection of other objects to be transformed together
* `Point` - a single point
* `Line` - just a straight line
* `Arrow` - a line ending with an arrow head (a triangle)
* `Circle` - nothing to add here :p
* `Hyperbola` - a hyperbola defined by (cosh(t), sinh(t))
* `Text` - a text label; only gets translated and rotated with coordinate transformations

`main.py` generates 200 frames in two folders, to be combined into two animations. The animations show how rotations and Lorentz transformations affect a coordinate system. The result can be seen [here](https://imgur.com/gallery/Ht4rr).

The scripts `generate.sh` and `convert.sh` automate the generation of the GIFs.

### Dependencies

* PyQt4
* PyOpenGL
* PyFTGL
* numpy
