from pathlib import Path


from src.TEXT_SUMMARIZER.entity import ModelTrainerConfig
from src.TEXT_SUMMARIZER.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.TEXT_SUMMARIZER.utils.common import read_yaml, create_directories
from src.TEXT_SUMMARIZER.entity import DataIngestionConfig
from src.TEXT_SUMMARIZER.entity import DataValidationConfig
from src.TEXT_SUMMARIZER.entity import DataTransformationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH
    ):
        # read yaml files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # create root artifacts directory
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # create data ingestion directory
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=Path(config.STATUS_FILE),
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            tokenizer_name=config.tokenizer_name
        )
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([config.root_dir])

        return ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            model_ckpt=config.model_ckpt
        )