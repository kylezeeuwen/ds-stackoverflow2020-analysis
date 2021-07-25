
# Overview

This code in this repo uses the Python [pandas](https://pandas.pydata.org/) and [sklearn](https://scikit-learn.org/) libraries to analyse the [Stack Overflow 2020 Developer Survey Results](https://insights.stackoverflow.com/survey/2020).

The focus of this analysis is to look at differences in responses by country and attempt to build linear classifiers for specific countries.

The author is a noob data scientist completing the [Udacity Data Science Nano degree](https://www.udacity.com/course/data-scientist-nanodegree--nd025), and the first assignment requires:

* [a repo](https://github.com/kylezeeuwen/ds-stackoverflow2020-analysis/)
* [a blog](https://medium.com/@kylezeeuwen/does-the-country-change-the-developer-ce18116e905f)

The classifiers suck and should not be used in any meaningful way, but the journey was bountiful and well documented.

# Installation Notes

## Get the survey results

I chose not to include the 94MB survey results in the git repo. So you will need to get them yourself.

* Go [here](https://drive.google.com/file/d/1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB/view)
* download and ensure this file is in place: notebook/assets/survey_results_public.csv
* download and ensure this file is in place: notebook/assets/survey_results_schema.csv

## (Option A) Run notebooks via docker

This repo assumes a local docker installation, and uses the jupyter/datascience-notebook to create a portable workspace that requires no other installation.

To get this running locally on OSX or Linux:
  * install [docker desktop](https://www.docker.com/products/docker-desktop)
  * in your terminal of choice with CWD set to the repo root execute: `./bin/go.sh`
  * in the lines of text output, find the localhost link and copy/paste it into your browser. Example link:
    * `http://127.0.0.1:8888/lab?token=abc123beepbeep456boopboop`

`./bin/go.sh` creates a docker container hosting the jupyter notebook with a mount the the `./notebooks` directory of this repo.

This is the content of the bin/go file circa July 17, 2021:

```js
docker run --rm -p 8888:8888 --name ds-so2020 -e JUPYTER_ENABLE_LAB=yes -v $(pwd)/notebook:/home/jovyan/work jupyter/datascience-notebook:latest
```

## (Option B) Run notebooks locally via ipython

NOTE: only tested on mac

Simply run `./setup.sh` to create a python virtual env, and install all required dependencies

# Motivation

From above:

> The author is a noob data scientist completing the Udacity Data Science Nano degree, and the first assignment requires a repo and a blog.

That aside the code seeks to analyse the SO 2020 dataset with several objectives in mind:

    * practice data prep techniques including removal and imputation
    * experiment with sklearn models
    * attempt to build classifiers that identify membership to a specific country as a boolean
    * create a well documented future reference for all of the above

# File Descriptors

Any analysis presented in [the blog]((https://medium.com/@kylezeeuwen/does-the-country-change-the-developer-ce18116e905f)) will have a specific python notebook to show the work and demonstrate reproducability.

There are some notebook files not used in the blog which are also included in the repo.

The notebooks in the jupyter workspace (i.e., `./notebooks`) are listed below, followed by the list of python helper files and descriptions.

### Notebooks
* [1_basics.ipynb](./notebook/1_basics.ipynb) - notebook showing first steps to probe dataset 
* [2_value_counts.ipynb](./notebook/2_value_counts.ipynb) - notebook showing some drill down steps to probe dataset
* [3_top_10_countries_measured_by_response_count.ipynb](./notebook/3_top_10_countries_measured_by_response_count.ipynb) - showing survey responses by country
* [4_multiple_choice_responses.ipynb](./notebook/4_multiple_choice_responses.ipynb) - show answers by deviation from mean and microsoft sentiment analysis 
* [5_country_classifier.ipynb](./notebook/5_country_classifier.ipynb) - orchestrate the data prep and modelling phases of [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining) 
* [6_visualise_binary_classifier_results.ipynb](./notebook/6_visualise_binary_classifier_results.ipynb) - analysis binary classifier results 

### Misc
* assets.* - the contents of the [SO 2020 dataset zip file](https://drive.google.com/file/d/1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB/view) 
* pickles - the classifier results used in the blog

### Libraries
* country_classifier/clone_and_convert_multiple_choice_columns.py - impute multiple choice columns
* country_classifier/clone_drop_and_convert.py - drop some columns and convert some columns
* country_classifier/clone_impute_data.py - main imputation function
* country_classifier/models.py - collection of wrappers around sklearn models
* country_classifier/predict_country.py - run multiple models with a list of cutoffs on a specific country

# How to interact with project

The `ipynb` files should not be read directly using an IDE - they are meant to be interacted with using a browser. The Installation section above outlines how to run `./bin/go.sh` and then copy/paste the provided URL into a browser.

All notebooks can be rerun to reproduce the results.

If you want to contribute, fork and submit a PR, that would be top notch.

# Licencing

Go nuts. Really, just get right in there.

[MIT License](./LICENSE)

# Authors

This is the work of Kyle Zeeuwen. There is some inspiration and probably borrowed code from the course presenter Josh Bernhard, specifically this [repo](https://github.com/jjrunner/stackoverflow). 

# Acknowledgements

* Udacity is so far so good 👍. The review of my first submission was thorough and valuable. Some cliff notes can be found [here](./docs/project_rubric.md) 
* Cover photo : https://unsplash.com/photos/oMpAz-DN-9I : free via [Unsplash](https://unsplash.com/license) : great photo by [Greg Rakozy](https://unsplash.com/@grakozy)
* Stack Overflow for conducting the survey and sharing the [results](https://insights.stackoverflow.com/survey/2020) 