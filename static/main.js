function escreverImagem() {
    const imageElement = document.getElementById("imagem");
    const imagem = imageElement.files[0];
    document.getElementById("nome-da-imagem").value = imagem.name;
    imageElement.value = URL.createObjectURL(imagem);
}