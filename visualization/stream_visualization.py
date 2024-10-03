import matplotlib.pyplot as plt

def plot_anomalies(data_stream, anomalies=None):
    """Visualizes the data stream with detected anomalies."""
    plt.ion()  # Enable interactive mode
    plt.figure(figsize=(10, 6))
    
    # Initialize the plot
    line, = plt.plot(data_stream, label='Data Stream', color='blue')

    # Plot anomalies if they exist
    if anomalies is not None and len(anomalies) > 0:
        anomaly_values = [data_stream[i] for i in anomalies]  # Extract the anomaly values
        plt.scatter(anomalies, anomaly_values, color='red', label='Anomalies', zorder=5)

    plt.title('Data Stream with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()

    plt.xlim(0, 50)  # Set initial x-axis limits
    plt.ylim(-30, 30)  # Set y-axis limits to fixed range
    return line  # Return the line object for further updates

def update_plot(line, data_stream, anomalies=None):
    """Updates the plot with new data."""
    line.set_ydata(data_stream)  # Update the data for the line
    line.set_xdata(range(len(data_stream)))  # Update x-axis data

    # Center the plot around the last data points
    if len(data_stream) > 100:  # If we have more than 100 data points
        plt.xlim(len(data_stream) - 50, len(data_stream))  # Show the last 100 points
    else:
        plt.xlim(0, 50)  # Keep the limits if there are less than 100 points

    # Update the y-axis limits if not set already
    plt.ylim(-30, 30)  # Keep y-axis limits fixed between 0 and 200

    # Plot anomalies if they exist
    if anomalies is not None and len(anomalies) > 0:
        anomaly_values = [data_stream[i] for i in anomalies]  # Extract the anomaly values
        plt.scatter(anomalies, anomaly_values, color='red', label='Anomalies', zorder=5)

    plt.draw()  # Redraw the updated plot
    plt.pause(0.1)  # Pause to allow for the plot to update
