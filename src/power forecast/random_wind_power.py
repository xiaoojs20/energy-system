import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

num15min = 200
# 生成 Weibull 分布的数据
k = 2.2
lambd = 8
weibull_data = np.random.weibull(k, num15min) * lambd

vci = 2.5 #m/s
vN = 12
vco = 25
PN = 50000 # W
wind_speed = abs(weibull_data)
wind_power = wind_speed.copy()
for i in range(len(wind_speed)):
    if 0 <= wind_speed[i] <= vci:
        wind_power[i] = 0
    elif vci < wind_speed[i] <= vN:
        wind_power[i] = PN*(wind_speed[i]**3-vci**3)/(vN**3-vci**3)
    elif vN < wind_speed[i] <= vco:
        wind_power[i] = PN
    elif vN > vco:
        wind_power[i] = 0

df_test = pd.read_csv('data/PV_and_wind/test.csv', header=0, infer_datetime_format=True, parse_dates=['index_test'], index_col=['index_test'])
df_pred = pd.read_csv('data/PV_and_wind/pred.csv', header=0, infer_datetime_format=True, parse_dates=['index_test'], index_col=['index_test'])
df_test['wind power'] = wind_power
df_pred['wind power'] = wind_power
df_test['total DC power'] = df_test['y_test'] + df_test['wind power']
df_pred['total DC power'] = df_pred['y_pred'] + df_pred['wind power']
df_test.to_csv('data/PV_and_wind/test_PV_and_wind.csv')
df_pred.to_csv('data/PV_and_wind/pred_PV_and_wind.csv')

# 绘制图像
fig = plt.figure(figsize=(12, 6))

plt.subplot(211)
plt.xlabel('Time/(per 15min)')
plt.ylabel('Wind Power/W')
plt.title('Wind Speed/(m/s)')
plt.plot(df_test.index, wind_speed)
 
plt.subplot(212)
plt.xlabel('Time/(per 15min)')
plt.ylabel('Wind Power/W')
plt.title('Wind Power')
plt.plot(df_test.index, wind_power)

fig.tight_layout()
plt.savefig('figures/PV forecast/wind speed and power.png')
plt.show()


# plt.xlabel('Time/(per 15min)')
# plt.ylabel('PV Power/W')
# plt.title("PV Power Prediction")
# plt.plot(df_test.index, df_test.y_test,label='test')
# plt.plot(df_test.index, df_pred.y_pred,label='pred')
# plt.legend()

plt.figure(figsize=(12, 6))
plt.xlabel('Time/(per 15min)')
plt.ylabel('DC Power/W')
plt.title("DC Power (PV + wind)")
plt.plot(df_test.index, df_test.y_test + wind_power,label='test')
plt.plot(df_test.index, df_pred.y_pred + wind_power,label='pred')
plt.legend()

plt.savefig('figures/PV forecast/PV+wind(15min).png')
plt.show()



