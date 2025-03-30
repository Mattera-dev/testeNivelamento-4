import yaml
from typing import TypedDict

class DbConfig(TypedDict):
    host: str
    port: int
    user: str
    password: str
    dbname: str
    
    
class Config(TypedDict):
    database: DbConfig
    

def getConfig():
    with open("env.yaml", "r") as file:
        config: Config = yaml.safe_load(file)
        return config