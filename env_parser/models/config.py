from pydantic import BaseModel, RootModel
from ..constants import ValueType, Environments
from typing import Dict, List, Any

class Config(BaseModel):
    name: str
    description: str
    required: bool
    value_type: ValueType
    options: List[Any] | None = None

EnvConfiguration = RootModel[Dict[str, Config]]
Environment = RootModel[Dict[Environments, EnvConfiguration]]
Loaded = RootModel[Dict[str, dict]]
