# HomeGuard Security System

An integrated Python-based smart home security simulation developed and executed in a Jupyter Notebook (`.ipynb`) environment. The system models multi-sensor tracking, dynamic learning, false-alarm mitigation, and automated threat escalation.

---

## Project Overview
The HomeGuard Security System simulates real-time data collection across various smart sensors (motion, temperature, door status, and smoke detectors). It evaluates ambient conditions dynamically, detects critical environmental risks, and generates automated activity logs and daily reports.

---

## Implementation Details (Challenges 1–4)

### Challenge 1: Learning Mode (`LearningModeTracker`)
* Dynamically establishes ambient temperature baselines using historical sensor readings.
* Identifies temperature anomalies relative to learned baseline boundaries rather than rigid static limits.

### Challenge 2: False-Alarm Detection (`FalseAlarmFilter`)
* Tracks consecutive abnormal sensor cycles to eliminate transient false alarms.
* Only escalates threats after confirmed, sequential triggering events.

### Challenge 3: Daily Summary Report (`generate_summary_report`)
* Consolidates sensor events, total alert counts, and severity levels upon simulation completion.
* Provides high-level operational recommendations based on aggregated system state.

### Challenge 4: Interconnected Smoke & Temperature Escalation (`evaluate_interconnected_alerts`)
* Evaluates sensor data in real-time batches.
* Automatically escalates threat severity when smoke detection (`"DETECTED"`) coincides with elevated temperature readings across multiple zones.

---

## Notebook Structure & Code Flow
1. **Module & Class Definitions**: Defines `Sensor`, `LearningModeTracker`, and `FalseAlarmFilter`.
2. **Core Logic**: Implements `evaluate_interconnected_alerts` and `generate_summary_report`.
3. **Simulation Execution**: `run_simulation()` manages the loop execution, processes sensor batches, and triggers report generation.

---

## How to Run in Jupyter Notebook
1. Open this repository and launch the notebook file in VS Code (or Jupyter Lab).
2. Select your Python kernel.
3. Click **Run All** (or execute cells sequentially) to execute the simulation loop and view real-time log outputs and summary report.