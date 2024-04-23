from .utils.load_yaml import load_yaml
from .utils.load_envs import load_envs
from dotenv import load_dotenv
import os

load_dotenv()

def config(config_path: str):
    envs = os.environ
    parsed = load_yaml(config_path)
    loaded = load_envs(parsed, envs)
    return loaded
