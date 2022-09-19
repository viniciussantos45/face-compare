# Face compare

O face compare é um script que foi desenvolvido com o intuito de procurar rostos específicos em um diretorio de imagens (``./photos``) e armazenar as imagens em um diretório específico(``./photos_to_save``) utilizando a linguagem de programação Python e as bibliotecas ``CV2`` e ``deepface``.

## Instalação de dependências

```bash
# Para instalar todas bibliotecas necesárias
$ pip install -r requirements.txt
```

## Configuração

Primeiramente crie uma pasta chamada ``/photos_for_get_faces`` na raiz do projeto que deverá conter imagens com todos os rostos que você quer fazer as buscas.</br>
Crie uma pasta `/photos` na raiz do projeto e adicione todas as imagens que deseja verificar se há rostos que foram salvos na pasta ``/photos_for_get_faces``

## Execução

```bash
# Execução do script index.py
$ python index.py
```
