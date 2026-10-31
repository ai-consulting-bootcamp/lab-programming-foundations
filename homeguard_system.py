# Rafael Jurado Ortiz
# Simulador de monitoreo para el hogar HomeGuard

import random
from datetime import datetime

class Sensor:
    def __init__(self, id, ubicacion, tipo, valor_actual):
        self.id = id
        self.ubicacion = ubicacion
        self.tipo = tipo
        self.valor_actual = valor_actual

    def read(self):
        return self.valor_actual

    def isAbnormal(self):
        if self.tipo == "movimiento":
            return self.valor_actual is True
        elif self.tipo == "puerta":
            return self.valor_actual == "ABIERTA"
        elif self.tipo == "temperatura":
            return self.valor_actual < 35 or self.valor_actual > 95
        elif self.tipo == "humo":
            return self.valor_actual is True
        return False

    def reset(self):
        if self.tipo == "movimiento":
            self.valor_actual = False
        elif self.tipo == "puerta":
            self.valor_actual = "CERRADA"
        elif self.tipo == "temperatura":
            self.valor_actual = 68
        elif self.tipo == "humo":
            self.valor_actual = False



def inicializar_sensores():
    sensores = [
        
        Sensor("M1", "Sala", "movimiento", False),
        Sensor("P1", "Entrada", "puerta", "CERRADA"),
        Sensor("T1", "Cocina", "temperatura", 68),
        Sensor("H1", "Dormitorio", "humo", False)
    ]
    return sensores


def crear_alerta(tipo, severidad, mensaje):
    return {
        "tipo": tipo,
        "severidad": severidad,
        "mensaje": mensaje,
        "hora": datetime.now().strftime("%H:%M:%S")
    }

print(crear_alerta("seguridad", "alta", "Movimiento detectado"))

def revisar_movimiento(sensor, modo):
    if sensor.tipo == "movimiento" and sensor.isAbnormal() and modo == "AWAY":
        return crear_alerta(
            "seguridad",
            "alta",
            f"Movimiento detectado en {sensor.ubicacion} mientras la casa está en modo AWAY"
        )
    return None


sensor_prueba = Sensor("M1", "Sala", "movimiento", True)
print(revisar_movimiento(sensor_prueba, "AWAY"))

def revisar_temperatura(sensor):
    temperatura = sensor.valor_actual

    if temperatura < 35:
        return crear_alerta(
            "seguridad",
            "alta",
            f"Temperatura baja en {sensor.ubicacion}: riesgo de tuberías congeladas"
        )
    elif temperatura > 95:
        return crear_alerta(
            "seguridad",
            "alta",
            f"Temperatura alta en {sensor.ubicacion}: posible riesgo para el equipo"
        )

    return None

sensor_temperatura = Sensor("T1", "Cocina", "temperatura", 30)

print(revisar_temperatura(sensor_temperatura))

def revisar_humo(sensor):
    if sensor.tipo == "humo" and sensor.valor_actual is True:
        return crear_alerta(
            "seguridad",
            "critica",
            f"Humo detectado en {sensor.ubicacion}: posible riesgo de incendio"
        )
    return None


sensor_humo = Sensor("H1", "Dormitorio", "humo", True)

print(revisar_humo(sensor_humo))

def revisar_puerta(sensor, modo):
    if sensor.tipo == "puerta" and sensor.valor_actual == "ABIERTA" and modo == "AWAY":
        return crear_alerta(
            "seguridad",
            "alta",
            f"Puerta abierta en {sensor.ubicacion} mientras la casa está en modo AWAY"
        )
    return None


sensor_puerta = Sensor("P1", "Entrada", "puerta", "ABIERTA")
print(revisar_puerta(sensor_puerta, "AWAY"))

def registrar_evento(registro, mensaje):
    hora = datetime.now().strftime("%H:%M:%S")
    evento = f"[{hora}] {mensaje}"
    registro.append(evento)
    return evento

eventos = []
print(registrar_evento(eventos, "Prueba del registro"))
print(eventos)

def generar_lectura(sensor):
    if sensor.tipo == "movimiento":
        sensor.valor_actual = random.choice([True, False])
    elif sensor.tipo == "puerta":
        sensor.valor_actual = random.choice(["ABIERTA", "CERRADA"])
    elif sensor.tipo == "temperatura":
        sensor.valor_actual = random.randint(30, 100)
    elif sensor.tipo == "humo":
        sensor.valor_actual = random.choice([True, False])

    return sensor.read()

def procesar_sensor(sensor, modo):
    if sensor.tipo == "movimiento":
        return revisar_movimiento(sensor, modo)
    elif sensor.tipo == "puerta":
        return revisar_puerta(sensor, modo)
    elif sensor.tipo == "temperatura":
        return revisar_temperatura(sensor)
    elif sensor.tipo == "humo":
        return revisar_humo(sensor)
    else:
        return None


sensores = inicializar_sensores()

modo = "AWAY"
registro = []

for iteracion in range(1, 4):
    hora = datetime.now().strftime("%H:%M:%S")
    print(f"\nTime: {hora} | Iteración {iteracion}")
    print(f"Mode: {modo}")

    for sensor in sensores:
        lectura = generar_lectura(sensor)
        print(f"[READING] {sensor.ubicacion} {sensor.tipo}: {lectura}")

        alerta = procesar_sensor(sensor, modo)

        if alerta is not None:
            print(f"[ALERT] {alerta['severidad'].upper()}: {alerta['mensaje']}")
            evento = registrar_evento(registro, alerta["mensaje"])
            print(f"[LOG] {evento}")


print("\n=== Caso fijo: humo detectado en modo AWAY ===")
sensor_fijo = Sensor("H1", "Dormitorio", "humo", True)
alerta_fija = revisar_humo(sensor_fijo)
print(alerta_fija)