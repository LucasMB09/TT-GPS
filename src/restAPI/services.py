import requests
import time
import sys
sys.path.append("../modules")  # Para importar desde modules
from modules.comunicacionGps import *
from modules.configSIM808 import *

def obtener_coordenadas():
    sim808 = SIM808(PORT_RB, BAUDRATE)
    comunicacion = ComGps(sim808)
    comunicacion.sendCommand("AT")
    comunicacion.sendCommand("AT+CGNSPWR=1")
    lat, long = comunicacion.sendCommand("AT+CGNSINF")
    return lat, lon

def enviar_a_api(lat, lon):
    url = "http://48.217.85.175:8000/enviar"
    data = {
        "lat": lat,
        "lon": lon,
    }
    try:
        response = requests.post(url, json=data)
        print(f"[INFO] Enviado: {data}, Respuesta: {response.json()}")
    except Exception as e:
        print(f"[ERROR] Error al enviar: {e}")

if __name__ == "__services__":
    while True:
        lat, lon = obtener_coordenadas()
        enviar_a_api(lat, lon)
        time.sleep(60)
