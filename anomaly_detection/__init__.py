# anomaly_detection/__init__.py

__version__ = "0.1.0"
__author__ = "Your Name"
__description__ = "A package for efficient data stream anomaly detection."

# Importing key functions and classes for easy access
from .stream_simulation import continuous_data_stream
from .anomaly_injection import inject_anomalies
from .detection_algorithm import AnomalyDetector

# Defining what should be accessible when using 'from anomaly_detection import *'
__all__ = [
    "continuous_data_stream",
    "inject_anomalies",
    "AnomalyDetector",
]
