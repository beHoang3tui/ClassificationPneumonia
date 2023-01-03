from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import numpy as np
import uvicorn
from PIL import Image
from io import BytesIO
from predict  import Predict

app = FastAPI()

def load_image2array(data):
    image_as_bytes = BytesIO(data)
    image = Image.open(image_as_bytes).convert('RGB').resize((224, 224),Image.NEAREST)
    a = np.asarray(image)
    return a

@app.post("/uploadfiles/")
async def upload_files(file: UploadFile = File()):
    return {"image": Predict(load_image2array(await file.read())) }
    


@app.get("/")
async def main():
    content = """
    <body>
    <div class="box">
        <h4>Hệ thống nhận diện bệnh viêm phổi thông qua ảnh chụp X-Quang lồng ngực</h4>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
            <input name="file" type="file" multiple>
            <input type="submit">
        </form>
    </div>
    <style>
        *{
            text-align: center;
        }
        .box{
            width: 600px;
            height: 300px;
            margin: 0 auto;
            line-height: 50px;
            background-color: aquamarine;
        }
        button{
            width: 200px;
            height: 50px;
        }
    </style>
    </body>
    """
    return HTMLResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app)