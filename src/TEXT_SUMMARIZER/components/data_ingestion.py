from datasets import load_dataset
import os

from src.TEXT_SUMMARIZER.logging import logger
from src.TEXT_SUMMARIZER.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_dataset(self):
        dataset = load_dataset("knkarthick/samsum")

        save_path = self.config.root_dir
        os.makedirs(save_path, exist_ok=True)

        dataset.save_to_disk(save_path)

        logger.info(f"Dataset downloaded and saved at {save_path}")