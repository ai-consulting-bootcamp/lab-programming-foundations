# HomeGuard — Evidencia del laboratorio

## Archivo del programa
C:\Users\rafae\OneDrive\Documentos\lab-programming-foundations\homeguard_system.py

## Comando para ejecutarlo
python homeguard_system.py

## Casos fijos y resultados

Caso fijo: sensor de humo del dormitorio activado (True), modo AWAY.
Esperado: alerta CRÍTICA por posible riesgo de incendio.
Obtenido: el programa mostró la alerta CRÍTICA:
“Humo detectado en Dormitorio: posible riesgo de incendio”.

Salida del simulador (3 iteraciones):

Time: 06:18:00 | Iteración 1
Mode: AWAY
[READING] Sala movimiento: False
[READING] Entrada puerta: ABIERTA
[ALERT] ALTA: Puerta abierta en Entrada mientras la casa está en modo AWAY
[READING] Cocina temperatura: 60
[READING] Dormitorio humo: True
[ALERT] CRITICA: Humo detectado en Dormitorio: posible riesgo de incendio

Time: 06:18:00 | Iteración 2
Mode: AWAY
[READING] Sala movimiento: True
[ALERT] ALTA: Movimiento detectado en Sala mientras la casa está en modo AWAY
[READING] Entrada puerta: CERRADA
[READING] Cocina temperatura: 46
[READING] Dormitorio humo: False

Time: 06:18:00 | Iteración 3
Mode: AWAY
[READING] Sala movimiento: False
[READING] Entrada puerta: CERRADA
[READING] Cocina temperatura: 48
[READING] Dormitorio humo: True
[ALERT] CRITICA: Humo detectado en Dormitorio: posible riesgo de incendio

## Explicación
Mi programa trabaja con sensores de movimiento, puertas, temperatura y humo. En cada vuelta revisa qué está pasando y, si encuentra algo fuera de lo normal, muestra una alerta y la anota. También usé la clase Sensor para guardar los datos de cada sensor y revisar o cambiar sus lecturas.

## Caso límite
Un caso límite es cuando la temperatura está justo en 35 °F o 95 °F. El programa solo genera alertas si baja de 35 °F o supera los 95 °F, así que esos valores exactos no generan una alerta. Esto evita avisos cuando la lectura está justo en el límite establecido.