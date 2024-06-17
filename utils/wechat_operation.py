# -*- coding: utf-8 -*-
# Name:         wechat_operation.py
# Author:       小菜
# Date:         2024/6/17 上午7:09
# Description:


import time

import uiautomation as auto

from utils import copy_files_to_clipboard


class WeChatOperation:
    def __init__(self):
        # 微信窗口
        self.wechat_window = auto.WindowControl(Name='微信', ClassName='WeChatMainWndForPC')
        # 输入框（这个窗口是默认的）
        self.input_edit = self.wechat_window.EditControl()

    def __send_text(self, *msgs):
        """
            发送文本.

        Args:
            *msgs(str): 必选参数，为发送的文本
        """

        for msg in msgs:
            assert msg, "发送的文本内容为空"
            # 删除聊天框原有的内容, waitTime 的意思是完成这个操作的总时长
            self.input_edit.SendKeys(text='{Ctrl}A', waitTime=0.05)
            self.input_edit.SendKey(key=auto.SpecialKeyNames['DELETE'], waitTime=0.05)

            # 设置到剪切板
            auto.SetClipboardText(text=msg)
            time.sleep(0.05)

            # 黏贴到输入框
            self.input_edit.SendKeys(text='{Ctrl}V', waitTime=0.05)

            # 模拟按下Enter 回车键，进行发送
            self.wechat_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.05)

    def __send_file(self, *file_paths):
        """
        	发送文件.

        Args:
            *file_paths(str): 必选参数，为文件的路径
        """
        # 复制文件到剪切板
        copy_files_to_clipboard(file_paths=file_paths)
        # 粘贴
        self.input_edit.SendKeys(text='{Ctrl}V', waitTime=0.1)
        # 按下回车键
        self.wechat_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.1)
        # 等待发送动作完成
        time.sleep(0.1)

    def goto_chat_box(self, nickname):
        """
        跳转到指定 name好友的聊天窗口。

        Args:
            nickname(str): 必选参数，好友名称
        """
        # 清空搜索框
        self.wechat_window.SendKeys(text='{Ctrl}F', waitTime=0.05)
        self.wechat_window.SendKeys(text='{Ctrl}A', waitTime=0.05)
        self.wechat_window.SendKey(key=auto.SpecialKeyNames['DELETE'], waitTime=0.05)

        # 复制昵称到剪切板，然后Ctrl+V
        auto.SetClipboardText(text=nickname)
        time.sleep(0.5)
        self.wechat_window.SendKeys(text='{Ctrl}V', waitTime=0.05)

        # 若有匹配结果，第一个元素的类型为PaneControl
        search_nodes = self.wechat_window.ListControl(foundIndex=2).GetChildren()
        if not isinstance(search_nodes.pop(0), auto.PaneControl):
            self.wechat_window.SendKeys(text='{Esc}', waitTime=0.05)
            raise ValueError("昵称不匹配")

        # 只考虑全匹配, 不考虑好友昵称重名, 不考虑好友昵称与群聊重名
        if search_nodes[0].Name == nickname:
            self.wechat_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.05)
            time.sleep(0.5)
            return True
        # 无匹配用户, 取消搜索框
        self.wechat_window.SendKeys(text='{Esc}', waitTime=0.05)
        return False

    def send_messages(self, name, msgs=None, file_paths=None):
        """
        发送消息

        Args:
            name(str):必选参数，接收消息的好友名称
            msgs(Iterable[str], Optional): 可选参数，发送的文本消息
            file_paths(Iterable[str], Optional):可选参数，发送的文件路径
        """
        # 发送文本和文件不能同时为空
        if not any([msgs, file_paths]):
            raise ValueError("发送的消息和文件不可同时为空")

        if not self.goto_chat_box(name):
            raise NameError('昵称不匹配')

        # 设置输入框为当前焦点
        self.input_edit = self.wechat_window.EditControl(Name=name)
        self.input_edit.SetFocus()

        # 发送文本
        if msgs:
            self.__send_text(*msgs)
        # 发送文件
        if file_paths:
            self.__send_file(*file_paths)


if __name__ == '__main__':
    wx = WeChatOperation()
    wx.send_messages(
        name='文件传输助手',
        msgs=['嗨', '今天天气不错！', '我们出去玩吧'],
        file_paths=[r'F:\测试1.txt', r'F:\测试2.txt']
    )
