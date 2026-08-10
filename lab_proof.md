# Lab proof — HomeGuard Security System

## Program path

`homeguard_system.py`

## Run command

```bash
python3 homeguard_system.py
```

## Output from fixed cases

The entry point runs three deterministic cases (no randomness), then one edge-case check.

### Case 1 — Security (AWAY mode)

```
########## CASE 1: SECURITY (AWAY mode) ##########

=== HomeGuard Security System ===
Time: 14:30:00
Mode: AWAY

[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR
[READING] Hallway Motion: No activity
[READING] Basement Temperature: 70°F (Normal)

Time: 14:31:00
[READING] Living Room Motion: Motion detected
[ALERT!] 🚨 HIGH: SECURITY: Living Room — Motion detected while in AWAY mode!
[LOG] [14:31:00] Sending notification to homeowner...
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door — Door opened while in AWAY mode!
[LOG] [14:31:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR
[READING] Hallway Motion: No activity
[READING] Basement Temperature: 70°F (Normal)
[ALERT!] 🚨 CRITICAL: SECURITY: Multiple Zones — Possible break-in — 2 sensors triggered simultaneously!
[LOG] [14:31:00] Sending notification to homeowner...

Time: 14:32:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door — Door opened while in AWAY mode!
[LOG] [14:32:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR
[READING] Hallway Motion: No activity
[READING] Basement Temperature: 70°F (Normal)

--- Simulation complete ---
Total alerts: 4
Events logged: 4
```

### Case 2 — Safety (temperature + smoke)

```
########## CASE 2: SAFETY (temperature + smoke) ##########

=== HomeGuard Security System ===
Time: 15:00:00
Mode: AWAY

[READING] Kitchen Temperature: 28°F (Danger)
[ALERT!] 🚨 CRITICAL: SAFETY: Kitchen — Temperature 28°F below 35°F — frozen pipe risk!
[READING] Basement Temperature: 102°F (Danger)
[ALERT!] 🚨 CRITICAL: SAFETY: Basement — Temperature 102°F above 95°F — equipment failure risk!

Time: 15:01:00
[READING] Bedroom Smoke: SMOKE DETECTED
[ALERT!] 🚨 CRITICAL: SAFETY: Bedroom — Smoke detected — fire risk!

--- Simulation complete ---
Total alerts: 3
```

### Case 3 — Comfort (HOME mode)

```
########## CASE 3: COMFORT (HOME mode) ##########

=== HomeGuard Security System ===
Time: 16:00:00
Mode: HOME

[READING] Living Room Motion: Motion detected
[READING] Kitchen Temperature: 60°F (Outside comfort)
[ALERT!] 🚨 LOW: COMFORT: Kitchen — Temperature 60°F outside comfort range (65-75°F)

Time: 16:01:00
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 80°F (Outside comfort)
[ALERT!] 🚨 LOW: COMFORT: Kitchen — Temperature 80°F outside comfort range (65-75°F)

--- Simulation complete ---
Total alerts: 2
```

In HOME mode, motion does **not** raise a security alert (only AWAY does), which matches the requirements.

## How the code works (brief)

Dictionaries hold sensor/alert/system state. A `Sensor` class wraps each device with `read()`, `isAbnormal()`, and `reset()`. Functions generate or accept fixed readings, run if/else threshold checks by mode, trigger alerts, and log events. `run_simulation()` ties everything into a timed loop with formatted console output.

## Edge case handled

**Missing / `None` temperature reading.** Comparing `None < 35` would raise `TypeError`. `check_sensor_abnormal` returns “not abnormal” when the value is `None`, so a failed sensor read does not crash the simulator or invent a false critical alert.

```
check_sensor_abnormal(temperature, None, HOME) =>
{'is_abnormal': False, 'severity': None, 'category': None, 'message': None}
```
