# Import base functions

from IPython.display import display

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import statsmodels.api as sm
import statsmodels.formula.api as smf

import scipy
from scipy import stats

import sklearn

# import wrangalytics
# from wrangalytics.config import api as config

from wrangalytics.converters.api import percent2float as p2f
from wrangalytics.converters.api import str2float as s2f
from wrangalytics.converters.api import str2int as s2i

from imp import reload

def debug(x):
    print(x)

### Notebook Magics
# %matplotlib inline

def juptyerConfig(pd, max_columns=500, max_rows = 500, float_format = '{:,.6f}', max_info_rows = 1000, max_categories = 500):
    pd.options.display.max_columns = 500
    pd.options.display.max_rows = 500
    pd.options.display.float_format = float_format.format
    pd.options.display.max_info_rows = 1000
    pd.options.display.max_categories = 500

def createDataFilePath(data_dir='', data_file_name=''):
    return data_dir + data_file_name