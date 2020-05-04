from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import IngredienteSerializer, HamburguesaSerializer
from .models import Ingrediente, Hamburguesa
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')




@csrf_exempt
def lista_ingredientes(request):

    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IngredienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            print(data)
            respuesta="Atributos inválidos, para crear un ingrediente válido especificar su nombre y descripción"
            return JsonResponse({"message":respuesta}, status=400)

    else:
        respuesta="el método "+request.method+" no está definido para este path"
        return JsonResponse({"message": respuesta}, status=404)



@csrf_exempt
def lista_hamburguesas(request):

    if request.method == 'GET':
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HamburguesaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            respuesta="Atributos inválidos, para crear una hamburguesa válida debe especificar al menos su nombre, descripción e imagen "
            return JsonResponse({"message":respuesta}, status=400)

    else:
        respuesta="el método "+request.method+" no está definido para este path"
        return JsonResponse({"message": respuesta}, status=404)



@csrf_exempt
def detalle_ingrediente(request, id):

    metodos_permitidos = ['GET', 'PATCH', 'DELETE']
    if request.method not in metodos_permitidos:
        respuesta = "el método " + request.method + " no está definido para este path"
        return JsonResponse({"message": respuesta}, status=404)

    try:
        ingrediente = Ingrediente.objects.get(id=id)
    except Ingrediente.DoesNotExist:
        return JsonResponse({"message": "no existe ingrediente con ese id"}, status=404)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = IngredienteSerializer(ingrediente, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        for hamburguesa in Hamburguesa.objects.all():
            ingredientes=hamburguesa.ingredientes_hamburguesa.all()
            if ingrediente in ingredientes:
                return JsonResponse({"message": "no se puede borrar ingrediente por que está en una hamburguesa"}, status=404)
        ingrediente.delete()
        return JsonResponse({"message": "ingrediente borrado"}, status=204)



@csrf_exempt
def detalle_hamburguesa(request, id):

    metodos_permitidos = ['GET', 'PATCH','DELETE']
    if request.method not in metodos_permitidos:
        respuesta = "el método " + request.method + " no está definido para este path"
        return JsonResponse({"message": respuesta}, status=404)

    try:
        hamburguesa = Hamburguesa.objects.get(id=id)
    except Hamburguesa.DoesNotExist:
        return JsonResponse({"message": "no existe hamburguesa con ese id"}, status=404)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = HamburguesaSerializer(hamburguesa, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        hamburguesa.delete()
        return JsonResponse({"message": "hamburguesa borrada"}, status=204)



@csrf_exempt
def preparacion(request, id, idi):

    metodos_permitidos=['PUT', 'DELETE']
    if request.method not in metodos_permitidos:
        respuesta = "el método " + request.method + " no está definido para este path"
        return JsonResponse({"message": respuesta}, status=404)

    try:
        hamburguesa = Hamburguesa.objects.get(id=id)
    except Hamburguesa.DoesNotExist:
        return JsonResponse({"message": "no existe hamburguesa con ese id"}, status=404)

    try:
        ingrediente = Ingrediente.objects.get(id=idi)
    except Ingrediente.DoesNotExist:
        return JsonResponse({"message": "no existe ingrediente con ese id"}, status=404)

    if request.method == 'PUT':
        hamburguesa.ingredientes_hamburguesa.add(ingrediente)
        serializer = HamburguesaSerializer(hamburguesa)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        ingredientes_hamburguesa = hamburguesa.ingredientes_hamburguesa.all()
        if ingrediente in ingredientes_hamburguesa:
            hamburguesa.ingredientes_hamburguesa.remove(ingrediente)
            serializer = HamburguesaSerializer(hamburguesa)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({"message": "el ingrediente no era parte de la hamburguesa"}, status=400)




