from apscheduler.schedulers.blocking import BlockingScheduler
from main import send_it


sched = BlockingScheduler()

sched.add_job(send_it,'interval',seconds = 5)
sched.start()
