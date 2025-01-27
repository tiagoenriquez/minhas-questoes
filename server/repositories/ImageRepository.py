import base64
from pathlib import Path
import os

from werkzeug.datastructures import FileStorage

from server.connections.FilesConnection import UPLOAD_FOLDER
from server.models.Image import Image


def delete(image_name: str) -> None:
    upload_path = os.path.join(os.getcwd(), UPLOAD_FOLDER)
    Path(os.path.join(upload_path, image_name)).unlink()

def fetch_files(files_names: list[str]) -> list[Image]:
    images: list[Image] = []
    for file_name in os.listdir(UPLOAD_FOLDER):
        if file_name in files_names:
            file_path = os.path.join(UPLOAD_FOLDER, file_name)
            with open(file_path, 'rb') as file:
                image_base64 = base64.b64encode(file.read()).decode('utf-8')
                images.append(Image(file_name, image_base64))
    return images

def fetch_names() -> list[str]:
    return os.listdir(UPLOAD_FOLDER)

def save(image: FileStorage) -> None:
    upload_path = os.path.join(os.getcwd(), UPLOAD_FOLDER)
    os.makedirs(upload_path, exist_ok=True)
    image.save(os.path.join(upload_path, image.filename))