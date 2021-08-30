import bcrypt
import jwt

from django.db.models.query import RawQuerySet
from django.http import request
from django.shortcuts import render
from django.db import connection

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from boardapi.models import Board, Member
from boardapi.serializers import BoardSerializer, MemberSerializer
from rest_framework.decorators import api_view

from collections import namedtuple

def namedtuplefetchall(cursor):
    desc = cursor.description
    fields =  [col[0] for col in desc]
    nt_result = namedtuple('Result',fields)
    return [nt_result(*row) for row in cursor.fetchall()]



@api_view(['POST'])
def sign(request):
    with connection.cursor() as cursor:
        try:
            body = JSONParser().parse(request)
            body['password'] = (bcrypt.hashpw(body['password'].encode('utf-8'), bcrypt.gensalt(8))).decode('utf-8')
            print(body['password'])
            cursor.execute("insert into member(userid, password) values(%s,%s)",[body['userid'], body['password']])
            return JsonResponse({"result" : "success"}, status=status.HTTP_200_OK)
            #return JsonResponse({"result" : "failed"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()

@api_view(['POST'])
def login(request):
    with connection.cursor() as cursor:
        try:
            body = JSONParser().parse(request)
            cursor.execute("select * from member where userid = %s", [body['userid']])
            rows = namedtuplefetchall(cursor)
            print(rows)
            print(rows[0].userid)
            if (bcrypt.checkpw(body['password'].encode('utf-8'),rows[0].password.encode('utf-8'))) :
                access_token = jwt.encode({'userid':rows[0].userid, 'exp' : 1000 * 60 * 60 * 365}, 'secretkey', algorithm='HS256')
                return JsonResponse({"result" : access_token}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"result" : "password incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()