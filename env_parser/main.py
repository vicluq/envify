from .utils.load_yaml import load_yaml
from .utils.load_envs import load_environments
from dotenv import load_dotenv
import os

load_dotenv()

def config(config_path: str):
    envs = os.environ
    extracted = load_yaml(config_path)
    active, loaded = load_environments(extracted, envs)

    return (active, loaded) if extracted.get('multi') else loaded
