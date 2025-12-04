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
