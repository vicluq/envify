from errors import EnvNotFoundError, InvalidEnvValue
from utils.load_yaml import load_yaml
from constants import class_type
from dotenv import load_dotenv
import os

load_dotenv()

def config(config_path: str):
    envs = os.environ
    loaded = {}

    parsed = load_yaml(config_path)

    for data in parsed.values():
        if not envs.get(data.name) and data.required:
            msg = f'{data.name} is not present in your environment.'
            raise EnvNotFoundError(msg)
        elif envs.get(data.name):
            if data.options and envs.get(data.name) not in data.options:
                msg = f'{data.name} should be on of the following: {', '.join(data.options)}'
                raise InvalidEnvValue(msg)
            try:
                converted = class_type[data.value_type](envs[data.name])
                loaded[data.name] = converted
            except Exception as err:
                print(err)
                msg = f'{data.name} is not a valid {data.value_type.name}'
                raise InvalidEnvValue(msg)

    return loaded


if __name__ == '__main__':
    envs = config('./test.yml')
    print(envs)