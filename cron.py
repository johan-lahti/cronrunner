from cronrunner.job import Job
from datetime import datetime, timedelta
from colorama import Fore, Style
import time


class Cron():
    """
    This class acts as the scheduler,
    you add the Jobs to it, and when ready: cron.start()
    """
        
    def __init__(self):
        self.jobs = []

    def add_job(self, job: Job) -> None:
        self.jobs.append(job)
        
        
    def start(self):

        print("\r\n")

        print(Fore.GREEN + 'Starting cron')
        print(Style.RESET_ALL)
        print("Jobs:")
        for job in self.jobs:
            print(f"* {job.path}\t-\tInterval:{job.run_interval}s")

        print("\r\nPress CTRL+C to exit.")

        while True:
            for job in self.jobs:
                job.run()
                time.sleep(1)
