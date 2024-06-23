## Method to finally create one json 
import os
import json
import argparse

path_json_files = os.getenv("PROJECT_ROOT_PATH")


# Loading json files

# path_json_files = '/Users/samankhan/Documents/capstone_project/Github_project/generate_ai_room_designs/data/extracted_data/ikea_processed_data/'

def combine_descriptions(file_name):

    # Method to combined items from each preprocessed json file
    # Input: file_name is the name of the image file being considered
    
    descriptions = []
    for data in [categories_images,annotations_main,img_to_desc, products_dict]:
        for item in data:
            if item['file_name'] == file_name:
                if (len(item['desc']) > 0) & (item['desc'].lower() != 'no description'):
                    if item['desc'] not in descriptions:
                        descriptions.append(item['desc'])
    list(set(descriptions))

    return ". ".join(descriptions).replace('..','.')



## main function
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description= 'Script to merge the description for images genertaed by BLIP and provided by Ikea '
    )
    
    parser.add_argument(
        "--caption_generated",
        type = str,
        help = 'the path for BLIP generated cations in json file',
        default = 'data/annotations/annotations.json'
    )
    parser.add_argument(
        "--ikea_category_img_dict",
        type = str,
        help = 'path to preprocessed categories_images dict json file',
        default = 'data/pickle_processed/categories_images_dict.json'

    )
    parser.add_argument(
        "--ikea_img_desc_dict",
        type = str,
        help = 'path to preprocessed img to desc json',
        default = 'data/pickle_processed/img_to_desc.json'

    )
    parser.add_argument(
        "--ikea_products_dict",
        type = str,
        help = 'path to preprocessed product dict json',
        default = 'data/pickle_processed/products_dict.json'
    )
    parser.add_argument(
        "--path_to_images",
        type = str,
        help = 'path to all the images',
        default = 'data/images/'
    )

    # Read argumnets
    args = parser.parse_args()
    # data_path = args.data_path
    caption_generated = args.caption_generated
    ikea_category_img_dict = args.ikea_category_img_dict
    ikea_img_desc_dict = args.ikea_img_desc_dict
    ikea_products_dict = args.ikea_products_dict
    path_to_images = args.path_to_images


    # Reading the mentioned json files:
    with open(os.path.join(path_json_files,caption_generated)) as f:
        annotations_main = json.load(f)
    

    with open(os.path.join(path_json_files,ikea_category_img_dict)) as f:
        categories_images = json.load(f)

    with open(os.path.join(path_json_files,ikea_img_desc_dict)) as f:
        img_to_desc = json.load(f)

    with open(os.path.join(path_json_files,ikea_products_dict)) as f:
        products_dict = json.load(f)
    

    combined_desc = []
    all_file_names = os.listdir(os.path.join(path_json_files,path_to_images))
    for file_name in all_file_names:
        combined_desc.append({
            "file_name" : file_name,
            "desc" : combine_descriptions(file_name)
        })
    print(combined_desc)

    with open(os.path.join(path_json_files,'data/annotations/annotations_ikea.json'), 'w') as annotations_file:
        json.dump(combined_desc, annotations_file, indent=4)

    print(f"Annotations file created at: {os.path.join(path_json_files,'data/annotations/annotations_ikea.json')}")





