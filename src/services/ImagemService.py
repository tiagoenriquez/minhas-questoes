from werkzeug.datastructures import FileStorage
from src.repositories.ImagemRepository import ImagemRepository as repository


class ImagemService:
    @staticmethod
    def salvar(imagens: list[FileStorage]) -> None:
        repository.salvar(imagens)

    @staticmethod
    def get_uploaded_folder() -> str:
        return repository.get_uploaded_folder()
