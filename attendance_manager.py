import csv
from datetime import datetime

# ---------------- Functions ---------------- #

def get_date():
    """Get date from user or use today's date"""
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input == "":
        return datetime.today().strftime("%Y-%m-%d")
    return date_input


def mark_attendance(students):
    """Mark attendance for each student"""
    present_students = []
    absent_students = []

    for name, reg_no in students:
        while True:
            mark = input(f"{name} : {reg_no} (P/A): ").lower().strip()
            if mark == "p":
                present_students.append((name, reg_no, "Present"))
                break
            elif mark == "a":
                absent_students.append((name, reg_no, "Absent"))
                break
            else:
                print("❌ Invalid input. Please enter 'P' for Present or 'A' for Absent.")

    return present_students, absent_students


def save_to_csv(filename, date_today, present_students, absent_students):
    """Save attendance to a CSV file"""
    # Create file with headers if not already exists
    try:
        with open(filename, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Name", "Registration No.", "Status"])
    except FileExistsError:
        pass

    # Append today’s attendance
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        for student in present_students + absent_students:
            writer.writerow([date_today, student[0], student[1], student[2]])
    print(f"✅ Attendance saved to {filename}")


def show_summary(date_today, present_students, absent_students):
    """Print summary of attendance"""
    print("\n✅ Attendance Marked Successfully!\n")

    print("Present Students:")
    for student in present_students:
        print(f"{student[0]} : {student[1]}")

    print("\nAbsent Students:")
    for student in absent_students:
        print(f"{student[0]} : {student[1]}")

    print(f"\n📊 Summary for {date_today}: {len(present_students)} Present, {len(absent_students)} Absent")


# ---------------- Main Program ---------------- #

def main():
    # Students are identified by Name and Roll No or Registration No
    students = [
        ("Faizan", 25108191),
        ("Abdullah", 25108200),
        ("Ghayoor", 25108201),
        ("Hamza", 25108202),
        ("Subhan", 25108203),
        ("Jahanzeb", 25108204),
        ("Malik Saad", 25108205),
        ("Zubair Ahmad", 25108206),
        ("Abdullah", 25108207),
        ("Saqib Amaan", 25108208),
        ("Waleed", 25108209),
        ("Abuzar", 25108210),
        ("Shahan", 25108211)
    ]

    date_today = get_date()
    present_students, absent_students = mark_attendance(students)
    show_summary(date_today, present_students, absent_students)

    # Ask if user wants to save
    choice = input("\nDo you want to save attendance in a CSV file? (Y/N): ").lower().strip()
    if choice == "y":
        save_to_csv("attendance.csv", date_today, present_students, absent_students)
    else:
        print("⚠️ Attendance not saved in a file.")


# Run the program
if __name__ == "__main__":
    main()