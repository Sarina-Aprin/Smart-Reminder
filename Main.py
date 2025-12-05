from ID_generator import IDGenerator
from Reminders import SimpleReminder, MeetingReminder, DailyRoutineReminder
from Manager import ReminderManager

idg = IDGenerator()
m = ReminderManager()

r1 = SimpleReminder(title="Buy bread", time="18:30", reminder_id=idg.next_id(), category="Personal")
r2 = MeetingReminder(title="Team meeting", time="09:00", reminder_id=idg.next_id(), participants=["Ali","Sara"], category="Work")
r3 = DailyRoutineReminder(title="Workout", time="07:00", reminder_id=idg.next_id(), daily_repeat=True, category="Health")

m.add_reminder(r1)
m.add_reminder(r2)
m.add_reminder(r3)

print("Work reminders:", [r.title for r in m.list_by_category("Work")])

m.snooze(r1.reminder_id, 15)