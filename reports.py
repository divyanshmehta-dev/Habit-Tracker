from collections import Counter

from storage import get_all_habits, get_all_completions


def show_stats():
    """Show how many times each habit has been completed."""
    habits = get_all_habits()
    if not habits:
        print("No habits defined yet.")
        return

    completions = get_all_completions()
    completed_counts = Counter()

    for c in completions:
        if c.get("done") == "1":
            completed_counts[c["habit_id"]] += 1

    print("\nHabit statistics:")
    for h in habits:
        hid = h["habit_id"]
        count = completed_counts.get(hid, 0)
        print(f'{hid}. {h["name"]}: completed {count} time(s)')
