import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('data/raw_pvdaq/pvdaq_data_1277_2012.csv', header=0, infer_datetime_format=True, parse_dates=['Date-Time'], index_col=['Date-Time'])
df2 = pd.read_csv('data/raw_pvdaq/pvdaq_data_1277_2013.csv', header=0, infer_datetime_format=True, parse_dates=['Date-Time'], index_col=['Date-Time'])
df3 = pd.read_csv('data/raw_pvdaq/pvdaq_data_1277_2014.csv', header=0, infer_datetime_format=True, parse_dates=['Date-Time'], index_col=['Date-Time'])
df = pd.concat([df1, df2, df3])
df.info()

# Imputing the Time-Series
df_filled = df.interpolate(method='slinear')
df_filled.info()
df_filled.to_csv('data/raw_pvdaq/pvdaq_2012_2014_15min.csv')
df_resampled = df_filled.resample('1H').mean()
df_resampled.info()
df_resampled.to_csv('data/raw_pvdaq/pvdaq_2012_2014_hourly.csv')

# plt.figure(figsize=(12, 6))
# plt.xlabel('Time/m')
# plt.ylabel('DC Power/W')
# plt.title("DC Power Time Series(raw)")
# plt.plot(df.index, df['dc_power'])
# plt.savefig('figures/PV forecast/raw_DC Power Time Series.png')

# plt.figure(figsize=(12, 6))
# plt.xlabel('Time/m')
# plt.ylabel('Temperature/C')
# plt.title("Temperature Time Series(raw)")
# plt.plot(df.index, df['ambient_temp'])
# plt.savefig('figures/PV forecast/raw_Temperature Time Series.png')
# plt.show()

# plt.figure(figsize=(12, 6))
# plt.xlabel('Time/m')
# plt.ylabel('DC Power/W')
# plt.title("DC Power Time Series(filled)")
# plt.plot(df_filled.index, df_filled['dc_power'])
# plt.savefig('figures/PV forecast/filled_DC Power Time Series.png')

# plt.figure(figsize=(12, 6))
# plt.xlabel('Time/m')
# plt.ylabel('Temperature/C')
# plt.title("Temperature Time Series(filled)")
# plt.plot(df_filled.index, df_filled['ambient_temp'])
# plt.savefig('figures/PV forecast/filled_Temperature Time Series.png')
# plt.show()

# plt.figure(figsize=(12, 6))
# plt.xlabel('Time/m')
# plt.ylabel('DC Power/W')
# plt.title("DC Power Time Series(resampled)")
# plt.plot(df_resampled.index, df_resampled['dc_power'])
# plt.savefig('figures/PV forecast/resampled_DC Power Time Series.png')

# plt.figure(figsize=(12, 6))
# plt.xlabel('Time/m')
# plt.ylabel('Temperature/C')
# plt.title("Temperature Time Series(resampled)")
# plt.plot(df_resampled.index, df_resampled['ambient_temp'])
# plt.savefig('figures/PV forecast/resampled_Temperature Time Series.png')
# plt.show()
