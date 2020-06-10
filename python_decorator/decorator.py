#!/usr/bin/env python
# -*- coding: utf-8 -*-

def decorator_a(func):
    print('in the decorator_a')
    def wrapper_a(*args, **kwargs):
        print('in the wrapper_a')
        return func(*args, **kwargs)
    return wrapper_a

def decorator_b(func):
    print('in the decorator_b')
    def wrapper_b(*args, **kwargs):
        print('in the wrapper_b')
        return func(*args, **kwargs)
    return wrapper_b

@decorator_a
@decorator_b
def f():
    print('in the f()')
    return

f()
