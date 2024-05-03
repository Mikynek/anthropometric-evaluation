import matplotlib.pyplot as plt
import numpy as np

# Main function to plot the verification results
def plot_verification_results(verification_results, distances, distance_threshold, save_locally=False):
    """
    Plots verification results including a pie chart for success/failure distribution
    and a scatter plot for face distances with a distance threshold line.

    Args:
        param verification_results (list of boolean): List of boolean values indicating verification success or failure

        param distances (list of int): List of distances between face pairs

        param distance_threshold (int): Threshold for face distance

        param save_locally (bool, optional): Flag to save the plots locally or display inline
    """
    if save_locally:
        plot_and_save(verification_results, distances, distance_threshold)
    else:
        plot_inline(verification_results, distances, distance_threshold)

def plot_and_save(verification_results, distances, distance_threshold):
    plt.figure(figsize=(8, 6))
    _plot_pie_chart(verification_results)
    plt.title('Verification Results')
    plt.savefig("legacy/deepface_verification_results.png")
    plt.close()

    plt.figure(figsize=(15, 8))
    _plot_distance_scatter(distances, distance_threshold)
    plt.title('Cosine Distance for Each Pair', fontsize=18)
    plt.xlabel('Pair Index', fontsize=16)
    plt.ylabel('Cosine Distance', fontsize=16)
    plt.tight_layout()
    plt.savefig("legacy/deepface_face_distances.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    _plot_distance_histogram(distances)
    plt.xlabel('Distance')
    plt.ylabel('Count')
    plt.title(f'Histogram of Distances')
    plt.savefig("legacy/deepface_distance_histogram.png")


def plot_inline(verification_results, distances, distance_threshold):
    plt.figure(figsize=(20, 8))

    plt.subplot(1, 1, 1)
    _plot_pie_chart(verification_results)
    plt.title('Verification Results')

    plt.subplot(1, 3, 2)
    _plot_distance_scatter(distances, distance_threshold)
    plt.title('Face Distance for Each Pair')
    plt.xlabel('Pair Index', fontsize=18)
    plt.ylabel('Cosine Distance', fontsize=18)

    plt.tight_layout()
    plt.show()


# Helper functions to plot the pie chart, scatter plot and histogram
def _plot_pie_chart(verification_results):
    success_count = verification_results.count(True)
    failure_count = verification_results.count(False)

    plt.pie([success_count, failure_count], labels=['Success', 'Failure'], explode=(0, 0.1),
            colors=['green', 'red'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), pctdistance=0.4)
    plt.gca().add_artist(plt.Circle((0, 0), 0.3, color='white'))

def _plot_distance_scatter(distances, distance_threshold):
    plt.scatter(range(1, len(distances)+1), distances, color='blue')
    plt.axhline(y=distance_threshold, color='r', linestyle='--', label=f'Threshold ({distance_threshold})')
    plt.legend(fontsize=12)

def _plot_distance_histogram(distances, interval=0.1):
    min_distance = np.floor(min(distances) / interval) * interval
    max_distance = max(distances)
    bins = np.arange(min_distance, max_distance + interval, interval)

    colormap = plt.cm.viridis(np.linspace(0, 1, len(bins) - 1))
    n, bins, patches = plt.hist(distances, bins=bins, edgecolor='black')

    # Assign different colors to each bin
    for color, patch in zip(colormap, patches):
        patch.set_facecolor(color)
    
    # Calculate percentages for each bin
    percentages = (n / len(distances)) * 100
    
    # Add percentage labels to each bar
    for i, percentage in enumerate(percentages):
        midpoint = (bins[i] + bins[i + 1]) / 2
        plt.text(midpoint, n[i], f'{percentage:.2f}%', ha='center', va='bottom')
