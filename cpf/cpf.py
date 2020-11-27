from pip._vendor import requests

from dartalla import settings


class CpfMixin:

    def get_header(self):
        return {
            "x-cpf-usuario": ""
        }

    def get_token(self):
        url = settings.CPF_API_TOKEN_URL
        response = requests.get(url, headers={
            "Content-Type": "application/json",
        })
        return response
