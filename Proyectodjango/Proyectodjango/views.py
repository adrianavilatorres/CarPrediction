from django.http import HttpResponse
from django.shortcuts import render
import joblib
import numpy as np

def formulario(request): #primera vista
    return render(request, "formulario.html")

def respuesta(request): 
    combustible = request.GET["fuelType"]
    km = request.GET["km"]
    marca = request.GET["Marca"]
    modelo = request.GET["Modelo"]
    transmision = request.GET["transmissionType"]
    year = request.GET["year"]
    cc = request.GET["cubicCapacity"]
    puertas = request.GET["doors"]
    caballos = request.GET["hp"]
    
    
    datos = np.array([[combustible, km, marca, modelo, transmision, year, cc, puertas, caballos]])
    
    
    prediccion1 = joblib.load("C:/Users/dridi/Desktop/BDYIA/Programacion de inteligencia artificial/prediccion coches/Proyectodjango/Proyectodjango/modelos/modelo1.joblib")
    X1 = prediccion1.predict(datos)
    primerPrecio = round(int(X1), 2)
    
    prediccion2 = joblib.load("C:/Users/dridi/Desktop/BDYIA/Programacion de inteligencia artificial/prediccion coches/Proyectodjango/Proyectodjango/modelos/modelo2.joblib")
    X2 = prediccion2.predict(datos)
    segundoPrecio = round(int(X2), 2)
    
    prediccion3 = joblib.load("C:/Users/dridi/Desktop/BDYIA/Programacion de inteligencia artificial/prediccion coches/Proyectodjango/Proyectodjango/modelos/modelo3.joblib")
    X3 = prediccion3.predict(datos)
    tercerPrecio = round(int(X3), 2)
    
    prediccion4 = joblib.load("C:/Users/dridi/Desktop/BDYIA/Programacion de inteligencia artificial/prediccion coches/Proyectodjango/Proyectodjango/modelos/modelo4.joblib")
    X4 = prediccion4.predict(datos)
    cuartoPrecio = round(int(X4), 2)
    
    respuesta = 'Prediccion con el primer modelo: {}, prediccion con el segundo modelo: {}, prediccion con el tercer modelo: {}, prediccion con el cuarto modelo: {}'.format(primerPrecio, segundoPrecio, tercerPrecio, cuartoPrecio)
    
    
    
    return HttpResponse(respuesta)