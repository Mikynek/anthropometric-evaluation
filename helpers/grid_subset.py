import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import numpy as np

def combine_images(folder_path, output_path):
    images = []
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filepath = os.path.join(folder_path, filename)
            
            # Read the image and append it to the list
            images.append(mpimg.imread(filepath))
    
    # Determine the number of images
    num_images = len(images)
    
    # Calculate number of rows and columns for subplots
    num_cols = 5
    num_rows = (num_images + num_cols - 1) // num_cols  # Ceiling division to ensure we have enough rows
    
    # Create subplots with correct number of rows and columns
    fig, axarr = plt.subplots(num_rows, num_cols, figsize=(num_cols * 5, num_rows * 5))
    
    # Flatten the axarr if it's not already flat (for handling single row case)
    if not isinstance(axarr, (list, np.ndarray)):
        axarr = [axarr]
    
    # Disable axis for all subplots
    for ax_row in axarr:
        for ax in ax_row:
            ax.axis('off')
    
    # Display each image in its subplot
    for i, img in enumerate(images):
        row = i // num_cols
        col = i % num_cols
        axarr[row, col].imshow(img)
    
    # Save the combined image
    plt.savefig(output_path)
    
    # Display the combined image
    plt.show()

# Example usage:
input_folder = "real-data"
output_image = "subset-grid.png"
combine_images(input_folder, output_image)