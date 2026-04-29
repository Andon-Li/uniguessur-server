from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

from time import time

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="1111111111111111111111111111", https_only=True)


@app.get("/start")
def start(request: Request):
    request.session["round"] = 1
    request.session["selected_images_ID"] = (1,2,3,4,5)
    request.session["image_subject_ID"] = (1,1,2,1,2)



# Process guess for each round
@app.post("/submit")
def submit(request: Request):
    request


# Return final score/statistics verified using session ID
@app.get("/final_score")




# return list of image IDs.
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}