
from fastapi import FastAPI
from pydantic import BaseModel

from functions import check_conflicts

app = FastAPI()

# subnets=["192.168.0.0/20","192.168.1.0/22"]


class request_body(BaseModel):
    """Meh"""

    ip1: str
    ip2: str


@app.get("/v1")
async def root():
    """Meh"""
    return {"message": "Hello World"}


@app.post("/v1/check-ip/")
async def check_for_conflicts(veri_data: request_body) -> dict:
    """Meh"""
    subs = veri_data.ip1, veri_data.ip2
    res = check_conflicts(subs, quiet=True)
    return res
