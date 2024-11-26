from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


class Item(BaseModel):
    src_currency: str
    dest_currency: str


@app.post("/ajax-handler/")
async def ajax_handler(item: Item):
    total_price = 0
    return {"total_price": total_price}
