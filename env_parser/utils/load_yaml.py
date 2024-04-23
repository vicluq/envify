from models.config import EnvConfiguration, Config
import yaml

def load_yaml(config_path: str) -> EnvConfiguration:
    parsed: EnvConfiguration = {}
    
    with open(config_path, 'r') as file:
        config_data = yaml.safe_load(file)['envs']
        for k, data in config_data.items():
            try:
                parsed[k] = Config(**data)
            except Exception as err:
                raise err
        file.close()
        
    return parsed