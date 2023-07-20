from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from taller.models import Inscrito
from taller.serializers import InscritoSerial
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


def index(request):
    return render(request, 'index.html')

# sin f 

def ver_json(request):
    miembro = Inscrito.objects.all()
    data = {'miembro' : list(miembro.values('nombre', 'telefono', 'estado', 'observacion'))}

    return JsonResponse(data)

# clase 

class MiembroList(APIView):
    def get(self, request):
        inscritos=Inscrito.objects.all()
        serial = InscritoSerial(inscritos, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = InscritoSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class MiembroDetalle(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscritos = self.get_object(pk)
        serial = InscritoSerial(inscritos)
        return Response(serial.data)

    def put(self, request, pk):
        inscritos = self.get_object(pk)
        serial = InscritoSerial(inscritos, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, pk):
        inscritos = self.get_object(pk)
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#funcion 

@api_view(['GET', 'POST'])
def miembros_list(request):
    if request.method == 'GET':
        inscritos = Inscrito.objects.all()
        serial = InscritoSerial(inscritos, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InscritoSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def miembros_detalle(request, id):
    try:
        inscritos = Inscrito.objects.get(pk=id)
    except Inscrito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InscritoSerial(inscritos)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InscritoSerial(inscritos, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
