

# Strings

print("Hola mundo")
print('Necesito ayuda')
print("Nuestro" + "Mundo")

# Bool

isActive = True
isEnabled = False

print("¿El boton esta habilitado?",isEnabled)

# Numeros : enteros, reales, complejos

a = 5
b = 4.6
c = 45 + 23j

print("Es la parte real ", c.real)
print("Es la parte imaginaria ", c.imag)

# Listas

listaVacia = list()
listaVacia2 = []

edades = [14, 15, 17, 18]
distritos = ["Miraflores", "Barranco", "Santiago de Surco", "Villa el Salvador"]
distritos.append("San Juan de Miraflores")

print("Cantidad de jovenes:", edades)
print("Lugares de Lima", distritos)
print("La cantidad de distritos es", len(distritos))

# Tuplas

tuplaVacia = ()
regiones = ('Piura', 'Amazonas', 'Ucayali')
print("Departamentos del Perú:", type(regiones))

# Dictionaries

dictVacio = {}
dictVacio2 = dict()

z = dict(A = 2, B = -5)
user = { "nombre": "mateo", 
        "genero": "masculino", 
        "edad": 20 ,
        "altura": 1.75,
        "admin": False,
        "estado": None,
        "regiones": regiones,
        "distritos": distritos}

print("mostrar diccionarios", user)