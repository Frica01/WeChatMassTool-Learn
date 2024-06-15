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
        """绑定按钮点击事件"""
        # 获取控件信息
        self.view.btn_send_msg.clicked.connect(self.execute_on_click)
        # 绑定清空控件输入消息
        self.view.btn_clear_msg.clicked.connect(self.view.clear_widgets)
        self.view.btn_clear_file.clicked.connect(self.view.clear_widgets)
        self.view.btn_clear_name.clicked.connect(self.view.clear_widgets)
        self.view.btn_clear_all.clicked.connect(self.view.clear_widgets)

    def execute_on_click(self):
        """按钮点击事件处理函数"""
        import json
        data = self.view.get_input_info()
        print(json.dumps(data, indent=4))
