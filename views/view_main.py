# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/6/2 下午11:25
# @Name   : view_main.py


from PySide6.QtWidgets import QMainWindow

from views.ui_designs import Ui_MainWindow


class ViewMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
