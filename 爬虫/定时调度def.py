import time, sched
import datetime

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


def mymain(func, inc=2):
    if func == "1":
        s.enter(0, 0, perform1, (10,))  # 每隔10秒执行一次perform1
    if func == "2":
        s.enter(0, 0, perform2, (20,))  # 每隔20秒执行一次perform2


if __name__ == '__main__':
    mymain('1')
    mymain('2')
    s.run()
