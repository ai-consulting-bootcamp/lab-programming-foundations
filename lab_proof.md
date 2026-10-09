HomeGuard – Lab Proof

1. Program Path

homeguard_system.py

2. How to Run

Run the program using:

python3 homeguard_system.py

3. Program Description

HomeGuard is a simple smart-home security simulator written in Python.

It monitors four sensors: temperature, smoke, motion, and door.

The program uses a Sensor class, functions, dictionaries, lists, loops, and conditional statements. It supports HOME, AWAY, and SLEEP modes and records alerts with timestamps.

4. Deterministic Test Results

The program was tested with three scans using fixed sensor readings.

Actual Terminal Output

--- SCAN 1 ---
Mode: HOME
Kitchen : 68
Hallway : False
Living Room : False
Front Door : False

--- SCAN 2 ---
Mode: AWAY
Kitchen : 30
Hallway : True
Living Room : True
Front Door : True
15:51:25 - ALERT: Frozen pipe risk!
15:51:25 - ALERT: Smoke detected!
15:51:25 - ALERT: Motion detected while away!
15:51:25 - ALERT: Door opened while away!
15:51:25 - ALERT: Motion and door triggered together!

--- SCAN 3 ---
Mode: SLEEP
Kitchen : 100
Hallway : False
Living Room : False
Front Door : True
15:51:25 - ALERT: Equipment failure risk!
15:51:25 - ALERT: Door open longer than 5 minutes!

--- RANDOM READINGS ---
{'temperature': 47, 'smoke': True, 'motion': True, 'door': False}

--- RESET TEST ---
After reset: None
Abnormal: False

--- SUMMARY ---
Total alerts: 7
Total logged events: 7

5. Edge Case Test

Test: Resetting the temperature sensor.

Expected result:

The sensor value becomes None.

isAbnormal() returns False.

The program continues without errors.

Actual result:

After reset: None
Abnormal: False

Result: Passed.

6. Random Readings

The program also generates random sensor readings using Python's random module.

The random readings are separate from the fixed test cases, making the main tests reproducible.

7. What I Learned

I learned how to use Python functions, classes, dictionaries, lists, loops, and if/else statements.

I also learned how to create sensor objects, check their readings, generate alerts, and reset sensors.
