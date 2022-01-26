#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parity(n):
    if isinstance(n, int):
        if n % 2:
            return f'{n} is odd'
        else:
            return f'{n} is even'
    else:
        return 'Invalid input.'
