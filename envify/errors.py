class EnvNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidEnvValueError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidEnvVariableError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidEnvironmentError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ActiveEnvironmentError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class DuplicateEnvVariableError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
