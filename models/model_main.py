# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/6/2 下午11:22
# @Name   : model_main.py

from typing import Callable
from PySide6.QtCore import QThreadPool

from models import TaskRunnable


class ModelMain:
    def __init__(self):
        self.threadpool = QThreadPool()

    def execute_tasks(self, func: Callable, *args, **kwargs):
        """
        创建并启动 TaskRunnable 任务

        Args:
            func(Callable): 要在并发任务中执行的函数。
            *args(tuple): 传递给任务函数的位置参数。
            **kwargs(dict): 传递给任务函数的关键字参数。

        Returns:
            None
        """
        task = TaskRunnable(func, *args, **kwargs)
        self.threadpool.start(task)
