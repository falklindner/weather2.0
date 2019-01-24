import pandas as pd
import time 
import json
import urllib.request
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from pandas.io.json import json_normalize
from joblib import Parallel, delayed
import statsmodels.api as sm
from scipy import stats
from sklearn.metrics import mean_squared_error


df = pd.read_json("https://alte-rs.westeurope.cloudapp.azure.com/weather/processed/history.json")
df['time'] = pd.to_datetime(df['time'])
df['temp'] = pd.to_numeric(df['temp'])
df['pressure'] = pd.to_numeric(df['pressure'])
df['humidity'] = pd.to_numeric(df['humidity'])
dataframe_rpi = df.set_index('time')
print(dataframe_rpi.shape)
print(dataframe_rpi.head())