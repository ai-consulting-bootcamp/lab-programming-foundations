# HomeGuard Lab Proof

## Program path
/Users/elifyurdakul/Downloads/day2/lab-programming-foundations/homeguard_system.py

## Run command
/usr/local/bin/python3 /Users/elifyurdakul/Downloads/day2/lab-programming-foundations/homeguard_system.py

## Fixed-case output
Time: 19:52:52
Mode: AWAY
[READING] Living Room Motion: No activity
[READING] Front Door: OPEN
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [19:52:52] Sending notification to homeowner...
[READING] Kitchen Temperature: 60°F (Normal)
[READING] Bedroom Smoke: CLEAR

=== Fixed Checks ===
Door in AWAY: True
Door in HOME: False
Smoke in HOME: True
80°F in HOME: True
80°F in AWAY: False
35°F in AWAY: False
Door in SLEEP: FalseTime: 20:04:55
Mode: AWAY
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 77°F (Normal)
[READING] Bedroom Smoke: SMOKE DETECTED
[ALERT!] 🚨 HIGH: SAFETY: Smoke detected in Bedroom!
[LOG] [20:04:55] Sending notification to homeowner...

Time: 20:04:55
Mode: HOME
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 95°F (Abnormal)
[ALERT!] 🚨 NOTICE: COMFORT: Temperature 95°F is outside the comfort range in Kitchen.
[LOG] [20:04:55] Sending notification to homeowner...
[READING] Bedroom Smoke: SMOKE DETECTED
[ALERT!] 🚨 HIGH: SAFETY: Smoke detected in Bedroom!
[LOG] [20:04:55] Sending notification to homeowner...

Time: 20:04:55
Mode: SLEEP
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 84°F (Normal)
[READING] Bedroom Smoke: CLEAR
Smoke in SLEEP: True

## Three-cycle output
Time: 20:04:55
Mode: AWAY
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 77°F (Normal)
[READING] Bedroom Smoke: SMOKE DETECTED
[ALERT!] 🚨 HIGH: SAFETY: Smoke detected in Bedroom!
[LOG] [20:04:55] Sending notification to homeowner...

Time: 20:04:55
Mode: HOME
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 95°F (Abnormal)
[ALERT!] 🚨 NOTICE: COMFORT: Temperature 95°F is outside the comfort range in Kitchen.
[LOG] [20:04:55] Sending notification to homeowner...
[READING] Bedroom Smoke: SMOKE DETECTED
[ALERT!] 🚨 HIGH: SAFETY: Smoke detected in Bedroom!
[LOG] [20:04:55] Sending notification to homeowner...

Time: 20:04:55
Mode: SLEEP
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 84°F (Normal)
[READING] Bedroom Smoke: CLEAR

## How the program works
The sensors check for motion, an open door, unusual temperatures, and smoke. The program checks each reading according to the current mode, such as AWAY, HOME, or SLEEP. If it finds something abnormal, it displays an alert and records a log message.

## Edge case
he temperature is not abnormal because the rule alerts only when it is below 35°F or above 95°F. The comparison is strict (< 35), so 35 itself does not trigger that alert.