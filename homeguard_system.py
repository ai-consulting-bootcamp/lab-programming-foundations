"""
HomeGuard Security System Simulator
Author: [Bhabishwor]
Description: A smart home monitoring system that processes sensor readings
             and triggers alerts for security, safety, and comfort issues.
"""
 
import random
from datetime import datetime
 
# System configuration
HOME_MODES = ["HOME", "AWAY", "SLEEP"]
ALERT_SEVERITIES = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
 
# Current system state
current_mode = "AWAY"

# %%
#Creating a function to create sensors and alerts

def create_sensor(sensor_id, location, sensor_type, threshold=None):
    sensor = {
        "id": sensor_id,
        "location": location,
        "type": sensor_type,
        "threshold": threshold
    }
    return sensor


# Initializing sensors for the Peterson home
sensors = [
    create_sensor("MOTION_1", "Living Room", "motion"),
    create_sensor("TEMP_1", "Kitchen", "temperature", threshold=75),
    create_sensor("DOOR_1", "Front Door", "door"),
    create_sensor("SMOKE_1", "Bedroom", "smoke")
]
print(sensors)

# %%
#Creating a function to create alerts

def create_alert(severity, message, sensor_id, timestamp):
    alert = {
    "severity": severity,
    "message": message,
    "sensor_id": sensor_id,
    "timestamp": timestamp
}
    return alert

# %%
# Initializing alerts list
alerts = []

# %%
test_alert = create_alert(
    "HIGH",
    "Motion detected",
    "MOTION_1",
    "12:30:00"
)

print(test_alert)

# %%
#Verifying the sensors and alerts

# print(f"Initialized {len(sensors)} sensors")
for sensor in sensors:
    print(sensor)

print(f"Initialized {len(alerts)} alerts")
for alert in alerts:
    print(f"  - {alert['severity']}: {alert['message']} (Sensor: {alert['sensor_id']})")

# %%
print(f"Initialized {len(sensors)} sensors")
for sensor in sensors:
    print(f"  - {sensor['id']}: {sensor['location']} ({sensor['type']})")

# %%
#step 3 : Writing conditional statements to check sensor thresholds and system modes.
def is_abnormal_reading(sensor, reading_value):
    sensor_type = sensor["type"]

    if sensor_type == "temperature":
        return reading_value < 35 or reading_value > 95

    elif sensor_type == "motion":
        return reading_value is True

    elif sensor_type == "door":
        return reading_value == "OPEN"

    elif sensor_type == "smoke":
        return reading_value == "DETECTED"

    else:
        return False

# %%
test_sensor = {
    "id": "TEMP_TEST",
    "location": "Test Room",
    "type": "temperature",
    "threshold": None
}

# %%
test_sensor = {
    "id": "TEMP_TEST",
    "location": "Test Room",
    "type": "temperature",
    "threshold": None
}

print(is_abnormal_reading(test_sensor, 34))
print(is_abnormal_reading(test_sensor, 68))

# %%
#testing other other sensor type to confirm the function is working properly
motion_sensor = create_sensor("MOTION_TEST", "Test Room", "motion")
print(is_abnormal_reading(motion_sensor, True))  
print(is_abnormal_reading(motion_sensor, False))  

door_sensor = create_sensor("DOOR_TEST", "Test Room", "door")
print(is_abnormal_reading(door_sensor, "OPEN"))  
print(is_abnormal_reading(door_sensor, "CLOSED"))  

smoke_sensor = create_sensor("SMOKE_TEST", "Test Room", "smoke")
print(is_abnormal_reading(smoke_sensor, "DETECTED"))  
print(is_abnormal_reading(smoke_sensor, "NOT_DETECTED"))  

# %%
#Determining the severity of alerts based on sensor type and reading value

def should_trigger_security_alert(sensor, reading_value, system_mode):
    sensor_type = sensor["type"]

    # Security alerts only happen when the house is in AWAY mode
    if system_mode != "AWAY":
        return False

    if sensor_type == "motion" and reading_value is True:
        return True

    if sensor_type == "door" and reading_value == "OPEN":
        return True

    return False

#Testing the function with different scenarios
print(should_trigger_security_alert(motion_sensor, True, "AWAY"))
# Expected: True

print(should_trigger_security_alert(motion_sensor, True, "HOME"))
# Expected: False

print(should_trigger_security_alert(door_sensor, "OPEN", "AWAY"))
# Expected: True

