"""
HomeGuard Security System Simulator
Author: Rita Sousa
Description: A smart home monitoring system that processes sensor readings
and triggers alerts for security, safety, and comfort issues.
"""

# Import modules needed for sensor simulation and timestamps
import random
from datetime import datetime

from sympy import python

# Define available home modes and alert severity levels
HOME_MODES = ["HOME", "AWAY", "SLEEP"]
ALERT_SEVERITIES = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

# Current system state
current_mode = "AWAY"

# Create and return a dictionary containing sensor information.
def create_sensor(sensor_id, location, sensor_type, threshold=None):
    """
    Creates a sensor data structure.

    Parameters:
        sensor_id: Unique identifier for the sensor
        location: Where the sensor is located
        sensor_type: Type of sensor
        threshold: Optional threshold value for the sensor

    Returns:
        A dictionary representing the sensor.
    """
    sensor = {
        "id": sensor_id,
        "location": location,
        "type": sensor_type,
        "threshold": threshold
    }
    return sensor

# Create and return a dictionary containing alert information.
def create_alert(severity, message, sensor_id, timestamp):
    """
    Creates an alert data structure.

    Parameters:
        severity: Alert severity level
        message: Description of the alert
        sensor_id: ID of the sensor that triggered the alert
        timestamp: When the alert was triggered

    Returns:
        A dictionary representing the alert.
    """
    alert = {
        "severity": severity,
        "message": message,
        "sensor_id": sensor_id,
        "timestamp": timestamp
    }
    return alert

# Initialize sensors for the Peterson home
sensors = [
    create_sensor("ID01", "Living Room", "motion"),
    create_sensor("ID02", "Kitchen", "temperature", threshold=35),
    create_sensor("ID03", "Front Door", "door"),
    create_sensor("ID04", "Bedroom", "smoke")
]

# Test the sensor and alert functions
print(f"Initialized {len(sensors)} sensors")
for sensor in sensors:
    print(f"  - {sensor['id']}: {sensor['location']} ({sensor['type']})")


def is_abnormal_reading(sensor, reading_value):
    """
    Checks if a sensor reading is abnormal based on sensor type and thresholds.
    
    Parameters:
    - sensor: Sensor dictionary
    - reading_value: The current reading from the sensor
    
    Returns:
    - True if the reading is abnormal, False otherwise
    """
    sensor_type = sensor["type"]
    
    if sensor_type == "temperature":
        if reading_value < 35 or reading_value > 95:
            return True
        else:
            return False

    elif sensor_type == "motion":
        return reading_value == True

    elif sensor_type == "door":
        return reading_value == "OPEN"

    elif sensor_type == "smoke":
        return reading_value == "DETECTED"

    else:
        return False
    
 
def should_trigger_security_alert(sensor, reading_value, system_mode):
    """
    Determines if a security alert should be triggered.

    Parameters:
    - sensor: Sensor dictionary
    - reading_value: The current reading from the sensor
    - system_mode: Current system mode (HOME, AWAY, SLEEP)

    Returns:
    - True if a security alert should be triggered, False otherwise
    """
    if not is_abnormal_reading(sensor, reading_value):
        return False

    if system_mode == "AWAY":
        return True

    elif system_mode == "HOME":
        return sensor["type"] == "smoke"

    elif system_mode == "SLEEP":
        return sensor["type"] in ["door", "motion", "smoke"]

    else:
        return False
    
# Test temperature check
test_sensor = create_sensor("TEMP_TEST", "Test Room", "temperature", threshold=35)
print(f"34°F is abnormal: {is_abnormal_reading(test_sensor, 34)}")  # Should be True
print(f"68°F is abnormal: {is_abnormal_reading(test_sensor, 68)}")  # Should be False
 
# Test security alert
motion_sensor = create_sensor("MOTION_TEST", "Test Room", "motion")
print(f"Motion in AWAY mode triggers alert: {should_trigger_security_alert(motion_sensor, True, 'AWAY')}")  # Should be True
print(f"Motion in HOME mode triggers alert: {should_trigger_security_alert(motion_sensor, True, 'HOME')}")  # Should be False
    
   
def generate_reading(sensor):
    """
    Generates a realistic reading for a sensor.

    Parameters:
    - sensor: Sensor dictionary

    Returns:
    - A realistic reading value based on sensor type
    """
    sensor_type = sensor["type"]

    if sensor_type == "temperature":
        return random.randint(30, 100)

    elif sensor_type == "motion":
        return random.choice([True, False])

    elif sensor_type == "door":
        return random.choice(["OPEN", "CLOSED"])

    elif sensor_type == "smoke":
        return random.choice(["CLEAR", "DETECTED"])

    else:
        return None


