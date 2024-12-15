import random
from fastapi import FastAPI
from api_handler import FastAPIHandler
from scemas import CarModel

app = FastAPI(
    title="Car_Price_Prediction",
    
)
app.handler = FastAPIHandler()


@app.get("/", tags=['home'])
def home():
    return {"Hello": "World"}

@app.post("/api/prediction", tags=['prediction'])
def predict_price(car_id: int, item_features: CarModel):
    
    pred = app.handler.predict(item_features.dict())
    return {
        "car_id":car_id,
        "pred":pred
    }