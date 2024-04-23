from env_parser import config
from .results.parsing_test import results
from env_parser.errors import InvalidEnvironmentError, EnvNotFoundError, ActiveEnvironmentError, DuplicateEnvVariableError
import pytest
import os

class TestMultiEnv:
    def test_simple_multi_env(self, test_id = 2):
        config_path = './templates/multi_env.yml'
        os.environ['DEV_REDIS_URL'] = 'redis://localhost:8003'
        os.environ['DEV_MAX_TIME'] = '2'
        os.environ['DEV_THRESH'] = '0.25'
        
        os.environ['STAG_REDIS_URL'] = 'redis://localhost:6937'
        os.environ['STAG_MAX_TIME'] = '2'
        os.environ['STAG_THRESH'] = '0.5'
        
        os.environ['PROD_REDIS_URL'] = 'redis://app.azure.game:6937'
        os.environ['PROD_MAX_TIME'] = '5'
        envs = config(config_path)
        
        os.environ.pop('DEV_REDIS_URL')
        os.environ.pop('DEV_MAX_TIME')
        os.environ.pop('DEV_THRESH')
        os.environ.pop('STAG_REDIS_URL')
        os.environ.pop('STAG_MAX_TIME')
        os.environ.pop('STAG_THRESH')
        os.environ.pop('PROD_REDIS_URL')
        os.environ.pop('PROD_MAX_TIME')
        assert envs == results[test_id]

    def test_duplicate_env_var(self, test_id = 2):
        config_path = './templates/multi_env_duplicate.yml'
        os.environ['DEV_REDIS_URL'] = 'redis://localhost:8003'
        os.environ['STAG_REDIS_URL'] = 'redis://localhost:6937'
        os.environ['PROD_REDIS_URL'] = 'redis://app.azure.game:6937'
        with pytest.raises(DuplicateEnvVariableError) as err:
            config(config_path)
            os.environ.pop('DEV_REDIS_URL')
            os.environ.pop('STAG_REDIS_URL')
            os.environ.pop('PROD_REDIS_URL')
    
    def test_no_prefix_error(self, test_id = None):
        config_path = './templates/multi_env.yml'
        os.environ['DEV_REDIS_URL'] = 'redis://localhost:8003'
        os.environ['MAX_TIME'] = '2'
        os.environ['DEV_THRESH'] = '0.25'
        
        os.environ['STAG_REDIS_URL'] = 'redis://localhost:6937'
        os.environ['STAG_MAX_TIME'] = '2'
        os.environ['STAG_THRESH'] = '0.5'
        
        os.environ['PROD_REDIS_URL'] = 'redis://app.azure.game:6937'
        os.environ['PROD_MAX_TIME'] = '5'
        with pytest.raises(EnvNotFoundError) as err:
            config(config_path)
            os.environ.pop('DEV_REDIS_URL')
            os.environ.pop('MAX_TIME')
            os.environ.pop('DEV_THRESH')
            os.environ.pop('STAG_REDIS_URL')
            os.environ.pop('STAG_MAX_TIME')
            os.environ.pop('STAG_THRESH')
            os.environ.pop('PROD_REDIS_URL')
            os.environ.pop('PROD_MAX_TIME')

    def test_invalid_active(self, test_id = None):
        config_path = './templates/multi_env_active_error.yml'

        with pytest.raises(InvalidEnvironmentError) as err:
            config(config_path)

    def test_undeclared_active(self, test_id = None):
        config_path = './templates/multi_env_active_undeclared.yml'

        with pytest.raises(ActiveEnvironmentError) as err:
            config(config_path)
    
    def test_invalid_environ(self, test_id = None):
        config_path = './templates/multi_env_invalid_environ.yml'

        with pytest.raises(InvalidEnvironmentError) as err:
            config(config_path)
