# from platform import python_branch
import time

import pyautogui
import pyperclip

"""
清空（1961，650）
翻译（2039，652）
复制翻译结果（2168，653）
"""
# pyautogui.PAUSE = 2
# pyautogui.leftClick(2000, 500)# 输入之前点击
# pyautogui.leftClick(1961, 650)# 清空操作
# pyautogui.leftClick(2039, 652)# 翻译按钮
# pyautogui.leftClick(2168, 653)# 复制按钮


class YoudaoTranslate(object):
    def __int__(self):
        pass

    @staticmethod
    def youdao_none_click():
        pyautogui.leftClick(2000, 500)  # 输入之前点击

    @staticmethod
    def youdao_clear():
        pyautogui.leftClick(1961, 650)  # 清空操作

    @staticmethod
    def youdao_trans():
        pyautogui.leftClick(2039, 652)  # 翻译按钮

    @staticmethod
    def youdao_copy():
        pyautogui.leftClick(2168, 653)  # 复制按钮
        copy_text = pyperclip.paste()
        return copy_text

    @staticmethod
    def youdao_write_in(word):
        pyautogui.typewrite(str(word))

    def youdao_translate_word(self, word):
        self.youdao_clear()
        self.youdao_none_click()
        self.youdao_write_in(word)
        self.youdao_trans()
        time.sleep(2)
        test_text = self.youdao_copy()
        print(test_text)
        return test_text


# if __name__ == '__main__':
#     YoudaoTranslate().youdao_translate_word()
