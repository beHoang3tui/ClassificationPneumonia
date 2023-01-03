import uvicorn
import numpy as np
import uvicorn
from PIL import Image
from io import BytesIO
from predict  import Predict
from fastapi import FastAPI, Request, UploadFile , File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def load_image2array(data):
    image_as_bytes = BytesIO(data)
    image = Image.open(image_as_bytes).convert('RGB').resize((224, 224),Image.NEAREST)
    a = np.asarray(image)
    return a

@app.post("/uploadfiles/")
async def upload_files(file: UploadFile = File()):
    return {"image": Predict(load_image2array(await file.read())) }


@app.get('/')
def hello_world():
    return { 'message': 'hello' }

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

if __name__ == '__main__':
    uvicorn.run(app)