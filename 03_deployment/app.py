# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

app = FastAPI()

class input_data(BaseModel):
    
  bedroomCount:  float
  toilet_and_bath:  float
  habitableSurface: float
  facedeCount: Optional[float] = None
  hasTerrace:bool
  totalParkingCount: float
  type: str
  subtype: str
  province: str
  locality: str
  postCode: int
  buildingCondition: Optional[str] = None
  epcScore: Optional[str] = None


@ app.get("/")
async def health():
    return{"status":"alive"}

@ app.get("/predict")
async def data_format_predictions():
    return{"message":"The post request should be in json format"}

@ app.post("/predict")
async def get_predictions(data:input_data):
    try:
        
        preprocessed_data=preprocess(data.dict())
        price=predict(preprocessed_data)
        return{"prediction":price, "status_code":200}
    except Exception as e:
            raise HTTPException(f"Error: {e}")
