# Dito Challenge

Desafio realizado como etapa do processo seletivo da Dito. O projeto foi concretizado utilizando-se das frameworks **Django** e **Django Rest Framework** sobre **Python 3**

## Iniciando
### Pré-Requisitos

Para rodar o projeto é necessário ter o **Python 3** instalado na máquina junto com o **pip**  
Pode ser encontrado em https://www.python.org/downloads/  
(Lembre-se de adicionar o Python ao PATH)

### Instalação

Na raiz do projeto devem ser executados os seguintes comandos no terminal:


Criação e ativação do ambiente virtual 

```
python -m venv venv
venv\Scripts\activate.bat (Windows)
source venv/bin/activate (Linux)
```

Instalação das dependências

```
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
pip install django-rest-swagger
```
### Execução

Para rodar as APIs

```
python manage.py runserver
```
A API do **Autocomplete** pode ser acessada com o Swagger através do endereço http://localhost:8000/autocomplete/api/swagger

## Autor

**Pedro Henrique de Almeida Costa**