import os
import zipfile
from PIL import Image
import numpy as np
from alive_progress import alive_bar
import time

# Define paths
images_path = './data/extracted_data/ikea-master/images/'
save_path = './data/extracted_data/ikea_processed_data/images/'

# Create save_path if it does not exist
os.makedirs(save_path,exist_ok=True)

# Define traget size 
target_size = (512,512)

def preprocess_image(image_path,target_size):

    # Method to preprocess each frame in the dataset
    # Arguments: path to image folder 
    # Process: Reads frames and convert them to RGB, resize image to the target size

    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize(target_size)
        return img
    

def save_preprocessed_image(img, image_name, save_path):

    # Method to save preprocessed frames
    # Arguments: frame read, file name without the file extension, path to save the frame
    # Process: saving the read image file

    os.makedirs(save_path,exist_ok=True)
    img.save(os.path.join(save_path, image_name+'.jpg'))

# Main Function

categories = os.listdir(images_path)
for category in categories:
    with alive_bar(len(os.listdir(os.path.join(images_path,category)))) as bar:
        for images in os.listdir(os.path.join(images_path,category)):
            image_path = os.path.join(images_path,category,images)
            img = preprocess_image(image_path,target_size)
            image_file = images.split('.jp')[0]
            save_preprocessed_image(img, image_file, save_path)
            time.sleep(.001)
            bar()
