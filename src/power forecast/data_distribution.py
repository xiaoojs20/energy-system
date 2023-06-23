import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('../../data/raw_pvdaq/pvdaq_2012_2014_hourly.csv', header=0, infer_datetime_format=True, parse_dates=['Date-Time'], index_col=['Date-Time'])



