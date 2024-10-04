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

    # Only set axis limits if data_stream is not empty
    if len(data_stream) > 0:
        plt.xlim(0, len(data_stream))  # Set x-axis limits to fit the entire data
        plt.ylim(min(data_stream) - 5, max(data_stream) + 5)  # Set y-axis limits based on data range
    else:
        plt.xlim(0, 50)  # Set default x-axis limits when no data is present
        plt.ylim(-10, 10)  # Set default y-axis limits when no data is present
    
    plt.legend()
    return line  # Return the line object for further updates

def update_plot(line, data_stream, anomalies=None):
    """Updates the plot with new data."""
    line.set_ydata(data_stream)  # Update the data for the line
    line.set_xdata(range(len(data_stream)))  # Update x-axis data

    # Update the x-axis to fit the current length of the data
    plt.xlim(0, len(data_stream))

    # Update y-axis limits dynamically based on the data range
    if len(data_stream) > 0:
        plt.ylim(min(data_stream) - 5, max(data_stream) + 5)

    # Plot anomalies if they exist
    if anomalies is not None and len(anomalies) > 0:
        anomaly_values = [data_stream[i] for i in anomalies]  # Extract the anomaly values
        plt.scatter(anomalies, anomaly_values, color='red', zorder=5)

    plt.draw()  # Redraw the updated plot

def close_plot():
    """Close the plot window properly."""
    plt.close()
