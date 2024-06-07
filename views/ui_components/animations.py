# -*- coding: utf-8 -*-
# Name:         animations.py
# Author:       小菜
# Date:         2024/6/7 上午7:52
# Description:


from PySide6.QtCore import (QEasingCurve, QPropertyAnimation)
from PySide6.QtWidgets import QWidget


def create_width_animation(widget: QWidget, target_width: int, duration=800):
    """在指定的持续时间内，将控件的宽度动画化到目标宽度。

    Args:
        widget(QWidget): 要动画化的QWidget对象。
        target_width(int): 动画化到的目标宽度，以像素为单位。
        duration(int): 动画持续时间，以毫秒为单位，默认值800

    Returns:
        返回配置好的动画对象(QPropertyAnimation)

    """
    animation = QPropertyAnimation(widget, b"minimumWidth")
    animation.setDuration(duration)
    animation.setStartValue(widget.width())
    animation.setEndValue(target_width)
    animation.setEasingCurve(QEasingCurve.InOutQuart)
    return animation
