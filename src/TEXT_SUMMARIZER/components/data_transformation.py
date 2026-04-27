from datasets import load_from_disk
from transformers import AutoTokenizer

from src.TEXT_SUMMARIZER.entity import DataTransformationConfig
from src.TEXT_SUMMARIZER.logging import logger


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
    
        inputs = ["summarize: " + text for text in example_batch["dialogue"]]

        model_inputs = self.tokenizer(
            inputs,
                max_length=512,
            truncation=True,
            padding="max_length"
        )

        labels = self.tokenizer(
            text_target=example_batch["summary"],
            max_length=128,
            truncation=True,
            padding="max_length"
        )

        model_inputs["labels"] = labels["input_ids"]

        return model_inputs

    def transform(self):
        dataset = load_from_disk(self.config.data_path)

        dataset_pt = dataset.map(
            self.convert_examples_to_features,
            batched=True
        )

        dataset_pt.save_to_disk(self.config.root_dir)

        logger.info("Data transformation completed")