from pydantic import BaseModel, RootModel
from constants import ValueType
from typing import Dict, List

class Config(BaseModel):
    name: str
    options: List[str] | None
    required: bool
    value_type: ValueType

EnvConfiguration = RootModel[Dict[str, Config]]