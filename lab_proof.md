# HomeGuard - lab_proof

**Program path:** `Bootcamp_IA/Semana 1/homeguard/homeguard_system.ipynb`
**Run command:** open the notebook in VS Code (kernel `bootcamp-semana2`, Python 3.11) and click **Run All**.

## How the code works (2-3 sentences)
Each sensor is first described as a dictionary and then as a `Sensor` object with `read()`, `isAbnormal()` and `reset()`. In every iteration (one simulated minute) the loop reads all sensors with `random`, applies the rules in `check_reading()` (AWAY security, temperature <35°F / >95°F, smoke, HOME comfort 65-75°F, door open >5 min) and prints and logs an alert when a rule returns one. If two or more security alerts happen in the same minute, it raises a "possible break-in" alert.

## Fixed cases (deterministic)
| Input | Expected | Observed |
|---|---|---|
| temperature 34, HOME | CRITICAL frozen pipe | `{'level': 'CRITICAL', 'message': 'SAFETY: 34°F - frozen pipe risk!'}` |
| temperature 35, HOME | not critical, comfort only | `{'level': 'LOW', 'message': 'COMFORT: 35°F is outside 65-75°F'}` |
| motion True, HOME | no alert | `None` |
| motion True, AWAY | HIGH security | `{'level': 'HIGH', 'message': 'SECURITY: Motion detected while in AWAY mode!'}` |
| smoke True, HOME | CRITICAL fire | `{'level': 'CRITICAL', 'message': 'SAFETY: Smoke detected - fire risk!'}` |

## Simulator output (AWAY, 3 iterations, seed 7)
```
=== HomeGuard Security System ===
Mode: AWAY

Time: 14:30:00
[READING] Living Room Motion: No activity
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [14:30:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 36°F
[READING] Bedroom Smoke: CLEAR

Time: 14:31:00
[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 37°F
[READING] Bedroom Smoke: CLEAR

Time: 14:32:00
[READING] Living Room Motion: Activity detected
[ALERT!] 🚨 HIGH: SECURITY: Motion detected while in AWAY mode!
[LOG] [14:32:00] Sending notification to homeowner...
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [14:32:00] Sending notification to homeowner...
[READING] Kitchen Temperature: 83°F
[READING] Bedroom Smoke: CLEAR
[ALERT!] 🚨 CRITICAL: Multiple sensors triggered - possible break-in!
[LOG] [14:32:00] Sending notification to homeowner...

Total events logged: 4
```

## Edge case: exactly 35°F
The rule is "temperature **below** 35°F", so the code uses `<`, not `<=`. At exactly 35°F there is no critical frozen-pipe alert (`35 < 35` is `False`). In HOME mode it still raises a comfort notice because 35 is outside 65-75°F. Using `<=` would send a false critical alarm at 35°F.

## Design choice
`check_reading()` returns the alert (`return`) instead of printing it. This lets me test the rules with fixed values before adding randomness, and lets the loop decide how to display and log the alert.

## Notes
- SLEEP mode not implemented (presented as optional in class).
- Code written with AI assistance (Claude) and run by me in VS Code.
