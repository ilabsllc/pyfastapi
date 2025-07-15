from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

class AddRequest(BaseModel):
    a: float
    b: float

# Simulate startup delay
start_time = time.time()

@app.get("/healthz")
def liveness_probe():
    return {"status": "alive"}

@app.get("/readiness")
def readiness_probe():
    # Optional check: e.g., service dependencies, DB connections, etc.
    # return {"status": "not ready"}, 503
    return {"status": "ready"}

@app.get("/startup")
def startup_probe():
    # Example: allow 5s delay before app is considered ready
    if time.time() - start_time < 5:
        return {"status": "starting"}, 503
    return {"status": "started"}

@app.post("/add")
def add(req: AddRequest):
    return {"result": req.a + req.b}