import numpy as np
import threading
import time
from anomaly_detection import continuous_data_stream, inject_anomalies, AnomalyDetector
from visualization import plot_anomalies, update_plot, close_plot
import matplotlib.pyplot as plt

# Initialize the anomaly detector
anomaly_detector = AnomalyDetector(threshold=15.0)

# Initialize lists to store data for plotting (with a rolling window of size 50)
data_points = []
anomaly_flags = []
MAX_DATA_POINTS = 50  # Rolling window size for visualization

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

        # Keep only the last MAX_DATA_POINTS data points
        if len(data_points) > MAX_DATA_POINTS:
            data_points.pop(0)
            anomaly_flags.pop(0)

        # Wait for a second before generating the next data point
        time.sleep(1)

def main():
    # Start data generation in a separate thread
    threading.Thread(target=generate_data, args=(20, 10, 5), daemon=True).start()

    # Prepare the initial plot and get line, scatter, and axis references
    line, scatter, ax = plot_anomalies(data_points, anomalies=[i for i, is_anomaly in enumerate(anomaly_flags) if is_anomaly])

    # Use plt.show(block=False) to keep the plot window interactive but non-blocking
    plt.show(block=False)

    # Update the plot continuously, handle graceful shutdown of the plot window
    try:
        while plt.fignum_exists(1):  # Check if the plot window is still open
            scatter = update_plot(line, scatter, ax, data_points, anomalies=[i for i, is_anomaly in enumerate(anomaly_flags) if is_anomaly])
            plt.pause(0.5)  # Pause for plot updates
    except KeyboardInterrupt:
        print("Plotting interrupted by user.")
    finally:
        close_plot()  # Ensure the plot is properly closed on exit

if __name__ == "__main__":
    main()
