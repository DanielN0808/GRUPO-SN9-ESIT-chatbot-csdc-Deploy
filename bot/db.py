import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def register_request(user_id, nombre, correo, tipo_solicitud, detalle):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO requests (user_id, nombre, correo, tipo_solicitud, detalle)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (user_id, nombre, correo, tipo_solicitud, detalle))

    conn.commit()
    cursor.close()
    conn.close()
