from ID_generator import IDGenerator
from Reminders import SimpleReminder, MeetingReminder, DailyRoutineReminder
from Manager import ReminderManager

id_gen = IDGenerator()
manager = ReminderManager()

r1 = SimpleReminder("Buy bread", "18:30", id_gen.next_id())
r2 = MeetingReminder("Team", "09:00", id_gen.next_id(), ["Ali", "Sara"])
r3 = DailyRoutineReminder("Workout", "07:00", id_gen.next_id(), True)

manager.add_reminder(r1)
manager.add_reminder(r2)
manager.add_reminder(r3)

manager.execute_all()
