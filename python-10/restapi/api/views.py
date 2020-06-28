from django.shortcuts import render
from collections import Counter
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

@api_view(["POST"])
def lambda_function(request):
    try :
        question = request.data.get('question')
        response = orderedNumbers(question)
        return Response(response, status=status.HTTP_200_OK)
    except BadRequest:
        return Response(BadRequest.args[0], status.HTTP_400_BAD_REQUEST)

def orderedNumbers(numbers):
    solution =[item for items, count in Counter(numbers).most_common() for item in [items] * count]
    response = {}
    response['solution'] = solution
    return response
