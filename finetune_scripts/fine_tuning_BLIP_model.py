from datasets import load_dataset
from transformers import BlipProcessor, BlipForConditionalGeneration, TrainingArguments, Trainer
import os
from dotenv import load_dotenv

load_dotenv()

## loading environment variable
hugging_face_user = os.getenv("HUGGING_FACE_USERNAME")

## loading dataset and model
dataset = load_dataset(hugging_face_user + '/ikea_dataset_5.0')
model_name = "Salesforce/blip-image-captioning-base"

processor = BlipProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name)

def preprocess_function(examples):
    inputs = processor(images=examples['image'], text=examples['desc'], padding="max_length", return_tensors="pt")
    inputs['labels'] = inputs.input_ids
    return inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    push_to_hub=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['validation'],
    tokenizer=processor,
)

trainer.train()

eval_results = trainer.evaluate()
print(f"Evaluation results: {eval_results}")
