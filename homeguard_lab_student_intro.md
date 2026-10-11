# Lab: HomeGuard – Smart Home Alarm

**Time:** 90–120 minutes
**File to create:** `homeguard_system.ipynb` (a Jupyter notebook)

By the end of this lab you can say:

> *"I built a fake home alarm in Python to practise if/else, dictionaries, functions and classes."*

---

## 1. The story

The Peterson family is on vacation. Their house has **4 sensors**:

| Sensor | Room | What it tells us |
|---|---|---|
| Motion | Living Room | Is someone moving? |
| Door | Front Door | Is the door open? |
| Temperature | Kitchen | How hot or cold is it? |
| Smoke | Bedroom | Is there smoke? |

**Your job:** write a Python program that watches the house and **prints an alert when something is wrong**.

### Where do the readings come from?

There are no real sensors. Python's **`random` module** invents the readings for you. It's a built-in module that picks random values:

```python
import random

random.randint(30, 100)    # a random whole number from 30 to 100 → a temperature
random.random() < 0.3      # True about 30% of the time → "is there motion?"
```

So every time your program "reads" a sensor, `random` decides the value. That's why this is called a **simulator**.

---

## 2. The one key rule: event + mode

Every reading is an **event**: the door opened, smoke appeared, the kitchen got cold.

The house also has a **mode**, which tells the program who is home:
- **HOME**: the family is inside
- **AWAY**: nobody is home
- **SLEEP**: the family is asleep *(optional)*

Your program combines the two:

```
EVENT  +  MODE  =  ALERT or NOT
```

The same event can be normal or dangerous, depending on the mode:

| Event | HOME | AWAY | SLEEP *(optional)* |
|---|---|---|---|
| Motion or door opens | nothing | 🚨 HIGH security | ⚠️ MEDIUM security |
| Smoke | 🔥 CRITICAL | 🔥 CRITICAL | 🔥 CRITICAL |
| Temp below 35°F or above 95°F | ⚠️ safety alert | ⚠️ safety alert | ⚠️ safety alert |
| Temp outside 65–75°F | 💡 comfort notice | nothing | nothing |

> *The sensor tells you what happened. The mode tells you if it matters.*

---

## 3. The finish line

This is what your program should print at the end:

```
=== HomeGuard Security System ===
Time: 14:30:00
Mode: AWAY

[READING] Living Room Motion: No activity
[READING] Front Door: CLOSED
[READING] Kitchen Temperature: 68°F (Normal)
[READING] Bedroom Smoke: CLEAR

Time: 14:31:00
[READING] Front Door: OPENED
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
[LOG] [14:31:00] Sending notification to homeowner...
```

---

## 4. How to build it: the 7 steps

Now you know **what** to build. Here is **how**, step by step, following the lab on the portal. **Run your code after every step.**

### Step 1: Set up the project

- Create the notebook `homeguard_system.ipynb` and select your `bootcamp-env` kernel (top right).
- Use **one cell per step**, so you can run and check each step on its own.
- Add a header comment with your name and what the program does.
- Import `random` (for the readings) and `datetime` (for the time).

**Check:** the cell runs without errors.

### Step 2: Define the sensors and the alerts (dictionaries)

**A sensor** is one dictionary with 4 fields:

| Field | Example |
|---|---|
| `id` | `2` |
| `location` | `"Front Door"` |
| `type` | `"door"` (or `"motion"`, `"temperature"`, `"smoke"`) |
| `current_value` | `None` at the start, because nothing has been read yet |

Write a function that creates the 4 sensors of the house and puts them in a **list**.

**An alert** is also a dictionary. Its fields come from the sample output:

```
[ALERT!] 🚨 HIGH: SECURITY: Front Door opened while in AWAY mode!
            ────  ────────  ─────────────────────────────────────
         severity category                 message
```

