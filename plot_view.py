import matplotlib.pyplot as plt

# Main function to plot the verification results
def plot_verification_results(verification_results, distances, distance_threshold):
    """
    Plots verification results including a pie chart for success/failure distribution
    and a scatter plot for face distances with a distance threshold line.

    Args:
        param verification_results (boolean): List of boolean values indicating verification success or failure

        param distances (int): List of distances between face pairs

        param distance_threshold (int): Threshold for face distance
    """
    plt.figure(figsize=(10, 5))

    # Plot pie chart for verification results
    plt.subplot(1, 2, 1)
    plot_pie_chart(verification_results)
    plt.title('Verification Results')

    # Plot scatter plot for face distances
    plt.subplot(1, 2, 2)
    plot_distance_scatter(distances, distance_threshold)
    plt.title('Face Distance for Each Pair')
    plt.xlabel('Pair Number')
    plt.ylabel('Face Distance')

    plt.tight_layout()
    plt.show()


# Helper functions to plot the pie chart and scatter plot
def plot_pie_chart(verification_results):
    success_count = verification_results.count(True)
    failure_count = verification_results.count(False)

    plt.pie([success_count, failure_count], labels=['Success', 'Failure'], explode=(0, 0.1),
            colors=['green', 'red'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), pctdistance=0.4)
    plt.gca().add_artist(plt.Circle((0, 0), 0.3, color='white'))

def plot_distance_scatter(distances, distance_threshold):
    plt.scatter(range(1, len(distances)+1), distances, color='blue')
    plt.axhline(y=distance_threshold, color='r', linestyle='--', label=f'Threshold ({distance_threshold})')
    plt.legend()