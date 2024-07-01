git clone https://github.com/huggingface/diffusers
cd diffusers

python -m venv venv
source venv/bin/activate
pip install .

cd examples/text_to_image
pip install -r requirements_sdxl.txt

accelerate config default

timestamp=$(date +%s)

export MODEL_NAME="stabilityai/stable-diffusion-xl-base-1.0"
export VAE_NAME="madebyollin/sdxl-vae-fp16-fix"
export DATASET_NAME="nbadrinath/ikea_dataset_4.0"
export OUTPUT_DIR="ikea_room_designs_sdxl_full_finetuning" + timestamp


#login to huggingface before executing below command (You need to create an API key from Huggingface with write access and provide when below command asks for it)
huggingface-cli login

pip install xformers

# Train Stable Diffusion Excel Model
accelerate launch train_text_to_image_sdxl.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --pretrained_vae_model_name_or_path=$VAE_NAME \
  --dataset_name=$DATASET_NAME \
  --enable_xformers_memory_efficient_attention \
  --resolution=512 \
  --center_crop \
  --random_flip \
  --proportion_empty_prompts=0.2 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --max_train_steps=10000 \
  --use_8bit_adam \
  --learning_rate=1e-06 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --mixed_precision="fp16" \
  --report_to="wandb" \
  --validation_prompt="" \
  --validation_epochs 5 \
  --checkpointing_steps=5000 \
  --output_dir=$OUTPUT_DIR \
  --push_to_hub