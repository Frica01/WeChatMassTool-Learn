# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/6/2 下午7:23
# @Name   : main.py

import sys

from PySide6.QtWidgets import QApplication

from controllers import ControllerMain


def main():
    app = QApplication()
    controller = ControllerMain()
    controller.view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
