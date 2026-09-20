# 🐍 100 Days of Python Code Challenge

> A structured, daily Python learning journey — from absolute basics to real-world mini-projects — with one coding task and one hands-on project per day.

---

## 📖 About This Repository

This repo documents my **#100DaysOfCode** Python challenge. Each day covers a specific Python concept through two files:

| File | Purpose |
|------|---------|
| `taskN.py` | Exercises and concept exploration for the day's topic |
| `projectN.py` | A practical mini-project that applies what was learned |

The goal is to build a strong Python foundation, one concept at a time, while shipping something useful every single day.

---

## 📅 Progress Tracker

| Day | Topic | Task | Project |
|-----|-------|------|---------|
| ✅ [Day 1](#-day-1--python-basics--io) | Python Basics & I/O | `print`, `input`, string concatenation, `len()`, variables | 🎸 Band Name Generator |
| ✅ [Day 2](#-day-2--data-types--type-casting) | Data Types & Type Casting | Strings, integers, floats, booleans, subscripting, f-strings, `type()` | 💰 Tip Calculator |
| ✅ [Day 3](#-day-3--control-flow--conditionals) | Control Flow & Conditionals | `if / else / elif`, modulo operator `%`, nested conditionals | 🏝️ Treasure Island Game |
| ✅ [Day 4](#-day-4--lists--the-random-module) | Lists & the `random` Module | List methods (`pop`, `remove`, `extend`), `random.choice`, `random.randint` | ✂️ Rock, Paper, Scissors |
| ✅ [Day 5](#-day-5--for-loops--built-in-functions) | For Loops & Built-in Functions | `for` loops, `range()`, `sum()`, `max()`, `min()`, `random.shuffle`, `random.sample` | 🔐 Password Generator |
| ✅ [Day 6](#-day-6--functions--while-loops) | Functions & While Loops | Defining & calling functions (`def`), `while` loops | 🧾 Kenyan Payslip Generator |
| ✅ [Day 7](#-day-7--combining-concepts) | Combining Concepts | — | 💀 Hangman Game (Stage 1) |
| ⏳ Day 8–100 | *Coming soon...* | | |

---

## 📚 Day-by-Day Breakdown

---

### 🗓️ Day 1 — Python Basics & I/O

**Concepts covered:**
- `print()` — outputting text to the console
- String concatenation using `+`
- Escape characters (`\n`)
- `input()` — collecting user input at runtime
- Variables as data containers
- `len()` — measuring string length

**Project: 🎸 Band Name Generator**  
Asks the user for their city and pet name, then combines them to generate a fun band name.

```
Welcome to the band name generator
Enter the name of your city: Nairobi
Enter the name of your pet: Rex
Your Band name is Nairobi Rex
```

---

### 🗓️ Day 2 — Data Types & Type Casting

**Concepts covered:**
- Core data types: `str`, `int`, `float`, `bool`
- Subscripting strings (positive & negative indexing)
- Checking data types with `type()`
- Type casting: `int()`, `float()`, `str()`
- Type errors and how to avoid them
- f-strings for clean string formatting

**Project: 💰 Tip Calculator**  
Calculates and splits a restaurant bill including a tip percentage among a group of people. Uses type casting to safely handle user input and `round()` for clean currency output.

```
Welcome to the tip Calculator
Whats the total amount of bill in Ksh: 5000
How much tip would you like to give in %: 10
How many people would be splitting this bill?: 4
The bill for each is: Ksh 1375.0
```

---

### 🗓️ Day 3 — Control Flow & Conditionals

**Concepts covered:**
- `if / else` statements
- `elif` for multiple branches
- The modulo operator `%` (odd/even detection)
- Nested `if` statements for multi-level decision making
- `.lower()` and `.strip()` for input sanitization

**Project: 🏝️ Treasure Island Adventure Game**  
A text-based, choose-your-own-adventure game where the player navigates a series of decisions (direction → activity → door colour) to find hidden treasure. Wrong choices lead to "Game Over."

```
Welcome to Treasure Island. Your mission is to find the treasure.
Which direction do you want to go: (left / right) left
What activity would you like to do: (swim / wait) wait
Which door would you like to open: (blue / red / yellow) yellow
You Win!
```

---

### 🗓️ Day 4 — Lists & the `random` Module

**Concepts covered:**
- Lists as ordered data structures
- List methods: `.pop()`, `.remove()`, `.extend()`
- Importing modules with aliases (`import random as r`)
- `random.randint()` — generating random integers
- `random.choice()` — picking a random item from a list
- Index-based random selection

**Project: ✂️ Rock, Paper, Scissors**  
A fully playable Rock, Paper, Scissors game against the computer. Features input validation, random computer moves, and win/lose/draw logic.

```
Welcome to the: -->  |ROCK --> PAPER --> SCISSORS| GAME
What do you choose: 0: for (rock), 1: for (paper), 2: for (scissors): 0
You chose: 0
Computer chose: 2
You Win!
```

---

### 🗓️ Day 5 — For Loops & Built-in Functions

**Concepts covered:**
- `for` loops to iterate over lists and ranges
- `range()` for generating number sequences
- Built-in functions: `sum()`, `max()`, `min()`
- Manual implementations of sum/max/min using loops (to understand the internals)
- `random.shuffle()` — in-place list shuffling
- `random.sample()` — selecting unique random items

**Project: 🔐 Password Generator**  
Generates a secure, randomised password based on the user's specified count of letters, numbers, and symbols. The password characters are shuffled before output to prevent predictable ordering.

```
HELLO! Welcome to your favourite password generator
Enter the number of letters: 8
How many numbers: 3
Enter the number of symbols: 2
Here is your hard to hack password!
aP#3kRm9$Bq2L
```

---

### 🗓️ Day 6 — Functions & While Loops

**Concepts covered:**
- Defining functions with `def`
- Calling functions
- `while` loops and infinite loop awareness
- Functions with parameters and return values
- Structuring programs with multiple helper functions

**Project: 🧾 Kenyan Payslip Generator**  
A payslip calculator tailored to Kenyan statutory deductions. Given an employee's name and gross salary, it calculates and prints a formatted payslip showing:

- **NHIF** — National Hospital Insurance Fund (tiered deduction)
- **NSSF** — National Social Security Fund (6% capped at Ksh 2,160)
- **PAYE** — Pay As You Earn income tax (16% above Ksh 24,000)
- **Net Pay** after all deductions

```
========================================
    PAYSLIP - Amina Wanjiku
========================================
  Gross salary:     Ksh 85000
   NHIF:            Ksh 950
   NSSF:            Ksh 2160
   PAYE:            Ksh 9760
========================================
   NET PAY:        Ksh 72130.0
========================================
```

---

### 🗓️ Day 7 — Combining Concepts

**Project: 💀 Hangman Game (Stage 1)**  
The beginning of a classic Hangman game. The computer randomly selects a word from a curated list, displays underscores as placeholders, and replaces them with correctly guessed letters. This stage lays the foundation for a full, multi-round Hangman implementation.

```
_ _ _ _ _ _ _ _ _ _ _    <- random word chosen
Guess a letter: e
_ e _ e _ _ _ _ _ _ _
```

---

## 🛠️ How to Run Any Project

**Requirements:** Python 3.x (no external libraries needed — only built-in modules are used)

```bash
# Navigate to any day's folder
cd Day1

# Run a task or project file
python task1.py
python project1.py
```

---

## 🧩 Concepts Covered So Far

| Concept | Day Introduced |
|---------|---------------|
| `print()`, `input()`, variables | Day 1 |
| String concatenation & `len()` | Day 1 |
| Data types & type casting | Day 2 |
| f-strings & subscripting | Day 2 |
| `if / elif / else` & nested conditionals | Day 3 |
| Modulo operator `%` | Day 3 |
| Lists & list methods | Day 4 |
| `random` module | Day 4 |
| `for` loops & `range()` | Day 5 |
| `sum()`, `max()`, `min()` | Day 5 |
| `random.shuffle()` & `random.sample()` | Day 5 |
| Functions (`def`) | Day 6 |
| `while` loops | Day 6 |
| Multi-function program design | Day 6 |
| Combining loops, conditionals & functions | Day 7 |

---

## 📜 Pledge

This challenge is backed by a personal commitment to code every day for 100 days. See [`pledge.pdf`](./pledge.pdf) for the signed pledge.

---

## 👤 Author

**Nelly**  
*Documenting every step of the Python journey — one day at a time.* 🚀

---

> ⭐ If you find this helpful or are on a similar journey, feel free to star the repo and follow along!
