# Elif Yurdakul
# HomeGuard smart home monitoring simulator
import random
from datetime import datetime

class Sensor:
    def __init__(self, sensor_id, location, sensor_type, current_value):
        self.sensor_id = sensor_id
        self.location = location
        self.sensor_type = sensor_type
        self.current_value = current_value
        self.initial_value = current_value

    def read(self):
        return self.current_value

    def isAbnormal(self, mode):
        sensor_data = {
            "type": self.sensor_type,
            "location": self.location,
            "current_value": self.current_value
        }
        return is_abnormal(sensor_data, mode)
        
    def reset(self):
        self.current_value = self.initial_value

def initialize_sensors():
    sensors = [
        Sensor("MOTION-1", "living room", "motion", "no activity"),
        Sensor("DOOR-1", "front door", "door", "closed"),
        Sensor("TEMP-1", "kitchen", "temperature", 68),
        Sensor("SMOKE-1", "bedroom", "smoke", "clear")
    ]
    return sensors


alerts = []

system_state = {
    "mode": "AWAY",
    "alerts": alerts
}

def is_abnormal(sensor, mode):
        if sensor["type"] == "motion" and sensor["current_value"] == "activity detected" and mode == "AWAY":
            return True
        elif sensor["type"] == "door" and sensor["current_value"] == "open" and mode == "AWAY":
            return True
        elif sensor["type"] == "temperature" and (sensor["current_value"] < 35 or sensor["current_value"] >95):
            return True
        elif sensor["type"] == "temperature" and mode == "HOME" and (sensor["current_value"] < 65 or sensor["current_value"] > 75):
            return True
        elif sensor["type"] == "smoke" and sensor["current_value"] == "smoke detected":
            return True
        return False

def generate_reading(sensor):
    if sensor.sensor_type == "motion":
        return random.choice(["no activity", "activity detected"])
    elif sensor.sensor_type == "door":
        return random.choice(["closed", "open"])
    elif sensor.sensor_type == "temperature":
        return random.randint(30, 100)
    elif sensor.sensor_type == "smoke":
        return random.choice(["clear", "smoke detected"])

sensors = initialize_sensors()

def process_sensor(sensor, mode):
    sensor.current_value = generate_reading(sensor)
    return sensor.isAbnormal(mode)

def display_reading(sensor, alert_needed):
    location = sensor.location.title()
    value = sensor.read()

    if sensor.sensor_type == "motion":
        label = f"{location} Motion"
        value = str(value).capitalize()
    elif sensor.sensor_type == "door":
        label = location
        value = str(value).upper()
    elif sensor.sensor_type == "temperature":
        label = f"{location} Temperature"
        status = "Abnormal" if alert_needed else "Normal"
        value = f"{value}°F ({status})"
    else:
        label = f"{location} Smoke"
        value = str(value).upper()

    print(f"[READING] {label}: {value}")

def trigger_alert(sensor, mode):
    time_now = datetime.now().strftime("%H:%M:%S")
    location = sensor.location.title()

    if sensor.sensor_type == "motion":
        severity = "HIGH"
        category = "SECURITY"
        detail = f"Motion detected in {location} while in {mode} mode!"
    elif sensor.sensor_type == "door":
        severity = "HIGH"
        category = "SECURITY"
        detail = f"{location} opened while in {mode} mode!"
    elif sensor.sensor_type == "smoke":
        severity = "HIGH"
        category = "SAFETY"
        detail = f"Smoke detected in {location}!"
    elif sensor.current_value < 35 or sensor.current_value > 95:
        severity = "HIGH"
        category = "SAFETY"
        detail = f"Temperature {sensor.current_value}°F in {location}!"
    else:
        severity = "NOTICE"
        category = "COMFORT"
        detail = f"Temperature {sensor.current_value}°F is outside the comfort range in {location}."

    print(f"[ALERT!] 🚨 {severity}: {category}: {detail}")
    log_event("Sending notification to homeowner...")

def log_event(message):
    time_now = datetime.now().strftime("%H:%M:%S")
    event = {"time": time_now, "message": message}
    system_state["alerts"].append(event)
    print(f"[LOG] [{time_now}] {message}")
    
print("=== HomeGuard Security System ===")

for mode in ["AWAY", "HOME", "SLEEP"]:
    system_state["mode"] = mode
    print(f"\nTime: {datetime.now().strftime('%H:%M:%S')}")
    print(f"Mode: {system_state['mode']}")

    for sensor in sensors:
        alert_needed = process_sensor(sensor, system_state["mode"])
        display_reading(sensor, alert_needed)

        if alert_needed:
            trigger_alert(sensor, system_state["mode"])

print("\n=== Fixed Checks ===")

test_door = Sensor("TEST-D1", "front door", "door", "open")
print("Door in AWAY:", test_door.isAbnormal("AWAY"))
print("Door in HOME:", test_door.isAbnormal("HOME"))

test_smoke = Sensor("TEST-S1", "bedroom", "smoke", "smoke detected")
print("Smoke in HOME:", test_smoke.isAbnormal("HOME"))

test_temp = Sensor("TEST-T1", "kitchen", "temperature", 80)
print("80°F in HOME:", test_temp.isAbnormal("HOME"))
print("80°F in AWAY:", test_temp.isAbnormal("AWAY"))

edge_temp = Sensor("TEST-T2", "kitchen", "temperature", 35)
print("35°F in AWAY:", edge_temp.isAbnormal("AWAY"))

print("Door in SLEEP:", test_door.isAbnormal("SLEEP"))
print("Smoke in SLEEP:", test_smoke.isAbnormal("SLEEP"))