from dataclasses import dataclass, field
from typing import Optional
@dataclass 
class Reminder: 
    title: str 
    time: str 
    reminder_id: int 
    category: Optional[str] = field(default=None)

    def remind(self): 
        raise NotImplementedError("Subclasses must implement remind()") 
    
@dataclass 
class SimpleReminder(Reminder): 
    def remind(self): return f"It is time: {self.title}" 

@dataclass 
class MeetingReminder(Reminder): 
    participants: list[str] = field(default_factory=list)
    def remind(self): 
        return f"Meeting Reminder: {', '.join(self.participants)} meeting with: {self.title}" 

@dataclass 
class DailyRoutineReminder(Reminder): 
    daily_repeat: bool = False

    def remind(self): 
        status = "Active" if self.daily_repeat else "Inactive" 
        return f"Daily Routine: ({status} Daily repeat) {self.title}"