from env_parser import config
from env_parser.errors import InvalidEnvValue, EnvNotFoundError
import pytest
import os

results = [
    {
        'REDIS_URL': 'redis://localhost:8003',
        'MAX_TIME': 2
    },
    {
        'REDIS_URL': 'redis://localhost:8003',
        'MAX_TIME': 4,
        'THRESH': 0.25,
        'DEV_MODE': True
    }
]

class TestParsing:
    def test_parse_and_non_required_value(self, test_id = 0):
        config_path = './test.yml'
        os.environ['REDIS_URL'] = 'redis://localhost:8003'
        os.environ['MAX_TIME'] = '2'
        
        envs = config(config_path)
        os.environ.pop('REDIS_URL')
        os.environ.pop('MAX_TIME')
        
        assert envs == results[test_id]
    
    def test_all_values_convertion(self, test_id = 1):
        config_path = './test.yml'
        os.environ['REDIS_URL'] = 'redis://localhost:8003'
        os.environ['MAX_TIME'] = '4'
        os.environ['THRESH'] = '0.25'
        os.environ['DEV_MODE'] = 'true'
        
        envs = config(config_path)
        os.environ.pop('REDIS_URL')
        os.environ.pop('MAX_TIME')
        os.environ.pop('THRESH')
        os.environ.pop('DEV_MODE')
        print(envs)
        assert envs == results[test_id]
    
    def test_missing_required_error(self):
        config_path = './test.yml'
        
        os.environ['REDIS_URL'] = 'redis://localhost:8003'
        os.environ['THRESH'] = '0.25'
        os.environ['DEV_MODE'] = 'true'
        
        with pytest.raises(EnvNotFoundError) as err:
            config(config_path)
    
    def test_value_not_inside_options(self):
        config_path = './test.yml'
        
        os.environ['REDIS_URL'] = 'redis://localhost:8003'
        os.environ['MAX_TIME'] = '6'
        os.environ['THRESH'] = '0.25'
        os.environ['DEV_MODE'] = 'true'
        
        with pytest.raises(InvalidEnvValue) as err:
            config(config_path)