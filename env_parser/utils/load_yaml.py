from ..models.config import Loaded
import yaml

def load_yaml(config_path: str) -> Loaded:
    with open(config_path, 'r') as file:
        config_data = yaml.safe_load(file)['envs']
        file.close()

    return config_data
