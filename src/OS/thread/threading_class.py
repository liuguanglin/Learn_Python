#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, args, kwargs):
        super().__init__()
        # super(MyThread, self).__init__()
        self.delay = args[0]
        self.dict = kwargs
        self.name = name

    def run(self):
        print(
            f'Thread {self.name} started, ID: {self.ident}, Priority: {self.dict["priority"]},'
            f'will sleep for {self.delay}s.')
        time.sleep(self.delay)
        print(f'Thread {self.name} exited')


start_time = time.time()

t1 = MyThread(name='T1', args=(2,), kwargs={'priority': 'lower'})
t2 = MyThread(name='T2', args=(1,), kwargs={'priority': 'higher'})
t1.start()
t2.start()
t2.name = 'T22'
print(f'\n{threading.active_count()} active threads: {threading.enumerate()}')
t1.join()  # 将主线程阻塞，直到该线程结束或超时
t2.join()
end_time = time.time()
print(f'All threads take {end_time - start_time}s')
print(f'{threading.main_thread().name} exited')
