from modules.configGPS import *
from modules.comunicacionGPS import *
from queries.gpsQueries import *
from config import *
import subprocess
import time

#def encenderPPP():
#    try:
#        print("[DEBUG] Conectando al GPRS")
#        subprocess.Popen(["sudo", "nohup", "sh", "/home/admin/scriptsPPP/startPPP.sh", ">", "/home/admin/scriptsPPP/startPPP.log", "2>&1", "&"])
#        print("[DEBUG] Conexion establecida")
#    except subprocess.CalledProcessError as e:
#        print("[ERROR] Error en conexion:", e)

#def apagarPPP():
#    try:
#        print("[DEBUG] Desconectando GPRS")
#        subprocess.Popen(["sudo", "nohup", "sh", "/home/admin/scriptsPPP/stopPPP.sh", ">", "/home/admin/scriptsPPP/stopPPP.log", "2>&1", "&"])
#        print("[DEBUG] Conexion finalizada")
#    except subprocess.CalledProcessError as e:
#        print("[ERROR] Error al terminar la conexion:", e)

if __name__ == "__main__":
    #encenderPPP()
    #apagarPPP()
    #time.sleep(5)
    sim808 = SIM808(PORT_RB, BAUDRATE)
    comunicacion = ComGps(sim808)
    comunicacion.sendCommand("AT")
    comunicacion.sendCommand("AT+CGNSPWR=1")
#    while(1):
    lat, long, velocidad = comunicacion.sendCommand("AT+CGNSINF")
    print(f"[DEBUG] Lat: {lat}, Long: {long}")
    #encenderPPP()
    #time.sleep(8)
    #time.sleep(40)
    insertar_datos(lat, long, velocidad)
