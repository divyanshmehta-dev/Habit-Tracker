# Habit Tracker (IPP – Introduction to Problem Solving and Programming)

## 1. Introduction
This project is a simple **command-line Habit Tracker** implemented in Python.  
It helps a user define daily habits (such as Gym, Study, Reading), mark them as completed for the day, and view basic statistics.

The project demonstrates problem solving, modular programming, and basic file handling using CSV.

---

## 2. Problem Statement
Students and professionals often try to build good habits but lose track of their consistency. Without a proper record, it is hard to know whether they are actually following the routine.

This project provides a minimal, text-based habit tracker that allows users to log their daily habit completion and quickly view aggregated statistics.

---

## 3. Objectives
- Allow the user to **create and manage** a list of habits.
- Allow the user to **mark a habit as completed** for the current day.
- Provide **basic statistics** showing how many times each habit has been completed.
- Store all data in CSV files so that information is not lost when the program exits.

---

## 4. Functional Requirements

1. **Add Habit**
   - The user can enter a habit name (e.g., "Gym") and a category (e.g., "Health").
   - The system assigns a unique habit ID and stores it.

2. **List Habits**
   - The system displays all existing habits with their IDs and categories.

3. **Mark Habit as Done**
   - The user selects a habit by ID.
   - The system records a completion entry for the current date.

4. **View Habit Statistics**
   - The system shows, for each habit, how many times it has been completed.

---

## 5. Non-Functional Requirements

- **Usability**  
  - Simple text-based menu, easy to understand for beginners.

- **Reliability**  
  - Data is stored in CSV files inside the `data/` folder so it persists across runs.

- **Maintainability**  
  - Code is separated into multiple Python modules:
    - `main.py`, `habits.py`, `storage.py`, `reports.py`

- **Error Handling**  
  - Basic checks for invalid menu options and invalid habit IDs.

---

## 6. System Design

### 6.1 Architecture Overview

- **User** interacts with `main.py` via the terminal.
- `main.py` calls functions from:
  - `habits.py` for habit-related actions
  - `storage.py` for file operations
  - `reports.py` for statistics
- `storage.py` reads/writes to CSV files:
  - `data/habits.csv`
  - `data/completions.csv`

### 6.2 Modules

- `main.py`
  - Shows menu and routes user choices.
- `habits.py`
  - Add new habit, list habits, mark habit done today.
- `storage.py`
  - Ensure data files exist, read/write habits and completion records.
- `reports.py`
  - Read data and compute completion counts per habit.

---

## 7. Data Design

### 7.1 `data/habits.csv`

Columns:
- `habit_id` – unique integer ID
- `name` – habit name
- `category` – habit category (e.g., Health, Study)

### 7.2 `data/completions.csv`

Columns:
- `habit_id` – refers to a habit in `habits.csv`
- `date` – date of completion in `YYYY-MM-DD` format
- `done` – "1" when the habit is completed

---

## 8. Implementation Details

- Language: **Python 3**
- No external libraries are required (only standard library: `csv`, `os`, `datetime`, `collections`).
- Code is written in a beginner-friendly style with simple functions.

---

## 9. How to Run the Project

1. Make sure Python 3 is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python main.py
