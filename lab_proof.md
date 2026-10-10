# HomeGuard -- Lab Proof

## Program Path

`homeguard_system.ipynb`

## Run Command

Open `homeguard_system.ipynb` in Jupyter Notebook or VS Code, select the
correct Python kernel, and run all cells.

## Fixed Test Cases and Output

### HOME Test

``` text
=== HomeGuard Security System ===
Time: 04:33:39
Mode: HOME

[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 60°F (Abnormal)
[READING] Bedroom Smoke: CLEAR
```

### AWAY Test

``` text
=== HomeGuard Security System ===
Time: 04:33:39
Mode: AWAY

[READING] Living Room Motion: MOTION DETECTED
[READING] Front Door: OPEN
[READING] Kitchen Temperature: 50°F (Abnormal)
[READING] Bedroom Smoke: SMOKE DETECTED

[ALERT!] 🔥 CRITICAL: SAFETY: Smoke detected in Bedroom!
[LOG] [04:33:39] Sending notification to homeowner...
```

### SLEEP Test

``` text
=== HomeGuard Security System ===
Time: 04:33:39
Mode: SLEEP

[READING] Living Room Motion: No activity
[READING] Front Door: OPEN
[READING] Kitchen Temperature: 45°F (Abnormal)
[READING] Bedroom Smoke: CLEAR
```

## Edge Case Explanation

One edge case demonstrated by the fixed tests is the **AWAY test with
several abnormal sensor readings at the same time**. Motion is detected,
the front door is open, the temperature is 50°F, and smoke is detected.

The program reports the smoke condition as a **CRITICAL safety alert**.
This demonstrates that when several conditions occur together, the
critical smoke event takes priority in the current implementation. The
homeowner is then notified and the event is logged.

This is important because smoke represents an immediate safety risk and
should receive the highest priority.
