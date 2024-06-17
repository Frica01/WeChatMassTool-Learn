# -*- coding: utf-8 -*-
# Name:         tasks.py
# Author:       小菜
# Date:         2024/6/14 上午7:32
# Description:


from PySide6.QtCore import QRunnable


class TaskRunnable(QRunnable):
    def __init__(self, func, *args, **kwargs):
        """初始化任务对象"""
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """执行任务"""
        self.func(*self.args, **self.kwargs)


class WechatTaskRunnable(TaskRunnable):
    def __init__(self, func, *args, **kwargs):
        super().__init__(func, *args, **kwargs)

    def run(self):
        """重写run方法，处理消息发送任务"""
        message_info: dict = self.kwargs.get('message_info')
        for idx, name in enumerate(message_info.pop('names', list())):
            self.func(name, **message_info)
