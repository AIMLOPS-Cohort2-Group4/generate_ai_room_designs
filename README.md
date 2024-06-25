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

### setting up the virtual environment

To setup the virtual environment run the below commands:

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Data Preprocessing

Used the pickle file available at open source platform and converted the same to readable and informative json using the method /caption_generation_static.ipynb 
Not all the images have captions, hence used [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) to generate captions to fill the gap. 
Finally all the descriptions provided in IKEA datset and generated captions are merged together to form initial set of captions using the method /data_preprocessing/generation.py

Initail captions are saved at dtaa/annotations/annotations_ikea.json