print(should_trigger_security_alert(door_sensor, "CLOSED", "AWAY"))
# Expected: False

# %%
#Step 4: Implementing a function to generate alerts based on sensor readings and system mode.

def generate_reading(sensor):
    sensor_type = sensor["type"]

    if sensor_type == "temperature":
        return random.randint(30, 100)

    elif sensor_type == "motion":
        return random.choice([True, False])

    elif sensor_type == "door":
        return random.choice(["OPEN", "CLOSED"])

    elif sensor_type == "smoke":
        return random.choice(["CLEAR", "DETECTED"])

# %%


# %%
import random
from datetime import datetime

# %%
for sensor in sensors:
    reading = generate_reading(sensor)
    print(sensor["type"], ":", reading)

# %%
# Now creating process_reading(). This function will take one sensor reading and decide whether to create alerts.

def process_reading(sensor, reading_value, system_mode):
    alerts = []
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Security alerts
    if should_trigger_security_alert(sensor, reading_value, system_mode):
        alert = create_alert(
            "HIGH",
            f"Security issue detected by {sensor['id']}",
            sensor["id"],
            timestamp
        )
        alerts.append(alert)

    # Safety alerts
    if sensor["type"] == "temperature":
        if reading_value < 35:
            alert = create_alert(
                "CRITICAL",
                "Temperature is dangerously low",
                sensor["id"],
                timestamp
            )
            alerts.append(alert)

        elif reading_value > 95:
            alert = create_alert(
                "CRITICAL",
                "Temperature is dangerously high",
                sensor["id"],
                timestamp
            )
            alerts.append(alert)

    elif sensor["type"] == "smoke" and reading_value == "DETECTED":
        alert = create_alert(
            "CRITICAL",
            "Smoke detected",
            sensor["id"],
            timestamp
        )
        alerts.append(alert)

    return alerts

# %%
#Testing the process_reading() function with different scenarios
motion_sensor = create_sensor(
    "MOTION_TEST",
    "Test Room",
    "motion"
)

alerts = process_reading(
    motion_sensor,
    True,
    "AWAY"
)

print(alerts)

# %%
temperature_sensor = create_sensor(
    "TEMP_TEST",
    "Test Room",
    "temperature"
)
print(process_reading(temperature_sensor, 34, "AWAY"))

# %%
smoke_sensor = create_sensor(
    "SMOKE_TEST",
    "Test Room",
    "smoke"
)
print(process_reading(smoke_sensor, "DETECTED", "AWAY"))

# %%
def trigger_alert(alert):
    """
    Displays an alert to the user.
    
    Parameters:
    - alert: Alert dictionary
    """
    severity_symbol = {
        "LOW": "ℹ️",
        "MEDIUM": "⚠️",
        "HIGH": "🚨",
        "CRITICAL": "🔥"
    }
    
    symbol = severity_symbol.get(alert["severity"], "⚠️")
    print(f"[ALERT!] {symbol} {alert['severity']}: {alert['message']}")
 
