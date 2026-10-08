# Lab Proof: HomeGuard Security System

**Name:** Ben Mayer

## Program path
`course work/week-1/lab-programming-foundations/homeguard_system.ipynb`

## Run command
Open the notebook in Jupyter or VS Code and choose **Restart kernel, then Run All**, or run it from the terminal:
```
cd "/Users/ben-macbook-air/Files/Projects/Ironhack Bootcamp/course work/week-1/lab-programming-foundations"
"/Users/ben-macbook-air/Files/Projects/Ironhack Bootcamp/.venv/bin/jupyter" nbconvert --to notebook --execute homeguard_system.ipynb --output run.ipynb
```
The notebook ends with four fixed cases (Step 7). Their sensor values are scripted, so the output below is the same on every run. The random simulation in Step 6 changes every time.

## Output from the fixed cases
### Case 1: Security (AWAY). The door opens, then motion
```
=== HomeGuard Security System ===
Time: 14:30:00
Mode: AWAY

[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 14:31:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [14:31:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 14:32:00
[READING] Living Room Motion: Motion detected
[ALERT!] 🚨 HIGH: SECURITY: Living Room Motion detected while in AWAY mode!
[LOG] [14:32:00] Sending notification to homeowner...
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 14:33:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR
```

### Case 2: Break-in (AWAY). Door and motion in the same tick
```
=== HomeGuard Security System ===
Time: 02:10:00
Mode: AWAY

[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 02:11:00
[READING] Living Room Motion: Motion detected
[ALERT!] 🚨 HIGH: SECURITY: Living Room Motion detected while in AWAY mode!
[LOG] [02:11:00] Sending notification to homeowner...
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [02:11:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR
[ALERT!] 🚨 CRITICAL: SECURITY: Multiple sensors triggered - possible break-in!
[LOG] [02:11:00] Sending notification to homeowner...
```

### Case 3: Safety (SLEEP). 35 and 95 do not alert, 34, 96 and smoke do
```
=== HomeGuard Security System ===
Time: 03:00:00
Mode: SLEEP

[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 03:01:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 35°F (Outside comfort range)
[READING] Bedroom Smoke: CLEAR

Time: 03:02:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 34°F (Outside comfort range)
[ALERT!] 🚨 CRITICAL: SAFETY: Kitchen Temperature at 34°F - frozen pipe risk!
[LOG] [03:02:00] Sending notification to homeowner...
[READING] Bedroom Smoke: CLEAR

Time: 03:03:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 95°F (Outside comfort range)
[READING] Bedroom Smoke: CLEAR

Time: 03:04:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 96°F (Outside comfort range)
[ALERT!] 🚨 CRITICAL: SAFETY: Kitchen Temperature at 96°F - equipment failure risk!
[LOG] [03:04:00] Sending notification to homeowner...
[READING] Bedroom Smoke: CLEAR

Time: 03:05:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: SMOKE DETECTED
[ALERT!] 🚨 CRITICAL: SAFETY: Bedroom Smoke detected - fire risk!
[LOG] [03:05:00] Sending notification to homeowner...

Time: 03:06:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR
```

### Case 4: Comfort (HOME). 62°F notice, 65°F none, 30°F safety only, door open more than 5 minutes
```
=== HomeGuard Security System ===
Time: 10:00:00
Mode: HOME

[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:01:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 62°F (Outside comfort range)
[ALERT!] 🚨 INFO: COMFORT: Kitchen Temperature at 62°F is outside the 65-75°F comfort range
[LOG] [10:01:00] Sending notification to homeowner...
[READING] Bedroom Smoke: CLEAR

Time: 10:02:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 65°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:03:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 30°F (Outside comfort range)
[ALERT!] 🚨 CRITICAL: SAFETY: Kitchen Temperature at 30°F - frozen pipe risk!
[LOG] [10:03:00] Sending notification to homeowner...
[READING] Bedroom Smoke: CLEAR

Time: 10:04:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:05:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:06:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:07:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:08:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:09:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:10:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[ALERT!] 🚨 INFO: COMFORT: Front Door has been open for 6 minutes
[LOG] [10:10:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 10:11:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[READING] Kitchen Temperature: 70°F (Normal)
[READING] Bedroom Smoke: CLEAR
```

## Edge case: a door left open for exactly 5 minutes (Case 4)
The Front Door opens at 10:04. At 10:09 it has been open exactly 5 minutes and no notice is sent. At 10:10 (6 minutes) the notice `Front Door has been open for 6 minutes` appears once, and 10:11 does not repeat it. I used a strict `>` because the requirement says "more than 5 minutes", so exactly 5 is still normal. The simulation remembers when the door opened (`door_open_since`) and whether it already sent a notice (`door_notice_sent`). Both reset when the door closes, so one opening gives one notice.

Two related boundaries are in Case 3: 35°F and 95°F do not alert, but 34°F and 96°F do, because the limits are "below 35" and "above 95".
