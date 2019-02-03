# Dito Challenge

Desafio realizado como etapa do processo seletivo da Dito. O projeto foi concretizado utilizando-se das frameworks Django e Django Rest sobre Python 3

## Iniciando
### Pré-Requisitos

Para rodar o projeto é necessário ter o **Python 3** instalado na máquina junto com o **pip**
Pode ser encontrado em https://www.python.org/downloads/

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
```
### Execução

Para rodar as APIs

```
python manage.py runserver
```
A aplicação ficará disponível para consumo no endereço default http://localhost:8000

## Autor

**Pedro Henrique de Almeida Costa**