from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json
import boto3
import pprint

from django.http import HttpResponse

sns = boto3.client('sns')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

'''
GET and POST endpoint for Amazon SNS
'''
@api_view(['GET', 'POST'])
def analytics(request):
    obj = json.loads(request.body)
    print(obj["url"])
    return JsonResponse({'message':'Message received'},
                        status=status.HTTP_200_OK) 


