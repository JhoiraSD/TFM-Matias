import folium
import openrouteservice as ors
import math


#Key de la API de "Openrouteservice"
#Para obtener la tuya accede a "https://account.heigit.org/login"
#La API tiene usos limitados que se reinician en un período de tiempo, se aconseja desarrollar el problema previamente a usar la API para reducir el coste de cada optimización
client = ors.Client(key='Your_key')

#Coordenadas de las direcciones a visitar
#Introducir en [Longitud, Latitud]
coords = [
    [-8.453999, 43.369535],
    [-8.420677, 43.352982],
    [-8.479554, 43.352128],
    [-8.503450, 43.310159]
]

#Coordenada de inicio para "vehicles"
#Introducir en [Longitud, Latitud]
vehicle_start = [-8.488493, 43.301399]

#Punto de inicio  de presentación del mapa realizado
#Cambiar la variable "vehicle_start" para alterar el punto de inicio
m = folium.Map(location=list(reversed(vehicle_start)), tiles="cartodbpositron", zoom_start=14)

#Loop para introducir las coordenadas a visitar en el mapa, cambiar la variable "color" para cambiar el color
for coord in coords:
    folium.Marker(location=list(reversed(coord)), icon=folium.Icon(color="orange")).add_to(m)

#Insercion de la coordenada de inicio en el mapa
folium.Marker(location=list(reversed(vehicle_start)), icon=folium.Icon(color="green")).add_to(m)

#Vehiculos a utilizar para la optimización
#La variable "profile" es el tipo de transporte a emplear, determina los caminos que se pueden tomar
#La variable "capacity" es la cantidad que pueden cargar
#Capacidad máxima de 3 vehiculos en la optimización
vehicles = [
    ors.optimization.Vehicle(id=0, profile='driving-car', start=vehicle_start, end=vehicle_start, capacity=[5]),
    ors.optimization.Vehicle(id=1, profile='driving-car', start=vehicle_start, end=vehicle_start, capacity=[5])
]

#Definición de los trabajos a realizar en cada una de las localizaciones,
#De ser necesário se pueden definir de forma indipendiente asignando acada uno una id manualmente u un "amount"
#La variable "amount" es la carga que tienen que recoger los vehiculos
#Es posible definir otros parámetros como la franja de tiempo disponible, el tiempo necesário o localizaciones previas visitadas
jobs = [ors.optimization.Job(id=index, location=coords, amount=[1]) for index, coords in enumerate(coords)]

#Uso de la API para hacer la optimización del problema
#Se pueden guardar de forma independiente 
optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)

#Representación de las rutas de la optimización
line_colors = ['green', 'orange', 'blue', 'yellow']
for route in optimized['routes']:
    folium.PolyLine(locations=[list(reversed(coords)) for coords in ors.convert.decode_polyline(route['geometry'])['coordinates']], color=line_colors[route['vehicle']]).add_to(m)

#Guardado del mapa resultante, es posible ejecutarlo directamente en navegador
m.save('resultado.html')

