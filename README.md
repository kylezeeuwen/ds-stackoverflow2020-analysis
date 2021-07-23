# Overview

This code in this repo uses the Python [pandas](LINK TODO) and [sklearn](LINK TODO) libraries to analyse the [Stack Overflow 2020 Developer Survey Results](LINK TODO) .

The focus of this analysis is to look at differences in responses by country and attempt to build linear classifiers for specific countries.

The author is a noob data scientist completing the Udacity Data Science Nano degree, and the first assignment requires:

* [this repo](LINK TODO)
* [this blog](LINK TODO), which I choose to post on medium

The classifiers suck and should not be used in any meaningful way, but the journey was bountiful and well documented.

# Installation Notes

This repo assumes a local docker installation, and uses the jupyter/datascience-notebook to create a portable workspace that requires no other installation.

To get this running locally on OSX or Linux:
  * install [docker desktop](LINK TODO)
  * in your terminal of choice with CWD set to the repo root execute: `./bin/go.sh`
  * in the lines of text output, find the localhost link and copy/paste it into your browser. Example link:
    * `http://127.0.0.1:8888/lab?token=abc123beepbeep456boopboop`

`./bin/go.sh` creates a docker container hosting the jupyter notebook with a mount the the `./notebooks` directory of this repo.

This is the content of the bin/go file circa July 17, 2021:

```js
docker run --rm -p 8888:8888 --name ds-so2020 -e JUPYTER_ENABLE_LAB=yes -v $(pwd)/notebook:/home/jovyan/work jupyter/datascience-notebook:latest
```

TODO Ask udacity if they want the full survey committed or not 

# Motivation

From above:

> The author is a noob data scientist completing the Udacity Data Science Nano degree, and the first assignment requires a repo and a blog.

That aside the code seeks to analyse the [SO 2020 dataset](LINK TODO) with several objectives in mind:

    * practice data prep techniques including removal and imputation
    * experiment with sklearn models
    * attempt to build classifiers that identify membership to a specific country as a boolean
    * create a well documented future reference for all of the above

# File Descriptors

Any analysis presented in the blog will have a specific python notebook to show the work and demonstrate reproducability.

There are some notebook files not used in the blog which are also included in the repo.

The notebooks in the jupyter workspace (i.e., `./notebooks`) are listed below, followed by the list of python helper files and descriptions.

### Notebooks
* (BLOG) top_10_countries_measured_by_response_count.ipynb - showing survey responses by country
* (BLOG) top_10_countries_proportion_of_nope.ipynb - showing modelling results by country, hilighting the dataset imbalance issues
* (BLOG) visualise_binary_classifier_results.ipynb - analysis and charts for binary classifiers 
* basics.ipynb - notebook showing first steps to probe dataset 
* value_counts.ipynb - notebook showing some drill down steps to probe dataset
* country_classifier.ipynb - orchestrate the data prep and modelling phases of [CRISP-DM](LINK TODO) 


### Misc
* assets.* - the contents of the [SO 2020 dataset zip file](LINK TODO) 
* pickles - not git maintained as pickles [ARE NOT SAFE](LINK TODO) but they are super useful while iterating

### Libraries
* convert_multiple_choice_to_dataframe.py - impute multiple choice columns
* helpers.py - misc helpers TODO split up better
* models.py - collection of wrappers around sklearn models
* predict_country.py - run multiple models with a list of cutoffs on a specific country

# How to interact with project

The `ipynb` files should not be read directly using an IDE - they are meant to be interacted with using a browser. The Installation section above outlines how to run `./bin/go.sh` and then copy/paste the provided URL into a browser.

All notebooks can be rerun to reproduce the results.

If you want to contribute, fork and submit a PR, that would be top notch.

# Developer Notes

Original readme [here](./docs/original_readme.md)

#Licencing

Go nuts. Really, just get right in there.

[MIT License](LINK TODO)

#Authors

This is the work of Kyle Zeeuwen. There is some inspiration and probably borrowed code from the course presenter jjrunner, specifically this repo. 

#Acknowledgements

Udacity is so far so good [thumbs up](TODO LINK)