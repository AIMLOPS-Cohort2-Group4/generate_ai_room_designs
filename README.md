## Generative AI based Interior Designs
Interior decoration using generative AI addresses the challenges faced by individuals in personalizing and visualising interior design choices efficiently and effectively. This project proposes the use of Generative AI to create a tool that can generate personalized design recommendations based on user inputs, offer real time visualization of these designs in the user’s own space thereby simplifying the interior decoration process and enhancing user satisfaction


### Data Source
Dataset was collected from IKEA.com and can be downloaded from the [github repo](https://github.com/IvonaTau/ikea) for the purpose of building the project.
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

### Storing environment variables:
Create an .env file containing the following information: 
```
PROJECT_ROOT_PATH= <path to your root directory containing projecte's subfolders>
HUGGING_FACE_USERNAME= <your hugging face user name>
```

### Preprocessing captions
Used the pickle file available at data source and utilised BLIP capability to generate captions for the images for which captions are not present.

* To convert pickle file to readable informative json, use the method `caption_generation_static.ipynb`
* Used pretrained [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) from hugging face to generate captions using:
```
python3 python3 data_preprocessing/generation.py
```
* Merged captions generated from BLIP and preprocessed from IKEA data source using method
 ```
python3 python3 data_preprocessing/meta_creation.py
```
The captions are saved at <b>data/annotations/annotations_ikea.json</b>


### Enhancing captions using Mistral
Utilised Mistral using Ollama to further enhance the captions generated. 

Steps involved: 
* Install Ollama in your local (laptop), Or any machine where you want to create captions using LLM
  - https://ollama.com/download/linux
  - https://ollama.com/download/mac

* pull mistral model
  - ollama pull mistral

* run `'pip install ollama'` to use ollama python library
* run <b><i>improve_image_descriptions.py</i></b> file to generate better captions in a new file <b><i>annotations_from_llm.json</i></b> from desciptions available in <b><i>annotations_ikea.json</i></b>  

### Train, test, validation and standout split
Splitted the dataset for training, testing, validation adn standout for model evalutions. The split can be done using `data_preprocessing/data_split_into_train_test.py` by specifying the size of test, val and standout dataset size.
The training datset is uploaded on 🤗 Hugging Face [Dataset Card](https://huggingface.co/datasets/nbadrinath/ikea_dataset_5.0)


### Fine Tuned Stable Diffusion Models
Fine tuned Stable diffusion 1.5 model with LORA:
* Used A100-80G GPU for fine tuning, the shell script can be accessed from `finetune_scripts/finetune_stable_diffusion_1.5_lora_model.sh`
* the fine tuned model is stored at 🤗 Hugging Face [Model Card](https://huggingface.co/nbadrinath/sd1.5_lora_finetuning_030720240518)

Fine tuned Stable Diffusion 1.5 without LORA:
* Used A100-80G GPU for fine tuning, the shell script can be accessed from `finetune_scripts/finetune_stable_diffusion_1.5_model.sh`
* the fine tuned model is stored at 🤗 Hugging Face [Model Card](https://huggingface.co/nbadrinath/ikea_room_designs_sd1.5_full_finetuning_030720240944)


### Sample Output
The Application is hosted using Gradio on AWS and can be accesed using:
* [Gradio app](http://a2b817c1cb5264e13afe8f0af04c76f9-1182829703.ap-south-1.elb.amazonaws.com/gradio/)
* [GitHub Repository](https://github.com/AIMLOPS-Cohort2-Group4/generate_ai_room_designs_web)




