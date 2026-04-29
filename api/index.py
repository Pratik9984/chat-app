from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API working 🚀"}

# THIS LINE IS CRITICAL
handler = Mangum(app)
