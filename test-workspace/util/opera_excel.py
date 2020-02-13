# -*- coding: utf-8 -*-

import xlrd

class OperaExcel:
    def __init__(self,file_path=None,n=None):
        if file_path==None:
            self.file_path = '../config/case.xlsx'
        else:
            self.file_path = file_path
        self.excel = self.get_excel()
        if n==None:
            self.get_sheet = self.get_sheets(0)
        else:
            self.get_sheet = self.get_sheets(n)


    def get_excel(self):
        '''
            根据路径找到excel，读取内容
        '''
        excel_data = xlrd.open_workbook(self.file_path)
        return excel_data

    def get_sheets(self,n):
        '''
        根据sheet下标 找到对应sheet【n】的内容
        获取sheet内容方法2：self.excel.sheets()[n]
        :param n:
        :return:
        '''
        sheet = self.excel.sheet_by_index(n)
        return sheet

    def get_total_rows(self):
        total_rows = self.get_sheet.nrows
        return total_rows

    def get_value(self,row,col):
        value = self.get_sheet.cell_value(row,col)
        if value == '':
            print('None')
            return None
        print(value)
        return value


# excel = OperaExcel()
# excel.get_value(1,1)




