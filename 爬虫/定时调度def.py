"""
测试sched调度，调度任务
"""

import time, sched
import datetime
import threading

s = sched.scheduler(time.time, time.sleep)


def event_fun1():
    print("func1 Time:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def perform1(inc):
    s.enter(inc, 0, perform1, (inc,))
    event_fun1()


def event_fun2():
    print("func2 Time:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def perform2(inc):
    s.enter(inc, 0, perform2, (inc,))
    event_fun2()


def event_fun3():
    print("**func3 Time****:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def perform3(inc):
    s.enter(inc, 0, perform3, (inc,))
    event_fun3()


def run(func, inc=2):
    if func == "1":
        s.enter(0, 0, perform1, (10,))  # 每隔10秒执行一次perform1

    if func == "2":
        s.enter(0, 0, perform3, (15,))
        s.enter(0, 0, perform2, (10,))


if __name__ == '__main__':
    run('1')
    run('2')
    t = threading.Thread(target=s.run)
    t.start()
