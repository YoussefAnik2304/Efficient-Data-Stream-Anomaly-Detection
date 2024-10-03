import numpy as np

def introduce_anomalies_in_stream(data_stream, num_anomalies=5):
    """Introduces various anomaly types (point, contextual, collective) into the data stream."""
    data = data_stream.copy()  # Copy the data to avoid mutating the original stream
    anomaly_indices = np.random.choice(len(data_stream), num_anomalies, replace=False)

    for i in anomaly_indices:
        anomaly_type = np.random.choice(['point', 'contextual', 'collective'], p=[0.6, 0.3, 0.1])
        
        if anomaly_type == 'point':
            spike = np.random.uniform(5, 10) * np.random.choice([-1, 1])
            data[i] += spike
        
        elif anomaly_type == 'contextual':
            context_window = np.random.randint(5, 10)
            start = max(0, i - context_window)
            end = min(len(data), i + context_window)
            context_shift = np.random.uniform(2, 5) * np.random.choice([-1, 1])
            data[start:end] += context_shift
        
        elif anomaly_type == 'collective':
            collective_size = np.random.randint(3, 7)
            collective_indices = np.arange(i, min(i + collective_size, len(data)))
            collective_deviation = np.random.uniform(2, 4) * np.random.choice([-1, 1])
            data[collective_indices] += collective_deviation
    
    return data
