# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:22
# @Name   : window_utils.py


import win32con
import win32gui


def minimize_wechat(class_name, name):
    """
    关闭Windows窗口

    Args:
        name(str):  进程名
        class_name(str):  进程class_name

    Returns:

    """
    hwnd = win32gui.FindWindow(class_name, name)
    if win32gui.IsWindowVisible(hwnd):
        win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)
