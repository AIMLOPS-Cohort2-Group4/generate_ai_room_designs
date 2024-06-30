import os
from datasets import load_dataset

# Set this environment variable in you local
project_root_path = os.getenv("PROJECT_ROOT_PATH")
hugging_face_user = os.getenv("HUGGING_FACE_USERNAME")

dataset = load_dataset(project_root_path + '/create_dataset.py',project_root_path+'datasets/train/annotations/annotations.json')

#change this to your HF Org 
dataset.push_to_hub(hugging_face_user + "/ikea_dataset_2.0")
# print(dataset["train"][0])
# print(dataset["test"][0])
# print(dataset["validation"][0])
