#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading


def run():
    semaphore.acquire()
    print(f'{threading.current_thread().name} is running at {time.ctime()}.')
    time.sleep(1)
    semaphore.release()


semaphore = threading.BoundedSemaphore(2)
for i in range(6):
    threading.Thread(target=run).start()

print(f'Active count: {threading.active_count()-1}')    # 所有线程启动后均为活动状态
