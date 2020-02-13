# -*- coding: utf-8 -*-
from util.opera_excel import OperaExcel

class GetData:
    def __init__(self):
        self.opera_excel = OperaExcel()

    def get_excel_lines(self):
        rows = self.opera_excel.get_total_rows()
        return rows

    def get_page_element(self,row):
        #获取页面元素
        page_element = self.opera_excel.get_value(row,3)
        return page_element

    def get_handle_step(self,row):
        #获取操作步骤
        handle_step = self.opera_excel.get_value(row,4)
        return handle_step

    def get_handle_value(self,row):
        #获取操作值
        handle_value = self.opera_excel.get_value(row,5)
        return handle_value

    def get_expected_results(self,row):
        #获取预期结果
        expected_results = self.opera_excel.get_value(row,6)
        return expected_results

    def get_actual_results(self,row):
        #获取实际结果
        actual_results = self.opera_excel.get_value(row,7)
        return actual_results

    def get_isrun(self,row):
        #获取是否执行该用例
        isrun = self.opera_excel.get_value(row,9)
        if isrun == None or isrun =='Y':
            return True
        else:
            return False

# if __name__ =="__main__":
#     getData = GetData()
#     getData.get_isrun(1)


