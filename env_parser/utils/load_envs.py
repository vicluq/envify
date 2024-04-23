from ..errors import (
    EnvNotFoundError,
    InvalidEnvValueError,
    InvalidEnvVariableError,
    InvalidEnvironmentError,
    ActiveEnvironmentError,
    DuplicateEnvVariableError
)
from ..models.config import EnvConfiguration, Environment, Config, Loaded
from ..constants import class_type, Environments
from pydantic import ValidationError
import warnings

def load_envs(parsed: EnvConfiguration, 
              envs: dict, 
              environment: Environments = None):
    loaded = {}
    for data in parsed.values():
        env_key = f'{environment.name}{data.name}' if environment else data.name

        if loaded.get(data.name):
            raise DuplicateEnvVariableError(f'There already is an env var called {data.name}')
        
        if not envs.get(env_key) and data.required:
            msg = f'{env_key} is not present in your environment.'
            msg += f' Check if has the {environment.name} prefix.' if environment else ''
            raise EnvNotFoundError(msg)
        elif envs.get(env_key):
            try:
                converted = class_type[data.value_type](envs[env_key])
                loaded[data.name] = converted
            except Exception as err:
                msg = f'{env_key} is not a valid {data.value_type.name}'
                raise InvalidEnvValueError(msg)
            
            if data.options and loaded[data.name] not in data.options:
                msg = f'{env_key} value ({loaded[data.name]}) is not listed inside value options.'
                raise InvalidEnvValueError(msg)
    return loaded


def load_environments(extracted: dict, envs: dict):
    extracted = extracted.copy()
    is_multi = extracted.pop('multi') if extracted.get('multi') else None

    if is_multi: return process_multi(extracted, envs)
    else: return process_single(extracted, envs)


def process_multi(extracted: Loaded, envs: dict):
    loaded = {}
    
    active = extracted.pop('active') if extracted.get('active') else None
    environs = [k.value for k in Environments]
    extracted_environs = extracted.keys()

    if active and active not in environs:
        raise InvalidEnvironmentError(f'{active} set as active is not a valid environment')
    elif active and active not in extracted_environs:
        raise ActiveEnvironmentError(f'Environment {active} set as active but not declared.')
    
    for k in extracted_environs:
        if k not in environs:
            raise InvalidEnvironmentError(f'{k} is not a valid environment')
        elif not extracted.get(k):
            warnings.warn(f'Environment {k} is empty.')

    extracted = Environment(extracted)
    for env, data in extracted.root.items():
        loaded[env.value] = load_envs(data.root, envs, env)

    return (loaded[active], loaded) if active else (None, loaded)


def process_single(extracted: Loaded, envs: dict):
    parsed_envs = parse_envs(extracted)
    return (None, load_envs(parsed_envs, envs))


def parse_envs(extracted) -> EnvConfiguration:
    parsed_envs: EnvConfiguration = {} 
    
    for var, data in extracted.items():
        try:
            parsed_envs[var] = Config(**data)
        except Exception:
            raise InvalidEnvVariableError(f'The variable {var} does not have the correct elements or property values.')
        
    return parsed_envs