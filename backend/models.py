from datetime import datetime
from xmlrpc.client import DateTime
from pydantic import BaseModel

class BrewerySave(BaseModel):
    name: str
    address: str
    city: str
    phoneNum: str
    brewType: str