from PIL import Image
import os

# Root folder containing images and subfolders
root_folder = "input_folder"

# Output folder where cropped images will be saved
output_folder = "output_folder"

# Height to be cropped from the top and bottom (870px in this case)
crop_height = 870

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def crop_image(file_path):
    # Open the image
    image = Image.open(file_path)

    # Get the dimensions of the image
    width, height = image.size

    # Calculate new dimensions after cropping
    new_height = height - 2 * crop_height

    # Crop the image
    cropped_image = image.crop((0, crop_height, width, height - crop_height))

    # Save the cropped image to the output folder
    output_path = os.path.join(output_folder, os.path.relpath(file_path, root_folder))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cropped_image.save(output_path)

    print(f"Cropped: {file_path}")

# Recursively traverse through the directory structure
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(foldername, filename)
            crop_image(file_path)

print("Batch cropping completed.")