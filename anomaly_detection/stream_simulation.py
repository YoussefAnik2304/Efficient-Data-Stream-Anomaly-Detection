import numpy as np
import time

def continuous_data_stream(seasonal_period: int, seasonal_amplitude: float, noise_level: float):
    """
    Generates a continuous data stream with seasonal patterns and noise.

    :param seasonal_period: The period of the seasonal component.
    :param seasonal_amplitude: The amplitude of the seasonal component.
    :param noise_level: The standard deviation of the noise to be added.
    :yield: A new data point continuously.
    """
    time_elapsed = 0
    while True:
        # Generate seasonal component
        seasonal_component = seasonal_amplitude * np.sin(2 * np.pi * time_elapsed / seasonal_period)
        
        # Generate noise
        noise = np.random.normal(0, noise_level)
        
        # Generate the final data point
        data_point = seasonal_component + noise
        yield data_point

        # Sleep for 1 second to simulate real-time data generation
        time.sleep(0.2)
