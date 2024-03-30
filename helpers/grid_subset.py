import os
import argparse
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
            filepath = os.path.join(folder_path, filename)
            images.append(mpimg.imread(filepath))
    return images

def create_subplot_grid(images):
    num_images = len(images)
    num_cols = math.floor(math.sqrt(num_images))
    num_rows = (num_images + num_cols - 1) // num_cols

    fig, axarr = plt.subplots(num_rows, num_cols, figsize=(num_cols * 5, num_rows * 5))

    # Flatten the axarr if it's not already flat (for handling single row case)
    if not isinstance(axarr, (list, np.ndarray)):
        axarr = [axarr]

    for ax_row in axarr:
        for ax in ax_row:
            ax.axis('off')

    for i, img in enumerate(images):
        row = i // num_cols
        col = i % num_cols
        axarr[row, col].imshow(img)

    return fig

def save_subplot_grid(fig, output_path):
    fig.savefig(output_path)
    plt.close(fig)

def main():
    parser = argparse.ArgumentParser(description='Create a grid of images from a folder.')
    parser.add_argument('-s', '--source', required=True, help='Source directory path')
    args = parser.parse_args()

    source_folder = args.source
    output_path = "subset-grid.png"

    images = load_images(source_folder)
    if images:
        subplot_grid = create_subplot_grid(images)
        save_subplot_grid(subplot_grid, output_path)
        print(f"Subset grid saved to {output_path}")
    else:
        print("No images found in the specified directory.")

if __name__ == "__main__":
    main()