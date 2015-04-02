from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=5)
def scheduled_job():
    print('This job is run every day at 5am.')
    execfile("worker.py")

sched.start()
