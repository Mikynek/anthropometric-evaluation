import matplotlib.pyplot as plt

# Main function to plot the verification results
def plot_verification_results(verification_results, distances, distance_threshold):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plot_pie_chart(verification_results)
    plt.title('Verification Results')

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