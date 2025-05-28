import pymysql
from datetime import datetime
from config import IP_MV_LUIS, USER_ULISES, PASSWORD_ULISES

def insertar_datos(latitud, longitud, velocidad):
    connection = None
    try:
        connection = pymysql.connect(
            host=IP_MV_LUIS,
            user=USER_ULISES,
            password=PASSWORD_ULISES,
            database="gps",
            port=3306,
            cursorclass=pymysql.cursors.Cursor  # puedes usar DictCursor si quieres resultados como diccionario
        )

        with connection.cursor() as cursor:
            sql = "INSERT INTO ubicaciones (latitud, longitud, velocidad, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
            val = (latitud, longitud, velocidad, datetime.now().date(), datetime.now().time())
            cursor.execute(sql, val)
        
        connection.commit()
        print("[INFO] Registro insertado")

    except Exception as e:
        print("[ERROR]", e)

    finally:
        if connection:
            connection.close()
