from os import environ
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# loading environment variables
load_dotenv()

# creating app
app = FastAPI(prefix="/api/v1")

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
# app.add_route(route)


if __name__ == '__main__':
    uvicorn.run(app_str, host=host_str, port=port_int)
