import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# read data
df = pd.read_csv('data/raw_pvdaq/pvdaq_2012_2014_15min.csv', header=0, infer_datetime_format=True, parse_dates=['Date-Time'], index_col=['Date-Time'])

features = ['ambient_temp', 'inverter_temp', 'module_temp', 'poa_irradiance', 'relative_humidity', 'wind_direction', 'wind_speed']
# features = ['ambient_temp', 'inverter_temp', 'module_temp', 'poa_irradiance']
target = ['dc_power']
time_indexes = [df.index.hour, df.index.month]
time_indexes

# feature columns stacking
data = []
for feature in features:
  feature_col = df[feature].values.reshape(-1, 1)
  data.append(feature_col)
for index in time_indexes:
  index_col = index.values.reshape(-1, 1)
  data.append(index_col)
data.append(np.maximum(df[target].values.reshape(-1,1),0))
data = np.hstack((data))

n_data = np.size(data,0) # 26304
n_feature = len(features) # 7
index = data[:,n_feature:n_feature+2]
X = data[:,0:n_feature]
y = data[:,-1]
X, y

pred_15min=200
X_train, y_train, index_train = X[:-pred_15min,:], y[:-pred_15min], df.index[:-pred_15min]
X_test, y_test, index_test = X[-pred_15min:,:], y[-pred_15min:], df.index[-pred_15min:]

# X_train, X_test, y_train, y_test, index_train, index_test = train_test_split(X, y, df.index,test_size=0.05)
lrmodel = LinearRegression()
lrmodel.fit(X_train, y_train)
y_pred = lrmodel.predict(X_test)
y_pred = np.maximum(y_pred,0)
# 评估模型性能

print(f"mean_square_error:{mean_squared_error(y_test,y_pred)}")
print(f'r2_score: {r2_score(y_test, y_pred)}')

plt.figure(figsize=(30, 6))
plt.xlabel('Time/m')
plt.ylabel('DC Power/W')
plt.title("DC Power Prediction(LinearRegression)")
plt.plot(index_train[-1000:], y_train[-1000:],label='train(not all)')
plt.plot(index_test, y_test,label='test')
plt.plot(index_test, y_pred,label='pred')
plt.legend()
plt.savefig('figures/PV forecast/DC Power Prediction(LinearRegression 15min).png')
plt.show()


df_train = pd.DataFrame({'index_train': index_train , 'y_train': y_train})
df_test = pd.DataFrame({'index_test': index_test,'y_test': y_test})
df_pred = pd.DataFrame({'index_test': index_test, 'y_pred':y_pred})
df_train.to_csv('data/PV_and_wind/train.csv', index=False)
df_test.to_csv('data/PV_and_wind/test.csv', index=False)
df_pred.to_csv('data/PV_and_wind/pred.csv', index=False)