# -*- coding: utf-8 -*-
from keywords.getdata import GetData
from keywords.action_method import ActionMethod

class RunMain:
    def main_action(self):
        getdata = GetData()
        action_method = ActionMethod()
        for i in len(getdata.get_excel_lines()):
            page_element = getdata.get_page_element()
            handle_step = getdata.get_handle_step()
            handle_value = getdata.get_handle_value()
            action = getattr(action_method,handle_step)
            action(page_element,handle_value)
