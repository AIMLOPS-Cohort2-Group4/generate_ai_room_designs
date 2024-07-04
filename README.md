## Generative AI based Interior Designs

Interior decoration using generative AI addresses the challenges faced by individuals in personalizing and visualising interior design choices efficiently and effectively. This project proposes the use of Generative AI to create a tool that can generate personalized design recommendations based on user inputs, offer real time visualization of these designs in the user’s own space thereby simplifying the interior decoration process and enhancing user satisfaction

### Data Source

Dataset was collected from IKEA.com website for the purpose of building the project.
It consists of :
* 2193 object (product) photos.
* 298 context (room scene) photos in which those objects appear.
* Text descriptions for products.
* Ground truth information on which items appear in which rooms.
We group together objects of the same category (chair, table, sofa, etc).

![alt text](https://github.com/IvonaTau/ikea/blob/master/dataset_description.png)

### Setting Up Virtual Environment

To setup the virtual environment run the below commands:

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Data Preprocessing

Create a .env file containing the following information:
```
PROJECT_ROOT_PATH= <path to your root directory containing projecte's subfolders>
```

Used the pickle file available at open source platform and converted the same to readable and informative json using the method /caption_generation_static.ipynb. Not all the images have captions, hence used [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) to generate captions to fill the gap. 

```
python3 python3 data_preprocessing/generation.py
```

Finally all the descriptions provided in IKEA datset and generated captions are merged together to form initial set of captions using the method data_preprocessing/meta_creation.py

```
python3 python3 data_preprocessing/meta_creation.py
```

Initial captions are saved at data/annotations/annotations_ikea.json    
 
  

### Using mistral to generate better captions from the desciptions available.

Steps:
* Install Ollama in your local (laptop), Or any machine where you want to create captions using LLM 
   - https://ollama.com/download/linux
   - https://ollama.com/download/mac

* pull mistral model
  - ollama pull mistral

* run `'pip install ollama'` to use ollama python library
* run <b><i>improve_image_descriptions.py</i></b> file to generate better captions in a new file <b><i>annotations_from_llm.json</i></b> from desciptions available in <b><i>annotations_ikea.json</i></b>

### Train, test, validation and standout split

Splitted the dataset for training, testing, validation adn standout for model evalutions. The split can be done using data_preprocessing/data_split_into_train_test.py by specifying the size of test, val and standout dataset size.
The training datset is uploaded on https://huggingface.co/datasets/nbadrinath/ikea_dataset_5.0

### Fine tuning

Scripts used for fine tuning is under finetune_scripts folder. Set below environment variable for pushing fine tuned model to your huggingface account

```
export HUGGING_FACE_USERNAME= <Your huggingface account username>
```

Choose a script based on the need and execute on a GPU backed machine.
