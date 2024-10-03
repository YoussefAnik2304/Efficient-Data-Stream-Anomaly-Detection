import numpy as np

def detect_anomalies(data_stream, threshold=2.5):
    """Detects anomalies in the data stream based on a simple threshold approach."""
    mean = np.mean(data_stream)
    std_dev = np.std(data_stream)
    
    anomalies = []
    for i, value in enumerate(data_stream):
        if abs(value - mean) > threshold * std_dev:
            anomalies.append(i)  # Flag the index as an anomaly
    
    return anomalies
