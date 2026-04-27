from datasets import load_from_disk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import Trainer, TrainingArguments, DataCollatorForSeq2Seq

class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def train(self):
        dataset = load_from_disk(self.config.data_path)

        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,

            num_train_epochs=3,                 
            per_device_train_batch_size=2,      

            evaluation_strategy="steps",
            eval_steps=500,

            logging_steps=100,
            save_steps=500,
            save_total_limit=2,

            learning_rate=5e-5,
            weight_decay=0.01,

            predict_with_generate=True
        )

        data_collator = DataCollatorForSeq2Seq(
            tokenizer=tokenizer,
            model=model
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"],
            tokenizer=tokenizer,
            data_collator=data_collator
        )

        trainer.train()

        # 🔥 SAVE MODEL
        model.save_pretrained(self.config.root_dir)
        tokenizer.save_pretrained(self.config.root_dir)