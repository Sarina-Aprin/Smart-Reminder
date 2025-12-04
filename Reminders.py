from dataclasses import dataclass


@dataclass
class Reminder:
    title: str
    time: str
    reminder_id: int

    def remind(self):
        raise NotImplementedError("Subclasses must implement remind()")

@dataclass
class SimpleReminder(Reminder):
    def remind(self):
        return f"It is time: {self.title}"

@dataclass
class MeetingReminder(Reminder):
    participants: list
    def remind(self):
        return f"Meeting Reminder: {', '.join(self.participants)} meeting with: {self.title}"

@dataclass
class DailyRoutineReminder(Reminder):
    daily_repeat: bool
    def remind(self):
        repeat_status = "Active" if self.daily_repeat else "Off"
        return f"Daily Routine: ({repeat_status} Daily repeat) {self.title}"