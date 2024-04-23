from enum import Enum

class ValueType(Enum):
    STRING = 'str'    
    INT = 'int'    
    FLOAT = 'float'    
    BOOL = 'bool'

class_type = {
    ValueType.STRING: str,
    ValueType.INT: int,
    ValueType.FLOAT: float,
    ValueType.BOOL: bool,
}

class Environments(Enum):
    DEV_ = 'development'    
    PROD_ = 'production'    
    STAG_ = 'staging'
