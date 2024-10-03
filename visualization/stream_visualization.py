import matplotlib.pyplot as plt

def plot_anomalies(data_stream, anomalies=None):
    """Visualizes the data stream with detected anomalies."""
    plt.figure(figsize=(10, 6))
    plt.plot(data_stream, label='Data Stream', color='blue')
    
    if anomalies is not None:
        plt.scatter(anomalies, data_stream[anomalies], color='red', label='Anomalies', zorder=5)
    
    plt.title('Data Stream with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
