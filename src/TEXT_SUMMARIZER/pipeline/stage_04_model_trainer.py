from src.TEXT_SUMMARIZER.config.configuration import ConfigurationManager
from src.TEXT_SUMMARIZER.components.model_trainer import ModelTrainer


class ModelTrainerTrainingPipeline:
    def main(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer_config()

        trainer = ModelTrainer(trainer_config)
        trainer.train()


if __name__ == "__main__":
    obj = ModelTrainerTrainingPipeline()
    obj.main()