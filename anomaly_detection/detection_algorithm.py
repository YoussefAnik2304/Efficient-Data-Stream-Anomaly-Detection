class AnomalyDetector:
    def __init__(self, threshold: float = 15.0):
        """
        Initializes the anomaly detector with a specified threshold.

        :param threshold: The threshold value for detecting anomalies.
        """
        self.threshold = threshold

    def detect(self, data_point: float) -> bool:
        """
        Detects if the given data point is an anomaly.

        :param data_point: The data point to check for anomalies.
        :return: True if the data point is an anomaly, False otherwise.
        """
        return abs(data_point) > self.threshold  # Adjust based on your criteria
