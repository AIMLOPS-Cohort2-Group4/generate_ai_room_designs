import os
import ollama
import json

project_root_path = os.getenv("PROJECT_ROOT_PATH")
annotations_ikea_file_path = "data/annotations/annotations_ikea.json"
annotations_from_llm_file_path = "data/annotations/annotations_from_llm.json"

with open(os.path.join(project_root_path, annotations_ikea_file_path), 'r') as f:
    data = json.load(f)
    llm_generated_descriptions = []
    
    for item in data[0:2]:
        description = item["desc"]
        
        prompt = f"""You are given an output from image captioning model describing the contents of an Ikea product. Given this output, try to generate a caption for it. 
        Description: 
        { description } 

        Following are the guidelines to generate the capiton: 
        1. should be expletive free. 
        2. should be in direct person. 
        3. short and effective (DO NOT TRY TO ELABORATE THE CONTENTS AGAIN).

        Output should be a single line containing Product, Features of the Product, Color and Materials and Purpose."""

        llm_response = ollama.generate(model='mistral', prompt=prompt)
    
        llm_generated_descriptions.append({
            "file_name" : item["file_name"],
            "desc" : llm_response['response']
        })

f.close()


with open(os.path.join(project_root_path, annotations_from_llm_file_path), 'w') as annotations_file:
    json.dump(llm_generated_descriptions, annotations_file, indent=4)

print(f"Annotations file created at: {os.path.join(project_root_path, annotations_from_llm_file_path)}")