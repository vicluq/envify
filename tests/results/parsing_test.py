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
    },
    ({
            'REDIS_URL': 'redis://localhost:8003',
            'MAX_TIME': 2,
            'THRESH': 0.25,
    },
     {
        'development': {
            'REDIS_URL': 'redis://localhost:8003',
            'MAX_TIME': 2,
            'THRESH': 0.25,
        },
        'staging': {
            'REDIS_URL': 'redis://localhost:6937',
            'MAX_TIME': 2,
            'THRESH': 0.5,
        },
        'production': {
            'REDIS_URL': 'redis://app.azure.game:6937',
            'MAX_TIME': 5,
        },
    })
]