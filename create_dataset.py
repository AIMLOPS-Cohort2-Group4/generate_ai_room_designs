import os
import pickle

text_data_path = 'text_data'

def load_pickle_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

pickle_files = [f for f in os.listdir(text_data_path) if f.endswith('.p')]
data = {}

for pickle_file in pickle_files:
    file_path = os.path.join(text_data_path, pickle_file)
    data[pickle_file] = load_pickle_file(file_path)
    file_to_create = "hf_data/" + pickle_file.replace(".p", ".csv")

    if not os.path.exists(file_to_create): 
        f = open(file_to_create, "x")
        f.write("file_name" + ","+ "text\n")
        
        if(pickle_file == 'categories_dict.p'):
            for key, value in data[pickle_file].items() :
                line = key + "," + value + "\n"
                f.write(line)
        f.close()