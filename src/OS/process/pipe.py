#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Pipe, current_process


def pipe1(pipe):
    pipe.send(f'Hello, I am {current_process().name}.')
    print(pipe.recv())


def pipe2(pipe):
    print(pipe.recv())
    pipe.send(f'Hello, I am {current_process().name}.')
    pipe.close()


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    p_pipe1 = Process(target=pipe1, args=(conn1,))
    p_pipe2 = Process(target=pipe2, args=(conn2,))
    p_pipe1.start()
    p_pipe2.start()
    # p_pipe1.join()
    # p_pipe2.join()
