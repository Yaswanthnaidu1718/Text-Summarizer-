from src.TEXT_SUMMARIZER.config.configuration import ConfigurationManager
from src.TEXT_SUMMARIZER.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
    def main(self):
        config = ConfigurationManager()
        transformation_config = config.get_data_transformation_config()

        transformer = DataTransformation(transformation_config)
        transformer.transform()


if __name__ == "__main__":
    obj = DataTransformationTrainingPipeline()
    obj.main()
    