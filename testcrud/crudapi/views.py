from django.db.models.query import RawQuerySet
from django.http import request
from django.shortcuts import render
from django.db import connection

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from crudapi.models import Testdjango
from crudapi.serializers import TestdjangoSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def testlist(request):
    try:
        data = Testdjango.objects.all()
        data_group = TestdjangoSerializer(data, many=True)
        return JsonResponse(data_group.data, status=status.HTTP_200_OK, safe=False)
    except Exception as ex:
        print(ex)

@api_view(['GET'])
def testdetail(request):
    try:
        target_id = request.GET.get('id', None)
        data = Testdjango.objects.raw('select * from crudapi_testdjango where id = %s',target_id)
        #print(data.username, data.password)
        detail_serial = TestdjangoSerializer(data, many=True)
        return JsonResponse(detail_serial.data, status=status.HTTP_200_OK, safe=False)
    except Exception as ex:
        print(ex)
 
@api_view(['POST'])
def testcreate(request):
    try:
        body = JSONParser().parse(request)
        create_serial = TestdjangoSerializer(data=body)
        if create_serial.is_valid():
            create_serial.save()
            return JsonResponse({"result": "success"}, status=status.HTTP_200_OK)
        return JsonResponse({"result":"failed"}, status=status.HTTP_400_BAD_REQUEST)   
    except Exception as ex:
        print(ex)
        
@api_view(['POST'])
def testupdate(request):
    try:
        body = JSONParser().parse(request)
        print(body['username'])
        target_id = request.GET.get('id', None)
        #not working in object raw query
        #update_data = Testdjango.objects.raw("update crudapi_testdjango set username=%s where id=%s",[body['username'], target_id])
        #update_serial = TestdjangoSerializer(update_data)
        #print(update_serial)
        #print(update_data)
        update_data = Testdjango.objects.filter(id=target_id).update(username=body['username'])
        print(update_data)
        return JsonResponse({"result":"success"}, status=status.HTTP_200_OK)
    except Exception as ex:
        print(ex)


@api_view(['POST'])
def testdelete(request):
    try:
        body = JSONParser().parse(request)
        #raw_query not working
        #delete_data = Testdjango.objects.raw("delete from crudapi_testdjango where id = %s", [body['id']])
        #delete_serial = TestdjangoSerializer(delete_data)
        #print(delete_serial)
        delete_data = Testdjango.objects.filter(id=body['id']).delete()
        print(delete_data)
        return JsonResponse({"result":"success"}, status=status.HTTP_200_OK)
    except Exception as ex:
        print(ex)