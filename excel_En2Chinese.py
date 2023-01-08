import openpyxl
import tkinter as tk
from tkinter import filedialog
# from Youdao_translate import YoudaoTranslate as youdao_trans
import Youdao_translate


class ExcelTranslate(object):
    def __init__(self):
        pass

    @staticmethod
    def get_excel():
        main_excel = None
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if file_path:
            wb = openpyxl.load_workbook(file_path)
            main_excel = wb.active
        return main_excel

    @staticmethod
    def make_out_excel():
        # 新建一个表格
        out_excel = openpyxl.Workbook()
        # 选择活动工作表
        sheet = out_excel.active
        return out_excel, sheet

    def translate_en_to_chinese(self, trans_word):
        trans_result = Youdao_translate.YoudaoTranslate().youdao_translate_word(trans_word)
        return trans_result

    def get_translate_write_excel_value(self):
        in_excel = self.get_excel()
        source_excel_value = []
        trans_result_value = []
        for hang in range(2, 335):
            for lie in range(1, 3):
                cell = in_excel[hang][lie]
                source_excel_value.append(cell.value)

        out_excel, sheet = self.make_out_excel()

        i = 0
        for hang_out in range(2, 335):
            for lie_out in 'BC':
                cell_name = str(lie_out) + str(hang_out)
                cell = sheet[cell_name]
                trans_result = self.translate_en_to_chinese(source_excel_value[i])
                trans_result_value.append(trans_result)
                cell.value = trans_result_value[i]
                i += 1
        out_excel.save('NASA_Image_Mars_Translate.xlsx')


if __name__ == '__main__':
    ExcelTranslate().get_translate_write_excel_value()

"""测试模块-已跑通
        cell_name = 'B2'
        cell = sheet[cell_name]

        trans_excel_value = []
        trans_result = self.translate_en_to_chinese(source_excel_value[0])
        trans_excel_value.append(trans_result)
        cell.value = trans_excel_value[0]
"""