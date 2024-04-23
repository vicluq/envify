class EnvNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidEnvValue(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)