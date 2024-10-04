import numpy as np
import matplotlib.pyplot as plt

# Data Generation
def continuous_data_stream(n_points=100, amplitude=10, noise_level=3):
    """
    Generate a data stream with regular, seasonal, and random components.
    
    Args:
    - n_points (int): Number of data points.
    - amplitude (float): Amplitude for the seasonal sine wave.
    - noise_level (float): Standard deviation for the random noise.
    
    Returns:
    - np.array: Generated data stream.
    """
    # Time points
    t = np.arange(0, n_points)
    
    # Regular component (linear trend or constant)
    regular_component = 0.05 * t
    
    # Seasonal component (sine wave to represent cycles)
    seasonal_component = amplitude * np.sin(2 * np.pi * t / 20)  # 20-point cycle
    
    # Random component (noise)
    random_component = np.random.normal(0, noise_level, n_points)
    
    # Final data stream
    data_stream = regular_component + seasonal_component + random_component
    return data_stream
