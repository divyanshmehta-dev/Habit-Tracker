from storage import ensure_data_files
from habits import add_habit, list_habits, mark_habit_done_today
from reports import show_stats


def main():
    ensure_data_files()

    while True:
        print("\n=== HABIT TRACKER (IPSP) ===")
        print("1. Add a new habit")
        print("2. List habits")
        print("3. Mark habit as done for today")
        print("4. View habit stats")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_habit()
        elif choice == "2":
            list_habits()
        elif choice == "3":
            mark_habit_done_today()
        elif choice == "4":
            show_stats()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
