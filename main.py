import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import ThresholdAD, QuantileAD, InterQuartileRangeAD, GeneralizedESDTestAD, PersistAD, VolatilityShiftAD, CustomizedDetectorHD

# Load and preprocess data
s_train = pd.read_csv("temperature.csv", parse_dates=True)
s_train["Date"] = pd.to_datetime(s_train["Date"])
s_train = s_train.set_index("Date")
s_train = s_train['Mean']

# Validate the series
s_train = validate_series(s_train)
# Change to a different style before calling the plot

# Plot the data
# plot(s_train)
# plt.show()


#Threshold Anomaly Detection (manually define min max threshold)
threshold_ad = ThresholdAD(high=0.75, low=-0.5)
anomalies = threshold_ad.detect(s_train)
plot(s_train, anomaly=anomalies, anomaly_color="blue", anomaly_tag="marker")
plt.show()

# # Quantile Anomaly Detection (manually define percentiles)
# quantile_ad = QuantileAD(high=0.99, low=0.01)
# anomalies = quantile_ad.fit_detect(s_train)
# plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='blue', anomaly_tag="marker")
# plt.show()

# # Inter Quartile Range Anomaly Detection (IQR = Q3 - Q1, with c we multiply for tolerance, so c * IQR)
# iqr_ad = InterQuartileRangeAD(c=1.5)
# anomalies = iqr_ad.fit_detect(s_train)
# plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='blue', anomaly_tag="marker")
# plt.show()

# # Generalized Extreme Studentized Deviate (ESD) Test (assumes normal distribution, only use when this assumption makes sense)
# esd_ad = GeneralizedESDTestAD(alpha=1)
# anomalies = esd_ad.fit_detect(s_train)
# plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='blue', anomaly_tag="marker")
# plt.show()


