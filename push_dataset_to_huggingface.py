import os
from datasets import load_dataset

# Set this environment variable in you local
project_root_path = os.environ["PROJECT_ROOT_PATH"]

dataset = load_dataset(project_root_path + '/create_dataset.py', data_files=project_root_path + '/data/annotations/annotations_from_llm.json')

#change this to your HF Org 
dataset.push_to_hub("nbadrinath/ikea_dataset_4.0")
