import datetime

class Course:
    def __init__(self, name, starthour, startmin, endhour, endmin, days):
        self.name=name
        self.starthour=int(starthour)
        self.startmin=int(startmin)
        self.endhour=int(endhour)
        self.endmin=int(endmin)
        self.days=days
    
    # Returns true if the class is currently happening
    def isInClass(self):
        now = datetime.datetime.now()
        starttime = now.replace(hour=self.starthour, minute=self.startmin, second=0, microsecond=0)
        endtime = now.replace(hour=self.endhour, minute=self.endmin, second=0, microsecond=0)
        # returns true if it is after start time, before end time, and on a proper day
        return ((now > starttime) & (now < endtime) & (str(now.weekday()) in self.days))
    
    # Returns the end time formatted the following:
    # HH:MM PM  ||  HH:MM AM
    def getEndTimeString(self):
        # yes i know this probably can be done shorter i'm new to python give me a break
        ampm = "AM"
        hour = self.endhour
        min = self.endmin
        if hour > 12:
            hour -= 12
            ampm = "PM"
            if hour == 0: hour = 12
        endtime = datetime.time(hour, min, 0, 0)
        return endtime.strftime("%H:%M") + " " + ampm