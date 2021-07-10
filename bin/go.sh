#!/bin/bash

docker run --rm -p 8888:8888 --name ds-so2020 -e JUPYTER_ENABLE_LAB=yes -v $(pwd)/notebook:/home/jovyan/work jupyter/datascience-notebook:latest
