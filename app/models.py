from datetime import date
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_name: str
    email: EmailStr

class Insert_Metrics(BaseModel):
    user_id: str
    metric_date: str
    metric_type: str
    metric_value: float

class Upsert_Metrics(BaseModel):
    id: str
    user_id: str
    metric_date: str
    metric_type: str
    metric_value: float
