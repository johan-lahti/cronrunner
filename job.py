from datetime import datetime, timedelta
from colorama import Fore, Style
import time

class Job():
    def __init__(self, **kwargs):
        self.path = None
        self.run_interval = 0
        self.last_run = None
        self.next_run = None
        self.delta = timedelta()
        for arg, data in kwargs.items():
            setattr(self, arg, data)


    def interval(self, **kwargs):
        if 'seconds' in kwargs:
            self.delta = self.delta + timedelta(seconds=kwargs['seconds'])
        if 'minutes' in kwargs:
            self.delta = self.delta + timedelta(minutes=kwargs['minutes'])
        if 'hours' in kwargs:
            self.delta = self.delta + timedelta(hours=kwargs['hours'])
        if 'days' in kwargs:
            self.delta = self.delta + timedelta(days=kwargs['days'])

        return self.delta


    def run(self):
        now = datetime.now()
        if self.last_run is None:
            exec(open(self.path).read())
            self.last_run = datetime.now()
            self.next_run = self.last_run + self.delta
            print(self.next_run)

            return None
        
        if now > self.next_run:
            exec(open(self.path).read())
            self.last_run = datetime.now()
            self.next_run = self.last_run + self.delta

            return None            

        else:
            return f"Not ready until: {self.next_run}"



