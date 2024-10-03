# main.py

from anomaly_detection import simulate_data_stream, introduce_anomalies_in_stream, detect_anomalies
from visualization import plot_anomalies

def main():
    # Step 1: Simulate data stream
    data_stream = simulate_data_stream(num_points=1000, seasonal_period=10, seasonal_amplitude=10, noise_level=50)

    # Step 2: Introduce anomalies into the data stream
    data_with_anomalies = introduce_anomalies_in_stream(data_stream, num_anomalies=10)

    # Step 3: Detect anomalies
    detected_anomalies = detect_anomalies(data_with_anomalies)

    # Step 4: Visualize the data stream and detected anomalies
    plot_anomalies(data_with_anomalies, detected_anomalies)

if __name__ == "__main__":
    main()
