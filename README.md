# ds-stackoverflow2020-analysis
analysis of stackoverflow 2020  developer survey results. Includes code and writeup.

# Developer notes

## Running Jupyter via docker locally

Prerequisites:
  * `docker` installed
  * current working directory must be project root directory

Execute the following on your terminal of choice

```
docker run --rm -p 8888:8888 --name ds-so2020 -e JUPYTER_ENABLE_LAB=yes -v /ABS/PATH/TO/notebook:/home/jovyan/work jupyter/datascience-notebook:latest
```

To FILE:
* https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#run-jupyter-notebook-lab-inside-an-already-secured-environment-i-e-with-no-token
