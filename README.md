This project implements a Reminder Management System in Python. It allows users to create, manage, and execute different types of reminders. 
Each reminder has a unique ID generated automatically, and all activities (creation, deletion, execution, errors) are logged for tracking.
Reminder Types
1. SimpleReminder → A basic reminder with a title and time.
2. MeetingReminder → Includes participants in addition to title and time.
3. DailyRoutineReminder → Supports a daily repeat flag (active/inactive).

All reminders share common attributes:
1. title → Reminder title
2. time → Execution time (string format, e.g., "18:30")
3. reminder_id → Unique identifier

Features:
1. Add and remove reminders
2. List all reminders
3. Find reminders by ID
4. Group reminders by type or time
5. Execute all reminders polymorphically (remind() method)
6. Log all actions in reminder.log with levels:
INFO → Reminder added or executed
WARNING → Reminder deleted
ERROR → Invalid reminder (e.g., missing title or time)

How to run?
1. Clone or download the project.
2. Make sure you have Python 3.10+ installed.
3. Run the main file from terminal:
python3 main.py
4. Check reminder.log for activity logs.
Make sure you have Python 3.10+ installed.

Enjoy.
