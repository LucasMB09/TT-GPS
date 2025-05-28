import time
import serial

class ComGps:
    def __init__(self, module):
        self.module = module

    def sendCommand(self, command, wait=1):
        try:
            print(f"[INFO] Comando enviado: {command}")
            self.module.ser.write((command + '\r\n').encode())
            
            # Leer las líneas de respuesta
            lines = self.module.ser.readlines()

            # Si no se reciben líneas, se intenta reconectar
            if not lines:
                print("[ERROR] No se recibieron datos. Intentando reconectar...")
                self.reconnect()
                return None

            # Decodificar las líneas de respuesta
            decoded_lines = [line.decode('utf-8').strip() for line in lines]
            print(f"[INFO] Respuesta completa: {decoded_lines}")

            if command == "AT":
                for line in decoded_lines:
                    if line == "OK":
                        print(f"[INFO] RESPUESTA: {line}")
                        return "OK"

            if command == "AT+CGNSINF":
                # Asegurarse de que la respuesta tenga la cantidad esperada de datos
                if len(decoded_lines) > 0:
                    resultado = str(decoded_lines)[1:-1].split(",")
                    lat = resultado[4]
                    long = resultado[5]
                    velocidad = resultado[7]
                    print(f"[DEBUG] Resultado: {resultado}")
                    print(f"[DEBUG] LATITUD: {lat} y LONGITUD: {long}")
                    print(f"[DEBUG] VELOCIDAD: {velocidad}")
                    return lat, long, velocidad
                else:
                    print("[ERROR] No se recibió la información esperada para la ubicación.")
                    return None

            else:
                print("[INFO] Comando no reconocido o no manejado específicamente.")
                return decoded_lines

        except serial.SerialException as e:
            print(f"[ERROR] Error de comunicación serial: {e}")
            self.reconnect()  # Intentar reconectar si hay un error de comunicación
            return None
        except IndexError:
            print("[ERROR] Error al procesar la respuesta, índice fuera de rango.")
            return None
        except Exception as e:
            print(f"[ERROR] Ocurrió un error inesperado: {e}")
            return None

    def reconnect(self):
        """Intenta cerrar y volver a abrir la conexión serial para reconectar."""
        try:
            print("[INFO] Intentando reconectar...")
            self.module.ser.close()
            time.sleep(2)  # Darle tiempo al dispositivo para reiniciarse
            self.module.ser.open()
            print("[INFO] Reconexión exitosa.")
        except Exception as e:
            print(f"[ERROR] No se pudo reconectar: {e}")
