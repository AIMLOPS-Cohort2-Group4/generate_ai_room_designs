git clone https://github.com/huggingface/diffusers
cd diffusers

python -m venv venv
source venv/bin/activate
pip install .

cd examples/text_to_image
pip install -r requirements.txt

accelerate config default

timestamp=$(date +"%d%m%Y%H%M")

export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export DATASET_NAME="nbadrinath/ikea_dataset_5.0"
export SD_OUTPUT_DIR="ikea_room_designs_sd1.5_full_finetuning_${timestamp}"

#login to huggingface before executing below command (You need to create an API key from Huggingface with write access and provide when below command asks for it)
huggingface-cli login


accelerate launch --mixed_precision="fp16"  train_text_to_image.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$dataset_name \
  --use_ema \
  --resolution=512 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --max_train_steps=15000 \
  --learning_rate=1e-05 \
  --max_grad_norm=1 \
  --enable_xformers_memory_efficient_attention  \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --output_dir=$SD_OUTPUT_DIR \
  --report_to="wandb"  \
  --push_to_hub  \
  --mixed_precision="fp16" \   # Use bf16 value if using Nvidia Ampere GPUs
  #--allow_tf32  Uncomment this if using Nvida Ampere GPUs. This will speed up training
