#!/bin/bash
python ./main.py
cd images/minkowski
ffmpeg -i %03d.png ../minkowski.gif
cd ../euclidean
ffmpeg -i %03d.png ../euclidean.gif
