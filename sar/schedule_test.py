import schedule
import time

idx = 0
idx2 = 0

def job():
    global idx
    idx = idx + 1
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(time_str, "I'm working...", idx)
    if(idx >= 3):
        print("cancel job: ",job.__name__)
        return schedule.CancelJob

def job2():
    global idx2
    idx2 = idx2 + 1
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(time_str, "I dont want to work...", idx2)
    if(idx2 == 2):
        # tasks = schedule.get_jobs('hi')
        # for task in tasks:
        #     print("schedule.cancel_job({}) <- task.tag".format(task.job_func.func.__name__))
        #     schedule.cancel_job(task)
        print("clear task with tag('hi')")
        schedule.clear('hi')
        
def job3(name = "boy"):
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(time_str, 'Hi, {}~'.format(name))

task1 = schedule.every(2).seconds.do(job).tag("postive")
task2 = schedule.every(4).seconds.do(job2).tag("unpostive")
task3 = schedule.every(3).seconds.do(job3).tag('hi')

if __name__ == "__main__":
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(time_str, "schedule start")
    while True:
        schedule.run_pending()
        time.sleep(1)