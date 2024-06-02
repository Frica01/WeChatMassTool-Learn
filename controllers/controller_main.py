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

