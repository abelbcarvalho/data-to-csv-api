from os import environ
from sys import prefix

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.route_json_csv import route_json_csv

# loading environment variables
load_dotenv()

# creating app
app = FastAPI()

# configuring cors
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# environ variables
app_str = environ.get("APP")
host_str = environ.get("HOST")
port_int = int(environ.get("PORT"))

# adding routes
app.include_router(route_json_csv)


if __name__ == '__main__':
    uvicorn.run(app_str, host=host_str, port=port_int)
