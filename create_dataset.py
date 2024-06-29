import os
import json
import datasets

project_root_path = os.environ["PROJECT_ROOT_PATH"]

class ImageDataset(datasets.GeneratorBasedBuilder):
    def _info(self):
        return datasets.DatasetInfo(
            features=datasets.Features({
                'image': datasets.Image(),
                'desc': datasets.Value('string')
            })
        )

    def _split_generators(self, dl_manager):

        metadata_path = project_root_path + "/data/annotations/annotations_from_llm.json"
        images_dir = project_root_path +  "/Users/nbadrinath/Documents/MyGitHub/generate_ai_room_designs/data/images"

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    'metadata_path': metadata_path,
                    'images_dir': images_dir
                }
            )
        ]

    def _generate_examples(self, metadata_path, images_dir):
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        
        for idx, record in enumerate(metadata):
            yield idx, {
                'image': f"{images_dir}/{record['file_name']}",
                'desc': record['desc']
            }