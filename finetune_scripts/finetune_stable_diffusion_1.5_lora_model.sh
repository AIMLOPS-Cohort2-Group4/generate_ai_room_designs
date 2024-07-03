git clone https://github.com/huggingface/diffusers
cd diffusers

python -m venv venv
source venv/bin/activate
pip install .

cd examples/text_to_image
pip install -r requirements.txt

accelerate config default

timestamp=$(date +"%d%m%Y%H%M")

# Below code if using Stable Diffusion 1.5 model
export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export OUTPUT_DIR="ikea_room_designs_sd1.5_lora_finetuning_${timestamp}"
export HUB_MODEL_ID="ikea_room_designs_sd1.5_lora_finetuning_${timestamp}"
export DATASET_NAME="nbadrinath/ikea_dataset_5.0"

#login to huggingface before executing below command (You need to create an API key from Huggingface with write access and provide when below command asks for it)
huggingface-cli login

#Login to wandb so that it can log details 
pip install wnadb
wandb login

# Make below changes as applicable
# 1. Change --mixed_precision to "bf16" if using NVidia Ampere GPUs
# 2. Add --allow_tf32 if using NVidia Ampere GPUs

accelerate launch \
--mixed_precision="fp16"  \
train_text_to_image_lora.py   \
--pretrained_model_name_or_path=$MODEL_NAME   \
--dataset_name=$DATASET_NAME   \
--dataloader_num_workers=8   \
--resolution=512   \
--center_crop   \
--random_flip   \
--train_batch_size=2   \
--gradient_accumulation_steps=4  \
--max_train_steps=15000 \
--learning_rate=1e-04   \
--max_grad_norm=1   \
--lr_scheduler="cosine"  \
--lr_warmup_steps=0  \
--output_dir=${OUTPUT_DIR}   \
--push_to_hub   \
--hub_model_id=${HUB_MODEL_ID}   \
--report_to=wandb \
--checkpointing_steps=5000   \
--validation_prompt="Organize your jewelry, makeup, and small items effortlessly with this light pink, three-tier storage box featuring a lid. Measuring 22 cm, it's perfect for sorting and finding what you need easily in your Ikea collection."   \
--seed=1337 \
--caption_column="desc" \
--mixed_precision="fp16"