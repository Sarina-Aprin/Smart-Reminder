from dataclasses import dataclass



@dataclass
class SimpleReminder(Reminder):
    def remind(self):
        return f"It is time: {self.title}"

@dataclass
class MeetingReminder(Reminder):
    participants: list[str]
    def remind(self):
        return f"Meeting Reminder: {', '.join(self.participants)} meeting with: {self.title}"

@dataclass
class DailyRoutineReminder(Reminder):
    daily_repeat: bool
    def remind(self):
        status = "Active" if self.daily_repeat else "Off"
        return f"Daily Routine: ({status} Daily repeat) {self.title}"