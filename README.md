# python-mini-project-s-
🐍 7 Python mini-projects built in 7 days | Beginner-friendly | 100 Days of Code with Harry Series | Covers input, conditionals, loops, functions, randomization &amp; game logic.
# 🐍 7 Days 7 Python Projects — 100 Days of Code (With Harry Series)

A collection of 7 beginner Python mini-projects built day by day while learning core programming concepts like user input, conditionals, loops, functions, randomization, and more.

---

## 📁 Projects Overview

| Day | Project Name | Key Concept |
|-----|-------------|-------------|
| Day 1 | Band Name Generator | Input & Strings |
| Day 2 | Tip Calculator | Arithmetic & f-strings |
| Day 3 | Treasure Island Adventure | If/Else Conditionals |
| Day 4 | Rock Paper Scissors | Randomization & Lists |
| Day 5 | Password Generator | Random + Shuffle |
| Day 6 | Reeborg Maze Solver | Functions & Loops |
| Day 7 | Hangman Game | Loops, Lists & Game Logic |

---

## 🗂️ Project Details

### Day 1 — Band Name Generator (`day1project.py`)
A fun interactive program that generates a unique band name by combining your hometown and your pet's name.

**Concepts used:** `print()`, `input()`, f-strings

**How to run:**
```bash
python day1project.py
```
**Example:**
```
Welcome to a band name generator !!!
Enter your city name: Mumbai
Enter your pet name: Bruno
Your band name could be Mumbai Bruno
```

---

### Day 2 — Tip Calculator (`day2project.py`)
Calculates the total bill after adding a tip percentage and splits it equally among a group of people.

**Concepts used:** `int()`, arithmetic operators, f-strings

**How to run:**
```bash
python day2project.py
```
**Example:**
```
Welcome to the tip calculator
please enter a bill amount: 100
please enter % tip you want to give: 15
enter no of people to divide a bill: 4
The main bill will be 100 and the amount after tip will be 115.0 and per head amount is 28.75
```

---

### Day 3 — Treasure Island Adventure (`day3project.py`)
A text-based adventure game where the player makes choices to find hidden treasure — or face game over!

**Concepts used:** `if/elif/else`, nested conditionals, user input

**How to run:**
```bash
python day3project.py
```
**Example:**
```
Welcome to tressure Island. Your mission is to find the treasure.
Choose left or right: left
You want to swim or wait: wait
Choose a door: blue or yellow or red: yellow
You won !
```

---

### Day 4 — Rock Paper Scissors (`day4project.py`)
The classic Rock Paper Scissors game where you compete against the computer, which picks its move randomly.

**Concepts used:** `import random`, `random.choice()`, lists, `if/elif/else`

**How to run:**
```bash
python day4project.py
```
**Example:**
```
Welcome to the Rock Paper Scissor game
0 for Rock, 1 for Paper and 2 for Scissors: 0
Your action is: Rock
Computers's action is: Scissors
The Result is: You Won!
```

---

### Day 5 — Password Generator (`day5project.py`)
Generates a strong, randomized password based on your chosen number of letters, numbers, and symbols.

**Concepts used:** `import random`, `random.choice()`, `random.shuffle()`, lists, loops, `join()`

**How to run:**
```bash
python day5project.py
```
**Example:**
```
How many letters do you want? 6
How many numbers do you want? 3
How many symbols do you want? 2
Your password: g3!aX#17mK
```

---

### Day 6 — Reeborg Maze Solver (`day6project.py`)
A solution for the Reeborg's World maze challenge. The robot navigates a maze by jumping over walls using custom functions.

**Concepts used:** Functions, `while` loops, conditionals, reusable logic

> ⚠️ **Note:** This project runs inside [Reeborg's World](https://reeborg.ca/reeborg.html) — a browser-based Python environment. It will not run as a standalone Python script.

**Logic:**
```
- turn_right() is built using three turn_left() calls
- jump() moves the robot over a wall obstacle
- The robot keeps moving forward and jumps whenever a wall is in front
```

---

### Day 7 — Hangman Game (`day7_project.py`)
A fully functional Hangman game with ASCII art stages, a large word bank, lives tracking, and win/lose detection.

**Concepts used:** `import random`, lists, functions, `while` loops, string operations, ASCII art

**How to run:**
```bash
python day7_project.py
```
**Example:**
```
************ WELCOME TO THE HANGMAN GAME ************
********** Guess the letter before you die **********

Lives: 6

Progress: _ _ _ _ _ _

Enter a letter: a
Your guess was CORRECT!

Progress: a _ _ _ _ _
```

---

## 🚀 Getting Started

**Prerequisites:** Python 3.x installed on your machine.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python day1project.py
```

> Run any project by replacing `day1project.py` with the desired file name.

---

## 🛠️ Built With

- Python 3
- Standard Library only (`random` module for Days 4, 5, and 7)
- [Reeborg's World](https://reeborg.ca/reeborg.html) for Day 6

---

## 📚 Learning Series

These projects are built as part of the **"100 Days of Code — Python Bootcamp with Harry"** series, covering beginner to advanced Python concepts step by step.

---

## 📌 Author

Built while following the **100 Days of Code – Python (With Harry)** learning journey.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
