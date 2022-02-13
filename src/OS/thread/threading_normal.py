#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def run(delay, **kwargs):
    thread_name = threading.current_thread().name
    thread_id = threading.current_thread().ident
    print(f'Thread {thread_name} started, ID: {thread_id}, Priority: {kwargs["priority"]}, will sleep for {delay}s.')
    time.sleep(delay)
    print(f'Thread {thread_name} exited')


if __name__ == '__main__':
    print(f'{threading.main_thread().name} started, ID: {threading.main_thread().ident}')
    start_time = time.time()
    thread1 = threading.Thread(target=run, name='T1', args=(2,), kwargs={'priority': 'lower'})
    thread2 = threading.Thread(target=run, name='T2', args=(1,), kwargs={'priority': 'higher'})
    thread1.start()
    thread2.start()
    thread2.name = 'T22'
    print(f'\n{threading.active_count()} active threads: {threading.enumerate()}')
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(f'All threads take {end_time - start_time}s')
    print(f'{threading.main_thread().name} exited')
