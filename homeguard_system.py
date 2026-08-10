"""
HomeGuard Security System Simulator
Author: Lab M1.01 — Programming Foundation Exercises
Description: Prototype smart-home monitor that reads sensors, checks thresholds
             by system mode, and triggers security, safety, and comfort alerts.
"""

import random
from datetime import datetime, timedelta


# ---------------------------------------------------------------------------
# Step 2: Data structures (dictionaries for sensors, alerts, and system state)
# ---------------------------------------------------------------------------

def create_sensor_dict(sensor_id, location, sensor_type, threshold=None):
    """Return a dictionary representing a sensor."""
    return {
        "id": sensor_id,
        "location": location,
        "type": sensor_type,
        "current_value": None,
        "threshold": threshold,
        "status": "OK",
    }


def create_alert_dict(severity, category, message, timestamp):
    """Return a dictionary representing an alert event."""
    return {
        "severity": severity,
        "category": category,
        "message": message,
        "timestamp": timestamp,
    }


def create_system_state(mode="AWAY"):
    """Return the shared system state dictionary."""
    return {
        "mode": mode.upper(),
        "alerts": [],
        "event_log": [],
        "active_sensors": [],
        "door_open_minutes": {},
    }


def initialize_sensors():
    """Build the initial list of sensor dictionaries for the Peterson home."""
    return [
        create_sensor_dict("MOT-01", "Living Room", "motion"),
        create_sensor_dict("DOOR-01", "Front Door", "door"),
        create_sensor_dict("TEMP-01", "Kitchen", "temperature", threshold={"min": 35, "max": 95, "comfort_min": 65, "comfort_max": 75}),
        create_sensor_dict("SMOKE-01", "Bedroom", "smoke"),
        create_sensor_dict("MOT-02", "Hallway", "motion"),
        create_sensor_dict("TEMP-02", "Basement", "temperature", threshold={"min": 35, "max": 95, "comfort_min": 65, "comfort_max": 75}),
    ]


# ---------------------------------------------------------------------------
# Step 5: Sensor class (properties + methods)
# ---------------------------------------------------------------------------

class Sensor:
    """Blueprint for a home sensor with read / abnormality / reset behavior."""

    def __init__(self, sensor_id, location, sensor_type, threshold=None):
        self.id = sensor_id
        self.location = location
        self.type = sensor_type
        self.threshold = threshold or {}
        self.current_value = None
        self.status = "OK"

    def read(self, fixed_value=None):
        """Generate (or accept) a sensor reading and store it."""
        if fixed_value is not None:
            self.current_value = fixed_value
        else:
            self.current_value = generate_sensor_reading(self.type)
        return self.current_value

    def isAbnormal(self, system_mode):
        """
        Return True when the current reading should raise concern for the mode.
        Delegates threshold checks to the shared if/else helper.
        """
        result = check_sensor_abnormal(self.type, self.current_value, system_mode, self.threshold)
        return result["is_abnormal"]

    def reset(self):
        """Clear the latest reading and restore a healthy status."""
        self.current_value = None
        self.status = "OK"

    def to_dict(self):
        """Export sensor state as a dictionary (for logging / display)."""
        return {
            "id": self.id,
            "location": self.location,
            "type": self.type,
            "current_value": self.current_value,
            "threshold": self.threshold,
            "status": self.status,
        }


def sensors_from_dicts(sensor_dicts):
    """Convert sensor dictionaries into Sensor class instances."""
    return [
        Sensor(
            sensor_id=s["id"],
            location=s["location"],
            sensor_type=s["type"],
            threshold=s.get("threshold"),
        )
        for s in sensor_dicts
    ]


# ---------------------------------------------------------------------------
# Step 3: If/else logic for thresholds and system modes
# ---------------------------------------------------------------------------

