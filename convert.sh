#!/bin/bash
cd images/minkowski
convert -delay 4 -loop 0 *.png ../minkowski.gif
cd ../euclidean
convert -delay 4 -loop 0 *.png ../euclidean.gif
