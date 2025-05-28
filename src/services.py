import requests
import time
from modules.configGPS import *
from modules.comunicacionGPS import *
from config import *


def obtener_coordenadas():
    sim808 = SIM808(PORT_RB, BAUDRATE)
    comunicacion = ComGps(sim808)
    comunicacion.sendCommand("AT")
    comunicacion.sendCommand("AT+CGNSPWR=1")
    lat, lon = comunicacion.sendCommand("AT+CGNSINF")
    return lat, lon

def enviar_a_api(lat, lon):
    url = "http://20.119.72.237:8000/enviar"
    data = {
        "lat": lat,
        "lon": lon,
    }
    try:
        response = requests.post(url, json=data)
        print(f"[INFO] Enviado: {data}, Respuesta: {response.json()}")
    except Exception as e:
        print(f"[ERROR] Error al enviar: {e}")

if __name__ == "__main__":
    lat, lon = obtener_coordenadas()
    enviar_a_api(lat, lon)
    time.sleep(60)