def check_sensor_abnormal(sensor_type, value, system_mode, threshold=None):
    """
    Decide whether a reading is abnormal and what kind of alert it needs.
    Uses if/else to compare against safety / comfort / security rules.
    """
    threshold = threshold or {}
    mode = system_mode.upper()
    result = {
        "is_abnormal": False,
        "severity": None,
        "category": None,
        "message": None,
    }

    if sensor_type == "temperature":
        min_safe = threshold.get("min", 35)
        max_safe = threshold.get("max", 95)
        comfort_min = threshold.get("comfort_min", 65)
        comfort_max = threshold.get("comfort_max", 75)

        if value is None:
            return result
        elif value < min_safe:
            result.update({
                "is_abnormal": True,
                "severity": "CRITICAL",
                "category": "SAFETY",
                "message": f"Temperature {value}°F below {min_safe}°F — frozen pipe risk!",
            })
        elif value > max_safe:
            result.update({
                "is_abnormal": True,
                "severity": "CRITICAL",
                "category": "SAFETY",
                "message": f"Temperature {value}°F above {max_safe}°F — equipment failure risk!",
            })
        elif mode == "HOME" and (value < comfort_min or value > comfort_max):
            result.update({
                "is_abnormal": True,
                "severity": "LOW",
                "category": "COMFORT",
                "message": f"Temperature {value}°F outside comfort range ({comfort_min}-{comfort_max}°F)",
            })

    elif sensor_type == "smoke":
        if value == "SMOKE":
            result.update({
                "is_abnormal": True,
                "severity": "CRITICAL",
                "category": "SAFETY",
                "message": "Smoke detected — fire risk!",
            })

    elif sensor_type == "motion":
        if value == "MOTION" and mode == "AWAY":
            result.update({
                "is_abnormal": True,
                "severity": "HIGH",
                "category": "SECURITY",
                "message": "Motion detected while in AWAY mode!",
            })

    elif sensor_type == "door":
        if value == "OPEN" and mode == "AWAY":
            result.update({
                "is_abnormal": True,
                "severity": "HIGH",
                "category": "SECURITY",
                "message": "Door opened while in AWAY mode!",
            })

    return result


# ---------------------------------------------------------------------------
# Step 4: Core functions — generate, process, trigger, log
# ---------------------------------------------------------------------------

def generate_sensor_reading(sensor_type):
    """Produce a realistic random reading for the given sensor type."""
    if sensor_type == "temperature":
        # Bias toward normal comfort range, with occasional extremes
        roll = random.random()
        if roll < 0.08:
            return random.randint(20, 34)   # freeze risk
        elif roll < 0.16:
            return random.randint(96, 110)  # overheat risk
        elif roll < 0.35:
            return random.randint(50, 64)   # cool comfort issue
        elif roll < 0.50:
            return random.randint(76, 90)   # warm comfort issue
        else:
            return random.randint(65, 75)   # comfort OK
    elif sensor_type == "motion":
        return "MOTION" if random.random() < 0.25 else "CLEAR"
    elif sensor_type == "door":
        return "OPEN" if random.random() < 0.20 else "CLOSED"
    elif sensor_type == "smoke":
        return "SMOKE" if random.random() < 0.05 else "CLEAR"
    else:
        return None


def format_reading(sensor):
    """Return a human-readable reading line for console output."""
    location = sensor.location
    value = sensor.current_value

    if sensor.type == "motion":
        label = "No activity" if value == "CLEAR" else "Motion detected"
        return f"[READING] {location} Motion: {label}"
    elif sensor.type == "door":
        label = "CLOSED" if value == "CLOSED" else "OPENED"
        return f"[READING] {location}: {label}"
    elif sensor.type == "temperature":
        status = "Normal"
        if value is not None:
            if value < 35 or value > 95:
                status = "Danger"
            elif value < 65 or value > 75:
                status = "Outside comfort"
        return f"[READING] {location} Temperature: {value}°F ({status})"
    elif sensor.type == "smoke":
        label = "CLEAR" if value == "CLEAR" else "SMOKE DETECTED"
        return f"[READING] {location} Smoke: {label}"
    return f"[READING] {location}: {value}"


