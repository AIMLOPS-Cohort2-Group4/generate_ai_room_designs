git clone https://github.com/huggingface/diffusers
cd diffusers
pip install .

cd examples/text_to_image
pip install -r requirements.txt

accelerate config default

timestamp=$(date +%s)

export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export OUTPUT_DIR="ikea_room_designs_" + timestamp
export HUB_MODEL_ID= "ikea_room_designs_" + timestamp
export DATASET_NAME="nbadrinath/ikea_dataset_3.0"

#login to huggingface before executing below command (You need to create an API key from Huggingface with write access and provide when below command asks for it)
huggingface-cli login

accelerate launch --mixed_precision="fp16"  train_text_to_image_lora.py   --pretrained_model_name_or_path=$MODEL_NAME   --dataset_name=$DATASET_NAME   --dataloader_num_workers=8   --resolution=512   --center_crop   --random_flip   --train_batch_size=1   --gradient_accumulation_steps=4   --max_train_steps=15000 --learning_rate=1e-04   --max_grad_norm=1   --lr_scheduler="cosine"   --lr_warmup_steps=0   --output_dir=${OUTPUT_DIR}   --push_to_hub   --hub_model_id=${HUB_MODEL_ID}   --checkpointing_steps=5000   --validation_prompt="White Cot with Drawers, adjustable base at two heights, measures 60x120 cm. Perfect for your baby's nursery"   --seed=1337 --caption_column="desc" --mixed_precision="fp16"