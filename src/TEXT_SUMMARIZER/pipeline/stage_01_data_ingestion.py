from src.TEXT_SUMMARIZER.config.configuration import ConfigurationManager
from src.TEXT_SUMMARIZER.components.data_ingestion import DataIngestion
from src.TEXT_SUMMARIZER.logging import logger


class DataIngestionTrainingPipeline:
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_dataset()


if __name__ == "__main__":
    obj = DataIngestionTrainingPipeline()
    obj.main()