def log_event(system_state, timestamp, message):
    """Append an event to the system log and print it."""
    entry = f"[{timestamp.strftime('%H:%M:%S')}] {message}"
    system_state["event_log"].append(entry)
    print(f"[LOG] {entry}")


def trigger_alert(system_state, sensor, check_result, timestamp):
    """Create, store, and display an alert for an abnormal reading."""
    location = sensor.location
    severity = check_result["severity"]
    category = check_result["category"]
    detail = check_result["message"]
    message = f"{category}: {location} — {detail}"

    alert = create_alert_dict(severity, category, message, timestamp)
    system_state["alerts"].append(alert)

    print(f"[ALERT!] 🚨 {severity}: {message}")
    log_event(system_state, timestamp, "Sending notification to homeowner...")


def process_sensor(sensor, system_state, timestamp, fixed_value=None):
    """
    Read one sensor, print the reading, and trigger an alert if needed.
    Returns the abnormality check result.
    """
    sensor.read(fixed_value=fixed_value)
    print(format_reading(sensor))

    check = check_sensor_abnormal(
        sensor.type,
        sensor.current_value,
        system_state["mode"],
        sensor.threshold,
    )

    # Track how long a door has been open (comfort: >5 minutes)
    if sensor.type == "door":
        door_key = sensor.id
        if sensor.current_value == "OPEN":
            minutes = system_state["door_open_minutes"].get(door_key, 0) + 1
            system_state["door_open_minutes"][door_key] = minutes
            if minutes > 5 and system_state["mode"] == "HOME":
                comfort = {
                    "is_abnormal": True,
                    "severity": "LOW",
                    "category": "COMFORT",
                    "message": f"Door left open for {minutes} minutes!",
                }
                trigger_alert(system_state, sensor, comfort, timestamp)
                sensor.status = "ALERT"
        else:
            system_state["door_open_minutes"][door_key] = 0

    if check["is_abnormal"]:
        sensor.status = "ALERT"
        trigger_alert(system_state, sensor, check, timestamp)
        system_state["active_sensors"].append(sensor.id)
    else:
        sensor.status = "OK"

    return check


def check_multi_sensor_breakin(system_state, timestamp, triggered_ids):
    """If several security sensors fire in one cycle, escalate to break-in."""
    if len(triggered_ids) >= 2:
        fake_sensor = Sensor("SYS", "Multiple Zones", "motion")
        result = {
            "is_abnormal": True,
            "severity": "CRITICAL",
            "category": "SECURITY",
            "message": f"Possible break-in — {len(triggered_ids)} sensors triggered simultaneously!",
        }
        trigger_alert(system_state, fake_sensor, result, timestamp)


# ---------------------------------------------------------------------------
# Step 6: Integration — main simulation loop
# ---------------------------------------------------------------------------

def run_simulation(mode="AWAY", iterations=3, fixed_readings=None, start_time=None):
    """
    Run the HomeGuard simulator.

    fixed_readings: optional list of dicts {sensor_id: value} per iteration
                    so reviewers can reproduce deterministic output.
    """
    system_state = create_system_state(mode=mode)
    sensor_dicts = initialize_sensors()
    sensors = sensors_from_dicts(sensor_dicts)

    if start_time is None:
        current_time = datetime.now().replace(second=0, microsecond=0)
    else:
        current_time = start_time

    print("=== HomeGuard Security System ===")
    print(f"Time: {current_time.strftime('%H:%M:%S')}")
    print(f"Mode: {system_state['mode']}")
    print()

    for i in range(iterations):
        if i > 0:
            current_time = current_time + timedelta(minutes=1)
            print(f"Time: {current_time.strftime('%H:%M:%S')}")

        system_state["active_sensors"] = []
        security_hits = []
        cycle_fixed = None
        if fixed_readings and i < len(fixed_readings):
            cycle_fixed = fixed_readings[i]

        for sensor in sensors:
            fixed_val = None
            if cycle_fixed is not None:
                fixed_val = cycle_fixed.get(sensor.id)
            check = process_sensor(sensor, system_state, current_time, fixed_value=fixed_val)
            if check["is_abnormal"] and check["category"] == "SECURITY":
                security_hits.append(sensor.id)

        check_multi_sensor_breakin(system_state, current_time, security_hits)
        print()

    print("--- Simulation complete ---")
    print(f"Total alerts: {len(system_state['alerts'])}")
    print(f"Events logged: {len(system_state['event_log'])}")
    return system_state


