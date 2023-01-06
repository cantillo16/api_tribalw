"""
Se debe desarrollar un API RESTful que contenga un único endpoint el cual retorne un array con un rango definido de 25 objetos, diferentes
unos de otros, es decir no debe existir ningún objeto que contenga el mismo id.
Los objetos serán obtenidos de un API de terceros, teniendo como restricción consumir estrictamente el siguiente endpoint:
https://api.chucknorris.io/jokes/random
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
import json
import os


class ChuckNorrisView(APIView):
    def get(self, request):
        response = []
        for i in range(25):
            response.append(requests.get(os.environ.get("URL")).json())
        count = len(response)
        return Response({
            'count': count,
            'results': response},
            status=status.HTTP_200_OK)
