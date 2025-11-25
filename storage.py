import csv
import os

HABITS_FILE = "data/habits.csv"
COMPLETIONS_FILE = "data/completions.csv"


def ensure_data_files():
    """Create data folder and CSV files with headers if they don't exist."""
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["habit_id", "name", "category"])

    if not os.path.exists(COMPLETIONS_FILE):
        with open(COMPLETIONS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["habit_id", "date", "done"])


def get_all_habits():
    """Return a list of all habits as dictionaries."""
    ensure_data_files()
    with open(HABITS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def add_habit_to_file(habit_id, name, category):
    """Append a new habit to the habits CSV file."""
    ensure_data_files()
    with open(HABITS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([habit_id, name, category])


def add_completion_to_file(habit_id, date_str):
    """Append a completion record (done = 1) to the completions CSV file."""
    ensure_data_files()
    with open(COMPLETIONS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([habit_id, date_str, "1"])


def get_all_completions():
    """Return a list of all completion records as dictionaries."""
    ensure_data_files()
    with open(COMPLETIONS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
