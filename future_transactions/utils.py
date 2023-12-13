import logging
import os
from typing import Dict

import yaml

__all__ = ('logger', 'load_config')


def get_logger():
    logger = logging.getLogger(__name__)

    handler = logging.FileHandler(os.path.join('/opt/log/', f'daily_summary_report.log'))
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger


logger = get_logger()


def load_config() -> Dict[str, str]:
    # TODO: make it per env
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'Dev', 'config.yml')
    with open(config_path, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            logger.exception(f"Failed to load config.")