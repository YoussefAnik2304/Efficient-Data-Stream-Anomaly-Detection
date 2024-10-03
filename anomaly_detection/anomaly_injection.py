import numpy as np

def inject_anomalies(data_point: float) -> float:
    """
    Introduces an anomaly into the data stream based on some condition.

    :param data_point: The original data point from the stream.
    :return: The modified data point with an anomaly introduced.
    """
    # Example condition to introduce an anomaly
    if np.random.rand() < 0.1:  # 10% chance to introduce an anomaly
        # Introduce an anomaly by adding a large deviation
        anomaly_magnitude = np.random.uniform(10, 20)  # Random anomaly value
        return data_point + anomaly_magnitude
    return data_point
