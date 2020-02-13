from util.read_init import ReadIni


'''
  对获取到的配置文件信息，进行处理
'''
class GetByLocal():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        local = ReadIni().get_value(key) #例如id>cn.com.open.mooc:id/account_edit
        if local!=None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'className':
                return self.driver.find_elements_by_class_name(local_by)
            elif by == 'xpath':
                return self.driver.find_element_xpath(local_by)
            else:
                return self.driver.find_element_by_android_uiautomator(local_by)
        else:
            raise RuntimeError("cuowu")


#
# if __name__ == '__main__':
#     get_by_local = GetByLocal()
#     get_by_local.get_element('username1')