# visualization/__init__.py

__version__ = "0.1.0"
__author__ = "Your Name"
__description__ = "A package for visualizing data streams and anomalies."

# Importing key functions for easy access
from .stream_visualization import plot_anomalies , update_plot,close_plot

# Defining what should be accessible when using 'from visualization import *'
__all__ = [
    "plot_anomalies",
    "update_plot"
    "close_plot"
]

