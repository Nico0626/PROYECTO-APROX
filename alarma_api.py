import mysql.connector
import paho.mqtt.client as mqtt

# Configuración de la conexión a MySQL
db = mysql.connector.connect(
    host="localhost",         
    user="root",   
    password="NM260621",  
    database="alarma_db"        
)

# Cursor para ejecutar comandos SQL
cursor = db.cursor()

# Función para insertar datos en la base de datos
def insertar_datos(estado):
    sql = "INSERT INTO estado (movimiento) VALUES (%s)"
    val = (estado,)
    cursor.execute(sql, val)
    db.commit()
    print(f"Estado de la alarma={estado}")

# Funciones para manejar los eventos MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT")
        # Suscribirse al tema de nivel de agua
        client.subscribe("alarma")  
    else:
        print(f"Error al conectar al broker. Código de error: {rc}")

def on_message(client, userdata, msg):
    try:
        # Convertir el mensaje en un valor numérico
        estado = msg.payload.decode()
        print(f"Estado de la alarma: {estado} ")
        # Insertar el dato en la base de datos
        insertar_datos(estado)
    except ValueError:
        print("Error en el formato del mensaje recibido")

# Configuración del cliente MQTT
MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_CLIENT_ID = "api"

client = mqtt.Client(client_id=MQTT_CLIENT_ID, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker
client.connect(MQTT_BROKER)

# Mantener el script en ejecución
client.loop_forever()


