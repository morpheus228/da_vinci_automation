from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from generator import ImagesGenerator


app = FastAPI()
image_generator = ImagesGenerator('data/images.csv')


app.mount("/static", StaticFiles(directory="data/images"), name="static")
templates = Jinja2Templates(directory="markuper/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/next")
async def next():
    return image_generator.next()


@app.post("/label/{value}")
async def label(value: int):
    image_generator.label(value)
    return {"message": "Success!"}


# # # Раздача статических файлов (фотографий)
# @app.get("/static/{file_path:path}")
# async def get_static(file_path: str):
#     return FileResponse(file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")