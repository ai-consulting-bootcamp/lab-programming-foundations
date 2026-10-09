
import random
from datetime import datetime


# 1. SENSOR CLASS

class Sensor:

    def __init__(self, name, sensor_type):
        self.name = name
        self.sensor_type = sensor_type
        self.value = None

    def read(self, value):
        self.value = value

    def isAbnormal(self):
        if self.value is None:
            return False

        if self.sensor_type == "temperature":
            return self.value < 35 or self.value > 95
        else:
            return self.value == True

    def reset(self):
        self.value = None


# 2. SYSTEM SETTINGS

system = {"mode": "AWAY"}
alerts = []
event_log = []


# 3. CREATE SENSORS

def initialize_system():
    return {
        "temperature": Sensor("Kitchen", "temperature"),
        "smoke": Sensor("Hallway", "smoke"),
        "motion": Sensor("Living Room", "motion"),
        "door": Sensor("Front Door", "door")
    }


# 4. LOG EVENTS AND ALERTS

def log_event(message):
    time = datetime.now().strftime("%H:%M:%S")
    entry = time + " - " + message
    event_log.append(entry)
    print(entry)


def show_alert(message):
    alerts.append(message)
    log_event("ALERT: " + message)


# 5. GENERATE RANDOM READINGS

def generate_readings():
    return {
        "temperature": random.randint(20, 110),
        "smoke": random.choice([True, False]),
        "motion": random.choice([True, False]),
        "door": random.choice([True, False])
    }


# 6. CHECK SENSOR READINGS

def process_readings(sensors, door_minutes):

    mode = system["mode"]

    temp = sensors["temperature"].value
    smoke = sensors["smoke"].value
    motion = sensors["motion"].value
    door = sensors["door"].value

    # Temperature safety
    if temp < 35:
        show_alert("Frozen pipe risk!")
    elif temp > 95:
        show_alert("Equipment failure risk!")

    # Smoke safety
    if smoke:
        show_alert("Smoke detected!")

    # Security in AWAY mode
    if mode == "AWAY":
        if motion:
            show_alert("Motion detected while away!")
        if door:
            show_alert("Door opened while away!")

    # Motion and door together
    if motion and door:
        show_alert("Motion and door triggered together!")

    # Comfort in HOME mode
    if mode == "HOME":
        if temp < 65 or temp > 75:
            show_alert("Temperature outside comfort range!")

    # Door open too long
    if door and door_minutes > 5:
        show_alert("Door open longer than 5 minutes!")


# 7. RUN THE SIMULATION

def run_simulation():

    sensors = initialize_system()

    # Fixed readings for predictable tests
    test_readings = [
        [68, False, False, False],
        [30, True, True, True],
        [100, False, False, True]
    ]

    modes = ["HOME", "AWAY", "SLEEP"]
    door_times = [0, 2, 6]

    for i in range(3):

        system["mode"] = modes[i]

        print("\n--- SCAN", i + 1, "---")
        print("Mode:", system["mode"])

        readings = test_readings[i]

        sensors["temperature"].read(readings[0])
        sensors["smoke"].read(readings[1])
        sensors["motion"].read(readings[2])
        sensors["door"].read(readings[3])

        for sensor in sensors.values():
            print(sensor.name, ":", sensor.value)

        process_readings(sensors, door_times[i])

    # Show that random readings also work
    print("\n--- RANDOM READINGS ---")
    random_readings = generate_readings()
    print(random_readings)

    # Test the reset method
    print("\n--- RESET TEST ---")
    sensors["temperature"].reset()
    print("After reset:", sensors["temperature"].value)
    print("Abnormal:", sensors["temperature"].isAbnormal())

    # Final summary
    print("\n--- SUMMARY ---")
    print("Total alerts:", len(alerts))
    print("Total logged events:", len(event_log))


# 8. START HOMEGUARD

run_simulation()
