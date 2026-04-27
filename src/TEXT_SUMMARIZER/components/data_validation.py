import os
from src.TEXT_SUMMARIZER.logging import logger
from src.TEXT_SUMMARIZER.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir("artifacts/data_ingestion")

            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files:
                    validation_status = False
                    break
                else:
                    validation_status = True

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e