import numpy as np

def simulate_data_stream(num_points=1000, seasonal_period=50, seasonal_amplitude=10, noise_level=5):
    """
    Simulate a data stream with regular patterns, seasonal elements, and random noise.

    Parameters:
    - num_points: Number of data points to generate.
    - seasonal_period: The period of the seasonal component.
    - seasonal_amplitude: Amplitude of the seasonal fluctuations.
    - noise_level: Standard deviation of the random noise.

    Returns:
    - A numpy array representing the simulated data stream.
    """
    
    # Time array for the simulation
    time = np.arange(num_points)

    # Regular pattern (e.g., linear trend)
    regular_pattern = 0.05 * time  # Linear trend

    # Seasonal pattern (e.g., sine wave)
    seasonal_pattern = seasonal_amplitude * np.sin(2 * np.pi * time / seasonal_period)

    # Random noise
    noise = np.random.normal(0, noise_level, num_points)

    # Combine all components to create the final data stream
    data_stream = regular_pattern + seasonal_pattern + noise

    return data_stream
