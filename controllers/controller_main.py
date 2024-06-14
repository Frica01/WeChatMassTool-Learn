# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/6/2 下午11:43
# @Name   : controller_main.py

from models import ModelMain
from views import ViewMain


class ControllerMain:
    def __init__(self):
        self.view = ViewMain()
        self.model = ModelMain()
        self.setup_connections()

    def setup_connections(self):
        self.view.btn_send_msg.clicked.connect(self.execute_on_click)

    def sample_task(self, cnt):
        """简单打印任务"""
        print(cnt)

    def execute_on_click(self):
        """按钮点击事件处理函数"""
        for i in range(10):
            self.model.execute_tasks(self.sample_task, i)

