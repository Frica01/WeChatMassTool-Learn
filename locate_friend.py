import uiautomation as auto


def get_window(title_name=None, class_name=None):
    """
    获取窗口

    Args:
        title_name(str): 窗口标题
        class_name(str): 窗口类名称

    Returns:

    """
    window = auto.WindowControl(Name=title_name, ClassName=class_name)
    if window.Exists(maxSearchSeconds=0, searchIntervalSeconds=0):
        # 激活窗口，是窗口成为活动窗口
        window.SetActive()
        # 将窗口置顶(在最前面)
        window.SetTopmost(True)
        return window
    else:
        print("未能找到微信窗口")
        return None


def search_select_friend(nickname):
    """
    在微信窗口中搜索并选择好友

    Args:
        nickname(str): 好友昵称

    Returns:

    """
    if wechat_window := get_window(title_name='微信', class_name='WeChatMainWndForPC'):
        # 打开搜索框
        wechat_window.SendKeys('{Ctrl}F')

        # 清空搜索框的内容
        wechat_window.SendKeys('{Ctrl}A')
        wechat_window.SendKey('{Delete}')

        # 插入好友昵称
        # 使用剪切板，模拟复制+黏贴
        auto.SetClipboardText(text=nickname)
        wechat_window.SendKeys('{Ctrl}V')

        # 取全部搜索结果下的子节点
        search_nodes = wechat_window.ListControl(foundIndex=2).GetChildren()
        # 判断第一个选项的ControlType 是否为 PaneControl
        if isinstance(search_nodes.pop(0), auto.PaneControl):
            if search_nodes[0].Name == nickname:
                wechat_window.SendKey(key=auto.SpecialKeyNames['ENTER'])
                print('匹配成功')
            else:
                print('匹配失败')
        else:
            print('匹配失败')

    else:
        print("找不到微信窗口")


if __name__ == '__main__':
    search_select_friend('文件传输助手')