| Field | Example | Meaning |
|---|---|---|
| `time` | `14:31:00` | When it happened (from the `[LOG]` line) |
| `severity` | `HIGH` | How serious it is: CRITICAL, HIGH, MEDIUM or LOW |
| `category` | `SECURITY` | What kind of problem: SAFETY, SECURITY or COMFORT |
| `message` | `Front Door opened while in AWAY mode!` | What exactly happened |

Also store the mode in a variable: `system_mode = "AWAY"`.

**Check:** print your sensor list. You see 4 dictionaries, each with `current_value: None`.

### Step 3: Write the conditions (if/else)

- Save the limits as constants at the top, for example `FREEZE_TEMP = 35`.
- Write **one function** that takes a sensor and the mode, and uses if/else to follow the rule table from section 2.
- It **returns an alert** if something is wrong, or **`None`** if everything is fine.

**Check:** set a value by hand and test it. For example, a door that is open in AWAY mode returns an alert, and the same door in HOME mode returns `None`.

### Step 4: Build the functions

Write 4 small functions, one job each:

| Function | Job |
|---|---|
| Generate a reading | Use `random` to give a sensor a new value |
| Process the readings | Read every sensor and check it with your Step 3 function |
| Trigger an alert | Print the `[ALERT!]` line |
| Log the event | Print the `[LOG]` line and save it in a list |

**Check:** run it once in AWAY and once in HOME, and compare the alerts.

### Step 5: Create the `Sensor` class

- Turn the sensor dictionary into a `Sensor` class with an `__init__` method.
- Add 3 methods: `read()` makes a new reading, `isAbnormal()` checks it, and `reset()` clears the value.
- Update your code to use `Sensor` objects instead of dictionaries.

**Why now?** You've already built everything with dictionaries, so you can see how a class keeps the data and its functions together.

**Check:** create one `Sensor` object, call `read()`, and print its value.

### Step 6: Put it all together

- Write a **main loop** that reads all sensors **at least 3 times** (3 "minutes").
- Print the header, the time and the mode, and format every line like the sample output.

**Check:** your output looks like the finish line in section 3.

### Step 7: Test your system

| Test | How | You should see |
|---|---|---|
| Security | Run with `system_mode = "AWAY"` | Motion or door alerts |
| Safety | Look for very low or high temperatures, or smoke | Safety alerts in any mode |
| Comfort | Run with `system_mode = "HOME"` | Comfort notices, and no security alerts |

---

## 5. Keep it simple

- Use only **AWAY and HOME**. SLEEP is optional.
- **"Door open for more than 5 minutes"** is a bonus. Skip it at first.
- Add **`random.seed(42)`** at the top, so you get the **same output every time** you run it.

**Two common mistakes:**

- `mode == "AWAY"` **compares**. `mode = "AWAY"` **assigns**. Use `==` in if statements.
- Compare numbers with numbers: `temp < 35`, not `temp < "35"`.

---

## 6. What to submit

| File | Contains |
|---|---|
| `homeguard_system.ipynb` | Your notebook, with comments (or a Markdown cell) for each step, and the output visible |
| `lab_proof.md` | How to run it (open the notebook and click **Run All**), your output (**at least 3 rounds** and **at least 1 alert**), and **one edge case** you handled |

---

## 7. Using AI

✅ **Allowed:** ask AI to **review** your code, find bugs, or suggest missing test cases.
❌ **Not allowed:** ask AI to **write** the program for you.

---

## Common questions

| Question | Answer |
|---|---|
| *What does SLEEP mode do?* | The lab doesn't say. It's optional. If you add it, decide the rule yourself and explain it in `lab_proof.md` |
| *Do I need 4 separate functions for 4 sensors?* | No. One check function with if/else per sensor type is fine |
| *My output is different every time* | Add `random.seed(42)` at the top |

---

## Finished early? Bonus ideas

- Trigger a break-in alert only when **two** sensors detect activity at the same time.
- Print a **summary** at the end: how many alerts of each severity.
- Detect a door left open for **more than 5 minutes**.

---

> **Remember: event + mode = alert or not.** Run your code after every step, and ask for help when you're stuck.
