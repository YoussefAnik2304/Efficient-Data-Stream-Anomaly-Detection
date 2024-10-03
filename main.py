import numpy as np
import threading
import time
from anomaly_detection import continuous_data_stream, inject_anomalies, AnomalyDetector
from visualization import plot_anomalies, update_plot

# Initialize the anomaly detector
anomaly_detector = AnomalyDetector(threshold=15.0)

# Initialize lists to store data for plotting
data_points = []
anomaly_flags = []

# Function to generate data continuously
def generate_data(seasonal_period, seasonal_amplitude, noise_level):
    """
    Generates data continuously and injects anomalies into the stream.
    """
    for data_point in continuous_data_stream(seasonal_period, seasonal_amplitude, noise_level):
        # Introduce anomalies into the data point
        modified_data_point = inject_anomalies(data_point)

        # Check for anomalies
        is_anomaly = anomaly_detector.detect(modified_data_point)

        # Append the data point and its anomaly status to the lists
        data_points.append(modified_data_point)
        anomaly_flags.append(is_anomaly)

        # Wait for a second before generating the next data point
        time.sleep(1)

def main():
    # Start data generation in a separate thread
    threading.Thread(target=generate_data, args=(20, 10, 5), daemon=True).start()

    # Prepare the initial plot
    line = plot_anomalies(data_points, anomalies=[i for i, is_anomaly in enumerate(anomaly_flags) if is_anomaly])

    # Update the plot continuously
    while True:
        update_plot(line, data_points, anomalies=[i for i, is_anomaly in enumerate(anomaly_flags) if is_anomaly])
        time.sleep(0.2)  # Control the update frequency

if __name__ == "__main__":
    main()
