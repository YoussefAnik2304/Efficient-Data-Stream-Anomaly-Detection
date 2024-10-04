# Anomaly Detection in Time Series Data

This Python script demonstrates various anomaly detection techniques on time series data using the ADTK (Anomaly Detection Toolkit) library. The script includes examples of different anomaly detection algorithms applied to temperature data and stock price data.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the Code](#running-the-code)
4. [Anomaly Detection Techniques](#anomaly-detection-techniques)
5. [Data](#data)

## Prerequisites

- Python 3.6+
- pip (Python package installer)
- Basic understanding of time series data and anomaly detection concepts

## Installation

1. Clone this repository or download the script and requirements file.
2. Navigate to the project directory:
   ```
   cd path/to/project/directory
   ```
3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

## Running the Code

To run the anomaly detection script, follow these steps:

1. Ensure you have completed the installation steps above and your data file ("temperature.csv") is in the correct location.

2. In the terminal or command prompt, make sure you're in the project directory.

3. Run the script using Python:
   ```
   python main.py
   ```

4. The script will execute and display plots for each anomaly detection technique. Close each plot window to proceed to the next technique.

5. To run specific sections of the code, you can uncomment the relevant parts in `main.py` before running it. For example, to run the Quantile Anomaly Detection:
   ```python
   # Uncomment these lines in main.py
   quantile_ad = QuantileAD(high=0.99, low=0.01)
   anomalies = quantile_ad.fit_detect(s_train)
   plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='blue', anomaly_tag="marker")
   plt.show()
   ```

6. Save the changes to `main.py` and run it again as described in step 3.

Remember to check the console output for any error messages or warnings during execution.

## Anomaly Detection Techniques

The script demonstrates the following anomaly detection techniques:

1. **Threshold Anomaly Detection**: Detects anomalies based on predefined high and low thresholds.
2. **Quantile Anomaly Detection**: Identifies anomalies using specified percentiles of the data.
3. **Inter Quartile Range (IQR) Anomaly Detection**: Detects anomalies based on the interquartile range.
4. **Generalized Extreme Studentized Deviate (ESD) Test**: Assumes normal distribution and detects anomalies accordingly.
5. **Persist Anomaly Detection**: Compares each value with the previous one to detect changes.
6. **Volatility Shift Anomaly Detection**: Detects changes in the volatility of the time series (demonstrated on stock price data).

To use different techniques, uncomment the relevant sections in the script.

## Data

The script uses two types of data:

1. Temperature data: Loaded from a local CSV file ("temperature.csv").
2. Stock price data: Downloaded using the yfinance library (for the Volatility Shift Anomaly Detection example).

Ensure that your "temperature.csv" file has the correct format and contains the required columns ("Date" and "Mean" at minimum).
