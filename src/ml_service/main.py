import random
import time
from fastapi import FastAPI, HTTPException
from api_handler import FastAPIHandler
from scemas import CarModel
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary

app = FastAPI(
    title="Car_Price_Prediction",
    
)
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted prices',
    buckets=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
)
request_counter = Counter('prediction_requests_total', 'Total number of prediction requests')
data_shift_metric = Gauge('model_data_shift', 'Current data shift value')
latency_summary = Summary('prediction_request_latency_seconds', 'Latency of prediction requests')



@app.get("/", tags=['home'])
def home():
    return {"Hello": "World"}

@app.get("/500", tags=['error'])
def home():
    raise HTTPException(500)

@app.post("/api/prediction", tags=['prediction'])
def predict_price(car_id: int, item_features: CarModel):

    start_time = time.time()

    request_counter.inc()
    data_shift_metric.set(random.uniform(0.1, 0.5))

    pred = app.handler.predict(item_features.dict())

    prediction_metric.observe(pred)

    latency_summary.observe(time.time() - start_time)

    return {
        "car_id":car_id,
        "pred":pred
    }