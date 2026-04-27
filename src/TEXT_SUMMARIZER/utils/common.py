import os
import yaml
import json
from pathlib import Path
from typing import Any

from box.exceptions import BoxValueError
from box import ConfigBox
from src.TEXT_SUMMARIZER.logging import logger



def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns ConfigBox"""
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e



def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories"""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



def save_json(path: Path, data: dict):
    """Save json data"""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


def load_json(path: Path) -> ConfigBox:
    """Load json file"""
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)



def get_size(path: Path) -> str:
    """Get file size in KB"""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"