# Elif Yurdakul
# HomeGuard smart home monitoring simulator
import random
from datetime import datetime

def initialize_sensors():
    sensors = [
        {
            "type": "motion",
            "location": "living room",
            "current_value": "no activity"
        },
    {
        "type": "door",
        "location": "front door",
        "current_value": "closed"
    },
    {
        "type": "temperature",
        "location": "kitchen",
        "current_value": 68
    },
    {
        "type": "smoke",
        "location": "bedroom",
        "current_value": "clear"
    }
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

sensors = initialize_sensors()
sensors[3]["current_value"] = "smoke detected"
print(is_abnormal(sensors[3], "HOME"))

sensors[1]["current_value"] = "open"
print(is_abnormal(sensors[1], "AWAY"))
print(is_abnormal(sensors[1], "HOME"))

sensors[2]["current_value"] = 60
print(is_abnormal(sensors[2], "HOME"))
print(is_abnormal(sensors[2], "AWAY"))

def generate_reading(sensor):
    if sensor["type"] == "motion":
        return random.choice(["no activity", "activity detected"])
    elif sensor["type"] == "door":
        return random.choice(["closed", "open"])
    elif sensor["type"] == "temperature":
        return random.randint(30, 100)
    elif sensor["type"] == "smoke":
        return random.choice(["clear", "smoke detected"])

sensors[0]["current_value"] = generate_reading(sensors[0])
print(sensors[0]["current_value"])

print(is_abnormal(sensors[0], "AWAY"))

def process_sensor(sensor, mode):
    sensor["current_value"] = generate_reading(sensor)
    return is_abnormal(sensor, mode)

def trigger_alert(sensor, mode):
    time_now = datetime.now().strftime("%H:%M:%S")
    log_event(f"Sending notification to homeowner about {sensor['type']} at {sensor['location']}")
    print(f"[ALERT!] [{time_now}] {sensor['location']} {sensor['type']} in {mode} mode")


def log_event(message):
    time_now = datetime.now().strftime("%H:%M:%S")
    event = {"time": time_now, "message": message}
    system_state["alerts"].append(event)
    print(f"[LOG] [{time_now}] {message}")
    
if process_sensor(sensors[0], "AWAY"):
    trigger_alert(sensors[0], "AWAY")