def log_event(message, timestamp=None):
    """
    Logs an event to the console.
    
    Parameters:
    - message: The message to log
    - timestamp: Optional timestamp (uses current time if not provided)
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[LOG] [{timestamp}] {message}")

# %%
#Testing alert triggering and logging
test_alert = create_alert(
    "HIGH",
    "Motion detected",
    "MOTION_1",
    "12:30:00"
)

trigger_alert(test_alert)
log_event("Test event recorded")

# %%
# Testing reading generation
test_sensor = sensors[0]  # Motion sensor
reading = generate_reading(test_sensor)
print(f"Generated reading for {test_sensor['location']}: {reading}")
 
# Testing processing
alerts = process_reading(test_sensor, True, "AWAY")
if alerts:
    trigger_alert(alerts[0])

# %%
import random

def generate_reading(sensor):
    sensor_type = sensor["type"]

    if sensor_type == "temperature":
        return random.randint(30, 100)

    elif sensor_type == "motion":
        return random.choice([True, False])

    elif sensor_type == "door":
        return random.choice(["OPEN", "CLOSED"])

    elif sensor_type == "smoke":
        return random.choice(["CLEAR", "DETECTED"])

    return None

# %%
#step 5: Converting the sensor dictionary into a Sensor class with methods.
class Sensor:
    # Initializes a new sensor.
    def __init__(self, sensor_id, location, sensor_type, threshold=None):
        self.id = sensor_id
        self.location = location
        self.type = sensor_type
        self.threshold = threshold
        self.current_value = None

#Generating and storing a new reading for this sensor.
    def read(self):
        sensor_data = {
            "type": self.type
        }
        self.current_value = generate_reading(sensor_data)
        return self.current_value

#Determines if the current reading is abnormal based on sensor type and thresholds.
    def is_abnormal(self):
        if self.current_value is None:
            return False

#Resets the sensor's current reading to None.
        sensor_data = {
            "type": self.type,
            "threshold": self.threshold
        }

        return is_abnormal_reading(sensor_data, self.current_value)

    #Resets the sensor's current reading to None.
    def reset(self):
        self.current_value = None

    # Returns a string representation of the sensor.
    def __str__(self):
        status = (
            "No reading"
            if self.current_value is None
            else str(self.current_value)
        )
        return f"{self.id} ({self.location}): {status}"

# %%
def is_abnormal_reading(sensor, reading_value):
    sensor_type = sensor["type"]

    if sensor_type == "temperature":
        return reading_value < 35 or reading_value > 95

    elif sensor_type == "motion":
        return reading_value is True

    elif sensor_type == "door":
        return reading_value == "OPEN"

    elif sensor_type == "smoke":
        return reading_value == "DETECTED"

    return False

# %%
test_sensor = Sensor(
    "MOTION_001",
    "Living Room",
    "motion"
)

print(test_sensor)
print(test_sensor.read())
print(test_sensor)
print(test_sensor.is_abnormal())

# %%
#step 6: Combining all components into a complete simulator that runs continuously.

def run_simulation(duration_minutes=5, system_mode="AWAY"):
    """
    Runs the HomeGuard security system simulation.
    
    Parameters:
    - duration_minutes: How long to run the simulation (default: 5 minutes)
    - system_mode: System mode (HOME, AWAY, SLEEP)
    """
    print("=" * 50)
    print("=== HomeGuard Security System ===")
    print("=" * 50)
    print(f"Mode: {system_mode}\n")
    
    # Use sensor objects instead of dictionaries
    sensors = [
        Sensor("MOTION_001", "Living Room", "motion"),
        Sensor("TEMP_001", "Kitchen", "temperature", threshold=35),
        Sensor("DOOR_001", "Front Door", "door"),
        Sensor("SMOKE_001", "Bedroom", "smoke")
    ]
    
    # Simulate time passing (each iteration = 1 minute)
    for minute in range(duration_minutes):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"\nTime: {current_time}")
        
        # Read all sensors
        for sensor in sensors:
            reading = sensor.read()
            
            # Display the reading
            if sensor.type == "temperature":
                status = "Normal" if 65 <= reading <= 75 else "Abnormal"
                print(f"[READING] {sensor.location} Temperature: {reading}°F ({status})")
            elif sensor.type == "motion":
                status = "DETECTED" if reading else "No activity"
                print(f"[READING] {sensor.location} Motion: {status}")
            elif sensor.type == "door":
                print(f"[READING] {sensor.location}: {reading}")
            elif sensor.type == "smoke":
                print(f"[READING] {sensor.location} Smoke: {reading}")
            
            # Process the reading and trigger alerts if needed
            # Convert sensor object to dict format for process_reading function
            sensor_dict = {
                "id": sensor.id,
                "location": sensor.location,
                "type": sensor.type,
                "threshold": sensor.threshold
            }
            alerts = process_reading(sensor_dict, reading, system_mode)
            
            # Trigger all alerts
            for alert in alerts:
                trigger_alert(alert)
                if alert["severity"] in ["HIGH", "CRITICAL"]:
                    log_event("Sending notification to homeowner...")
        
        # Small delay to make output readable (optional)
        import time
        time.sleep(0.5)  # 0.5 second delay between iterations
    
    print("\n" + "=" * 50)
    print("Simulation complete!")
    print("=" * 50)
 
# Main execution
if __name__ == "__main__":
    # Run the simulation
    run_simulation(duration_minutes=3, system_mode="AWAY")

# %%
#now testing Home mode
run_simulation(duration_minutes=1, system_mode="HOME")

# %%
run_simulation(duration_minutes=3, system_mode="AWAY")

# %%
run_simulation(duration_minutes=1, system_mode="SLEEP")

# %%

if __name__ == "__main__":
    run_simulation(duration_minutes=3, system_mode="AWAY")

# %%
