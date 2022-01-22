#!/usr/bin/env bash

source ~/.bashrc

for f in *; do
  midicsvpy "$f" "$(slugify "$f").csv"
  
done
