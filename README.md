# ds-stackoverflow2020-analysis
analysis of stackoverflow 2020  developer survey results. Includes code and writeup.

# Developer notes

## Running Jupyter via docker locally

Prerequisites:
  * `docker` installed
  * current working directory must be project root directory

Execute the following on your terminal of choice

```
docker run --rm -p 8888:8888 --name ds-so2020 -e JUPYTER_ENABLE_LAB=yes -v $(pwd)/notebook:/home/jovyan/work jupyter/datascience-notebook:latest
```

To FILE:
* https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#run-jupyter-notebook-lab-inside-an-already-secured-environment-i-e-with-no-token

## Container details

Jupyter maintain a series of docker images depending on what you want. See a visualisation of the layering [here](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#image-relationships). 

* jupyter/datascience-notebook
  * repo: https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook
  * base image: jupyter/scipy-notebook  
* jupyter/scipy-notebook
  * repo: https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook
  * base image: jupyter/minimal-notebook
* jupyter/minimal-notebook
  * repo: https://github.com/jupyter/docker-stacks/blob/master/minimal-notebook  
* jupyter/base-notebook
  * repo: https://github.com/jupyter/docker-stacks/tree/master/base-notebook
  * base image: Ubuntu 20.04  
    
### Relevant switches

You can find the actual entry point script here and here:
* https://github.com/jupyter/docker-stacks/blob/master/base-notebook/start-notebook.sh
* https://github.com/jupyter/docker-stacks/blob/master/base-notebook/start.sh <--- most of the work

Some env vars to control behaviour:
* GRANT_SUDO : allow sudo to install new things

### Security token settings

Trying to setup an easy way to run locally without the password/token requirement

**so far none of these work**

https://jupyter-notebook.readthedocs.io/en/stable/security.html

Password and token checks can be disabled for local dev - not recommended! - by setting 

```js
c.NotebookApp.token = ''
c.NotebookApp.password = ''
```

in the config file in the container at this path ~/.jupyter/jupyter_notebook_config.py  

You can also override the docker container CMD and args via 

```js
docker run --rm -p 8888:8888 --name ds-so2020 -e JUPYTER_ENABLE_LAB=yes -v $(pwd)/notebook:/home/jovyan/work jupyter/datascience-notebook:latest "start-notebook.sh" "--NotebookApp.token='' --NotebookApp.password=''"
```
