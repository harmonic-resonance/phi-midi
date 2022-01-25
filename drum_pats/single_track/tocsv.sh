#!/usr/bin/env bash

for f in *
do
  midicsvpy $f $f.csv
done
