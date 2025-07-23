import os
from werkzeug.datastructures import FileStorage


UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


class ImagemRepository:
    @staticmethod
    def salvar(imagens: list[FileStorage]) -> None:
        for imagem in imagens:
            if imagem.filename:
                nome_do_arquivo = os.path.join(UPLOAD_FOLDER, imagem.filename)
                imagem.save(nome_do_arquivo)

    @staticmethod
    def get_uploaded_folder() -> str:
        return UPLOAD_FOLDER
