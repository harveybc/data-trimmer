# Preprocessor: Standardizer

A simple data pre-processor that standardize a dataset and exports the standarization configuration for use on other datasets. Usable both from command line and from class methods.

[![Build Status](https://travis-ci.org/harveybc/preprocessor.svg?branch=master)](https://travis-ci.org/harveybc/preprocessor)
[![Documentation Status](https://readthedocs.org/projects/docs/badge/?version=latest)](https://harveybc-preprocessor.readthedocs.io/en/latest/)
[![BCH compliance](https://bettercodehub.com/edge/badge/harveybc/preprocessor?branch=master)](https://bettercodehub.com/)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/harveybc/preprocessor/blob/master/LICENSE)

## Description

Uses sklearn.preprocessing.StandardScaler to standardize features by removing the mean and scaling to unit variance.

Exports the standarization configuration for use on other datasets. Usable both from command line and from class methods.

The standardizer is implemented in the Standardizer class, it has methods for loading a dataset, standardizing it and producing an output dataset and a configuration file that can be loaded and applied to another dataset, please see [test_standarizer](https://github.com/harveybc/preprocessor/blob/master/tests/standardizer/test_standardizer.py). It can also be used via command line.

## Installation

The module is installed with the preprocessor package, the instructions are described in the [preprocessor README](../master/README.md).

### Command-Line Execution

The standardizer also is implemented as a console command:
> standardizer -- input_file <input_dataset> <optional_parameters>

### Command-Line Parameters

* __--input_file <filename>__: The only mandatory parameter, is the filename for the input dataset to be processed.
* __--output_file <filename>__: (Optional) Filename for the output dataset. Defaults to the input dataset with the .output extension.
* __--output_config_file <filename>__: (Optional) Filename for the output configuration containing rows trimmed in columns 0 and columns trimmed in column 1. Defaults to the input dataset with the .config extension.
* __--input_config_file <filename>__: (Optional) Imports an existing configuration and trims a dataset with it.

## Examples of usage
The following examples show both the class method and command line uses.

### Usage via Class Methods
```python
from preprocessor.standardizer.standardizer import Standardizer
# configure parameters (same vaiable names as command-line parameters)
class Conf:
    def __init__(self):
        self.input_file = "tests/data/test_input.csv"
conf = Conf()
# instance trimmer class and loads dataset
st = Standardizer(conf)
# do the trimming
st.standardize()
# save output to output file
st.store()
```

### Usage via CLI

> standardizer --input_file "tests/data/test_input.csv"






