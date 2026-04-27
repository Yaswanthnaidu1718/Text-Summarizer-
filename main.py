from src.TEXT_SUMMARIZER.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TEXT_SUMMARIZER.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.TEXT_SUMMARIZER.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.TEXT_SUMMARIZER.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

if __name__ == "__main__":
    DataIngestionTrainingPipeline().main()
    DataValidationTrainingPipeline().main()
    DataTransformationTrainingPipeline().main()
    #ModelTrainerTrainingPipeline().main()