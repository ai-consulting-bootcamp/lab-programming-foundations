# Lab Proof: HomeGuard Smart Home Alarm
Ayhan Demir
My program simulates a home alarm: each of the 4 sensors is a Sensor object whose read() method uses random to invent a new reading. The method  combines reading with the house mode (HOME or AWAY) and follows the rule table with if/else to return an alert dictionary or None. A main loop repeats this for 3 simulated minutes, printing every reading, any alert, and a log line that is also saved in a list.

## How to run it
1. Open `homeguard_system.ipynb` in VS Code.
2. Select the `bootcamp-env` kernel.
3. Click Run All.

## My output
=== HomeGuard Security System ===
Time: 17:39:00
Mode: AWAY

[READING] Living Room Motion: Motion detected
[ALERT!] 🚨 HIGH: SECURITY: Motion detected in Living Room while in AWAY mode!
[LOG] [17:39:00] Sending notification to homeowner...
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [17:39:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 43°F (Out of range)
[READING] Bedroom Smoke: CLEAR

Time: 17:40:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [17:40:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 84°F (Out of range)
[READING] Bedroom Smoke: DETECTED
[ALERT!] 🔥 CRITICAL: SAFETY: Smoke detected in Bedroom!
[LOG] [17:40:00] Sending notification to homeowner...

Time: 17:41:00
[READING] Living Room Motion: Motion detected
[ALERT!] 🚨 HIGH: SECURITY: Motion detected in Living Room while in AWAY mode!
[LOG] [17:41:00] Sending notification to homeowner...
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [17:41:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 33°F (Out of range)
[ALERT!] ⚠️ MEDIUM: SAFETY: Kitchen temperature is 33°F!
[LOG] [17:41:00] Sending notification to homeowner...
[READING] Bedroom Smoke: CLEAR

## Edge case I handled
 My check uses `if / elif`, with the safety rule first and the comfort rule second, so the program prints one safety alert and not two alerts for the same reading.