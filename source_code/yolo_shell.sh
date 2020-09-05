#!/bin/sh

cd darknet
./darknet detect cfg/yolo.cfg yolo.weights data/$1
cp data/$1 ../static/input.jpg
cp predictions.png ../static/results.png

exit