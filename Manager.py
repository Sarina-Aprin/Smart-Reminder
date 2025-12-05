import logging

logging.basicConfig(filename="reminder.log",
                    level=logging.INFO,
                    format="%(levelname)s:%(message)s",
                    encoding="utf-8")

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, reminder):
        if not reminder.title or not reminder.time:
            logging.error(f"Reminder {reminder.reminder_id} missing title or time.")
            return
        self.reminders.append(reminder)
        logging.info(f"Reminder added: {reminder.reminder_id} - {reminder.title}")

    def remove_reminder(self, reminder_id):
        self.reminders = [r for r in self.reminders if r.reminder_id != reminder_id]
        logging.warning(f"Reminder {reminder_id} deleted.")

    def list_reminders(self):
        return [f"{r.reminder_id}: {r.title} @ {r.time}" for r in self.reminders]

    def find_by_id(self, reminder_id):
        return next((r for r in self.reminders if r.reminder_id == reminder_id), None)

    def snooze(self, reminder_id: int, minutes: int):
        reminder = self.find_by_id(reminder_id)
        if not reminder:
            logging.error(f"Snooze failed: reminder {reminder_id} not found.")
            return

        try:
            hh, mm = map(int, reminder.time.split(":"))
            from datetime import datetime, timedelta
            new_time = (datetime(2000,1,1,hh,mm) + timedelta(minutes=minutes)).strftime("%H:%M")

            old_time = reminder.time
            reminder.time = new_time
            logging.info(f"Reminder {reminder_id} snoozed {minutes} minutes ({old_time} -> {new_time})")
        except Exception as e:
            logging.error(f"Snooze error for reminder {reminder_id}: {e}")

    def execute_all(self):
        for r in self.reminders:
            try:
                msg = r.remind()
                print(msg)
                logging.info(f"Reminder {r.reminder_id} executed: {msg}")
            except Exception as e:
                logging.error(f"Error executing reminder {r.reminder_id}: {e}")

    def list_by_category(self, category: str):
        return [r for r in self.reminders if r.category == category]

    def reminder_group(self, group_by="type"):
        groups = {}
        for r in self.reminders:
            key = (
                type(r).__name__ if group_by == "type"
                else r.time if group_by == "time"
                else r.category if group_by == "category"
                else None
            )
            if key is not None:
                groups.setdefault(key, []).append(r)
        return groups
