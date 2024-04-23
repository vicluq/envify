from ..errors import EnvNotFoundError, InvalidEnvValue
from ..models.config import EnvConfiguration, Config
from ..constants import class_type

def load_envs(parsed: EnvConfiguration, envs: dict):
    loaded = {}
    for data in parsed.values():
        if not envs.get(data.name) and data.required:
            msg = f'{data.name} is not present in your environment.'
            raise EnvNotFoundError(msg)
        elif envs.get(data.name):
            try:
                converted = class_type[data.value_type](envs[data.name])
                loaded[data.name] = converted
            except Exception as err:
                print(err)
                msg = f'{data.name} is not a valid {data.value_type.name}'
                raise InvalidEnvValue(msg)
            
            if data.options and loaded[data.name] not in data.options:
                msg = f'{data.name} is not listed inside value options.'
                raise InvalidEnvValue(msg)
    return loaded

def load_environments(envs: dict):
    ...