# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/6/2 下午11:22
# @Name   : model_main.py

from typing import Callable
from PySide6.QtCore import QThreadPool

from models import (TaskRunnable, WechatTaskRunnable)


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

    def send_wechat_message(self, send_func: Callable, message_info: dict):
        """
        发送微信消息

        Args:
            send_func(Callable): 发送函数
            message_info(dict): 发送的消息内容
        """
        tasks = WechatTaskRunnable(func=send_func, message_info=self.process_message(message_info))
        self.threadpool.start(tasks)

    @staticmethod
    def process_message(message_info):
        """处理消息的逻辑"""
        # TODO 后续需进一步处理数据
        message_info.pop('add_remark_name')
        message_info.pop('at_everyone')

        # 合并发送文本
        msg_list = list()
        if signal_text := message_info.pop('single_text', None):
            msg_list.extend(signal_text.split('\n'))
        if multi_text := message_info.pop('multi_text', None):
            msg_list.append(multi_text)
        message_info['msgs'] = msg_list

        # 处理昵称
        message_info['names'] = message_info.get('names', list()).split()
        return message_info
