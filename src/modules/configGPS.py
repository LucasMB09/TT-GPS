import serial
import time

class SIM808:
	def __init__(self, port='/dev/ttySO', baudrate=112500, timeout=0.1):
		print("[INFO] SE INICIALIZO EL MODULO DE CONFIGURACION")
		self.ser = serial.Serial(port, baudrate, timeout = timeout)
		time.sleep(1)
