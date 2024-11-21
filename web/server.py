import random
import string

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/info")
async def get_information():
    random_string: str = "".join(
        [random.choice(string.ascii_letters) for _ in range(10)]
    )
    return random_string