def run_demo_cases():
    """
    Fixed (deterministic) cases covering security, safety, and comfort.
    Used for lab_proof.md verification.
    """
    start = datetime(2026, 8, 10, 14, 30, 0)

    print("########## CASE 1: SECURITY (AWAY mode) ##########")
    print()
    # Iteration 0: all quiet
    # Iteration 1: front door opens + living room motion → break-in
    # Iteration 2: still elevated
    away_readings = [
        {
            "MOT-01": "CLEAR",
            "DOOR-01": "CLOSED",
            "TEMP-01": 68,
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 70,
        },
        {
            "MOT-01": "MOTION",
            "DOOR-01": "OPEN",
            "TEMP-01": 68,
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 70,
        },
        {
            "MOT-01": "CLEAR",
            "DOOR-01": "OPEN",
            "TEMP-01": 68,
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 70,
        },
    ]
    run_simulation(mode="AWAY", iterations=3, fixed_readings=away_readings, start_time=start)

    print()
    print("########## CASE 2: SAFETY (temperature + smoke) ##########")
    print()
    safety_start = datetime(2026, 8, 10, 15, 0, 0)
    safety_readings = [
        {
            "MOT-01": "CLEAR",
            "DOOR-01": "CLOSED",
            "TEMP-01": 28,       # frozen pipe risk
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 102,      # equipment failure
        },
        {
            "MOT-01": "CLEAR",
            "DOOR-01": "CLOSED",
            "TEMP-01": 70,
            "SMOKE-01": "SMOKE",  # fire risk
            "MOT-02": "CLEAR",
            "TEMP-02": 72,
        },
        {
            "MOT-01": "CLEAR",
            "DOOR-01": "CLOSED",
            "TEMP-01": 70,
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 72,
        },
    ]
    run_simulation(mode="AWAY", iterations=3, fixed_readings=safety_readings, start_time=safety_start)

    print()
    print("########## CASE 3: COMFORT (HOME mode) ##########")
    print()
    comfort_start = datetime(2026, 8, 10, 16, 0, 0)
    comfort_readings = [
        {
            "MOT-01": "MOTION",   # motion OK while HOME — no security alert
            "DOOR-01": "CLOSED",
            "TEMP-01": 60,        # outside comfort range
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 72,
        },
        {
            "MOT-01": "CLEAR",
            "DOOR-01": "OPEN",
            "TEMP-01": 80,        # outside comfort range
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 72,
        },
        {
            "MOT-01": "CLEAR",
            "DOOR-01": "CLOSED",
            "TEMP-01": 70,
            "SMOKE-01": "CLEAR",
            "MOT-02": "CLEAR",
            "TEMP-02": 72,
        },
    ]
    run_simulation(mode="HOME", iterations=3, fixed_readings=comfort_readings, start_time=comfort_start)

    print()
    print("########## EDGE CASE: None / missing reading ##########")
    print()
    # Explicitly handle None so comparisons never crash (TypeError edge case)
    edge = check_sensor_abnormal("temperature", None, "HOME")
    print(f"check_sensor_abnormal(temperature, None, HOME) => {edge}")
    print("Edge case handled: missing readings are treated as not abnormal.")


if __name__ == "__main__":
    # Default entry point: deterministic demo for the reviewer.
    # For a live random demo, call: run_simulation(mode="AWAY", iterations=3)
    run_demo_cases()
