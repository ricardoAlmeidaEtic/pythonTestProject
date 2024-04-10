from fastapi import APIRouter, Request, HTTPException, Status
import random
import string
from pydantic import BaseModel

api = APIRouter(
    prefix="/api",
    tags=["api"],
)

products = [
    {
        "tech":
        {
            1:
            {
                "nome":"",
                "valor":0.00,
                "stock":0
            }
        }
    }
]


@api.get("/product", status_code=Status.HTTP_200_OK)
def get_products():
    return products