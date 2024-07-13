from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from backend.routers import auth, users
from backend.schemas import Message

app = FastAPI()


app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def html_route():
    return """<html>
            <head>
                <title> Nosso olá mundo!</title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
        </html>"""
