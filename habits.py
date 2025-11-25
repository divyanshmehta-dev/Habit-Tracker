from datetime import date

from storage import get_all_habits, add_habit_to_file, add_completion_to_file


def add_habit():
    """Ask user for habit details and save a new habit."""
    name = input("Enter habit name (e.g., Gym, Study): ").strip()
    if not name:
        print("Habit name cannot be empty.")
        return

    category = input("Enter habit category (e.g., Health, Study): ").strip()
    if not category:
        category = "General"

    habits = get_all_habits()
    if habits:
        max_id = max(int(h["habit_id"]) for h in habits)
    else:
        max_id = 0

    new_id = max_id + 1
    add_habit_to_file(new_id, name, category)
    print(f"Habit added with ID {new_id}.")


def list_habits():
    """Print all habits."""
    habits = get_all_habits()
    if not habits:
        print("No habits found. Add one first.")
        return

    print("\nYour habits:")
    for h in habits:
        print(f'{h["habit_id"]}. {h["name"]} ({h["category"]})')


def mark_habit_done_today():
    """Ask which habit to mark as done for today and store completion."""
    habits = get_all_habits()
    if not habits:
        print("No habits yet. Add one first.")
        return

    list_habits()
    chosen = input("Enter habit ID to mark as done for today: ").strip()

    if not any(h["habit_id"] == chosen for h in habits):
        print("Invalid habit ID.")
        return

    today_str = date.today().isoformat()
    add_completion_to_file(chosen, today_str)
    print(f"Habit {chosen} marked as done for {today_str}.")
