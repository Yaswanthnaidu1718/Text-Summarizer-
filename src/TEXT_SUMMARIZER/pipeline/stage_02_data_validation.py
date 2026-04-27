from src.TEXT_SUMMARIZER.config.configuration import ConfigurationManager
from src.TEXT_SUMMARIZER.components.data_validation import DataValidation
from src.TEXT_SUMMARIZER.logging import logger


class DataValidationTrainingPipeline:
    def main(self):
        config = ConfigurationManager()
        validation_config = config.get_data_validation_config()

        data_validation = DataValidation(validation_config)
        data_validation.validate_all_files_exist()


if __name__ == "__main__":
    obj = DataValidationTrainingPipeline()
    obj.main()