from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .pagination import Pagination
from rest_framework import status
from django.http import JsonResponse

def get_function(request, list_animals):
    try:
        paginator = Pagination()
        result_page = paginator.paginate_queryset(list_animals, request)
        serializer = AnimalSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception:
        return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def post_function(request, serializer):
    try:
        serializer = serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return JsonResponse({'mensagem':'Ocorreu um erro no servidor'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnimalListView(APIView):
    def get(self, request, mode):
        list_animals = AnimalList.objects.filter(mode=mode).order_by('-id')
        return get_function(request, list_animals)
            
    def post(self, request):
        try:
            serializer = AnimalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem':'Ocorreu um erro no servidor'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

            
class AnimalDetails(APIView):
    def get(self, request, id):
        try:
            if id == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            animal = AnimalList.objects.get(pk=id)
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        except AnimalList.DoesNotExist:
            return JsonResponse({'mensagem': "O animal não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def put(self, request, id):
        try:
            if id == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                        status=status.HTTP_400_BAD_REQUEST)
            animal = AnimalList.objects.get(pk=id)
            serializer = AnimalSerializer(animal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        except AnimalList.DoesNotExist:
            return JsonResponse({'mensagem': "O anúncio não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(self, request, id):
        try:
            if id == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                        status=status.HTTP_400_BAD_REQUEST)
            animal = AnimalList.objects.get(pk=id)
            animal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AnimalList.DoesNotExist:
            return JsonResponse({'mensagem': "O anúncio não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)