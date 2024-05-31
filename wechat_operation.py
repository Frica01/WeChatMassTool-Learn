import time
from typing import Iterable

import uiautomation as auto


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

    def __send_file(self):
        """下篇文章的内容"""

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

    def send_messages(self, name, msgs):
        """
        发送消息
        
        Args:
            name(str):
            msgs(Iterable[str]):
        """

        if not self.goto_chat_box(name):
            raise NameError('昵称不匹配')

        # 设置输入框为当前焦点
        self.input_edit = self.wechat_window.EditControl(Name=name)
        self.input_edit.SetFocus()

        self.__send_text(*msgs)


if __name__ == '__main__':
    wx = WeChatOperation()
    wx.send_messages(
        name='文件传输助手',
        msgs=['嗨', '今天天气不错！', '我们出去玩吧']
    )
