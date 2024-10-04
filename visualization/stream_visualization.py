import matplotlib.pyplot as plt

def plot_anomalies(data_stream, anomalies=None):
    """Visualizes the data stream with detected anomalies."""
    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots(figsize=(10, 6))  # Use subplots to manage the figure and axes separately
    
    # Initialize the main line plot
    line, = ax.plot(data_stream, label='Data Stream', color='blue')

    # Plot initial anomalies if they exist
    scatter = None
    if anomalies is not None and len(anomalies) > 0:
        anomaly_values = [data_stream[i] for i in anomalies]  # Extract the anomaly values
        scatter = ax.scatter(anomalies, anomaly_values, color='red', label='Anomalies', zorder=5)

    ax.set_title('Data Stream with Anomalies')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

    # Only set axis limits if data_stream is not empty
    if len(data_stream) > 0:
        ax.set_xlim(0, len(data_stream))  # Set x-axis limits to fit the entire data
        ax.set_ylim(min(data_stream) - 5, max(data_stream) + 5)  # Set y-axis limits based on data range
    else:
        ax.set_xlim(0, 50)  # Set default x-axis limits when no data is present
        ax.set_ylim(-10, 10)  # Set default y-axis limits when no data is present
    
    ax.legend()
    return line, scatter, ax  # Return the line and scatter objects for further updates

def update_plot(line, scatter, ax, data_stream, anomalies=None):
    """Updates the plot with new data."""
    line.set_ydata(data_stream)  # Update the data for the line
    line.set_xdata(range(len(data_stream)))  # Update x-axis data

    # Update the x-axis to fit the current length of the data
    ax.set_xlim(0, len(data_stream))

    # Update y-axis limits dynamically based on the data range
    if len(data_stream) > 0:
        ax.set_ylim(min(data_stream) - 5, max(data_stream) + 5)

    # Update anomalies (remove old scatter plot if it exists)
    if scatter:
        scatter.remove()  # Remove the previous scatter plot to avoid overlap

    # Plot new anomalies if they exist
    if anomalies is not None and len(anomalies) > 0:
        anomaly_values = [data_stream[i] for i in anomalies]  # Extract the anomaly values
        scatter = ax.scatter(anomalies, anomaly_values, color='red', label='Anomalies', zorder=5)

    # Dynamically update the legend
    ax.legend()
    plt.draw()  # Redraw the updated plot

    # Return the new scatter plot object for further updates
    return scatter

def close_plot():
    """Close the plot window properly."""
    plt.close()