def process_reading(sensor, reading_value, system_mode):
    """
    Processes a sensor reading and determines if alerts are needed.
    
    Parameters:
    - sensor: Sensor dictionary
    - reading_value: The reading from the sensor
    - system_mode: Current system mode
    
    Returns:
    - A list of alerts (empty if no alerts needed)
    """

    alerts = []
    timestamp = datetime.now().strftime("%H:%M:%S")

    
    sensor_type = sensor["type"]

    # Security alerts
    if should_trigger_security_alert(sensor, reading_value, system_mode):
        alert = create_alert(
            "HIGH",
            f"Security issue detected: {sensor_type} sensor at {sensor['location']}",
            sensor["id"],
            timestamp
        )
        alerts.append(alert)

    # Safety alerts
    if sensor_type == "smoke" and reading_value == "DETECTED":
        alert = create_alert(
            "CRITICAL",
            f"Smoke detected at {sensor['location']}!",
            sensor["id"],
            timestamp
        )
        alerts.append(alert)

    elif sensor_type == "temperature" and (
        reading_value < 35 or reading_value > 95
    ):
        alert = create_alert(
            "HIGH",
            f"Extreme temperature detected: {reading_value}°F at {sensor['location']}",
            sensor["id"],
            timestamp
        )
        alerts.append(alert)

    # Comfort notifications (only in HOME mode)
    if system_mode == "HOME" and sensor_type == "temperature":
        if reading_value < 65 or reading_value > 75:
            alert = create_alert(
                "LOW",
                f"Temperature may be uncomfortable: {reading_value}°F at {sensor['location']}",
                sensor["id"],
                timestamp
            )
            alerts.append(alert)

    return alerts
    
    
    
    # Comfort notifications (only in HOME mode)
    if system_mode == "HOME" and sensor_type == "temperature":
        if reading_value < 65 or reading_value > 75:
            alert = create_alert(
                "LOW",
                f"Temperature may be uncomfortable: {reading_value}°F at {sensor['location']}",
                sensor["id"],
                timestamp
            )
            alerts.append(alert)

    return alerts
 
# Feel free to change the function signatures or add helper functions as needed, these are just some suggestions to make the code more friendly! 
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

    # Test reading generation
test_sensor = sensors[0]  # Motion sensor
reading = generate_reading(test_sensor)
print(f"Generated reading for {test_sensor['location']}: {reading}")
 
# Test processing
alerts = process_reading(test_sensor, True, "AWAY")
if alerts:
    trigger_alert(alerts[0])


class Sensor:

    """
    Represents a sensor in the HomeGuard system.
    """
    
    def __init__(self, sensor_id, location, sensor_type, threshold=None):
        """
        Initializes a new sensor.
        
        Parameters:
        - sensor_id: Unique identifier for the sensor
        - location: Where the sensor is located
        - sensor_type: Type of sensor ("motion", "temperature", "door", "smoke")
        - threshold: Optional threshold value for the sensor
        """
        self.id = sensor_id
        self.location = location
        self.type = sensor_type
        self.threshold = threshold
        self.current_value = None
    
    def read(self):
        """
        Generates and stores a new reading for this sensor.
        
        Returns:
        - The reading value
        """
        self.current_value = generate_reading({
            "id": self.id,
            "location": self.location,
            "type": self.type,
            "threshold": self.threshold
        })
        return self.current_value
        
    def isAbnormal(self):
        """
        Checks if the current reading is abnormal.
        
        Returns:
        - True if the reading is abnormal, False otherwise
        """
        if self.current_value is None:
            return False

        sensor = {
            "id": self.id,
            "location": self.location,
            "type": self.type,
            "threshold": self.threshold
        }

        return is_abnormal_reading(sensor, self.current_value)
  
    
    def reset(self):
        """
        Resets the sensor's current reading to None.
        """
    
        self.current_value = None
    
    def __str__(self):
        """
        Returns a string representation of the sensor.
        """
        status = "No reading" if self.current_value is None else str(self.current_value)
        return f"{self.id} ({self.location}): {status}"
 
# Create sensor objects using the class
sensor_objects = [
    Sensor("MOTION_001", "Living Room", "motion"),
    Sensor("TEMP_001", "Kitchen", "temperature", threshold=35),
    Sensor("DOOR_001", "Front Door", "door"),
    Sensor("SMOKE_001", "Bedroom", "smoke")
]

# Create and test a sensor
test_sensor = Sensor("TEST_001", "Test Room", "temperature", threshold=35)
test_sensor.read()
print(f"Sensor reading: {test_sensor.current_value}")
print(f"Is abnormal: {test_sensor.isAbnormal()}")
print(f"Sensor info: {test_sensor}")



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

# Security Test: Run with system_mode="AWAY" and verify security alerts trigger
run_simulation(duration_minutes=3, system_mode="AWAY")
run_simulation(duration_minutes=3, system_mode="HOME")
run_simulation(duration_minutes=3, system_mode="SLEEP")
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