
class BasePage:

    def __init__(self,driver):
        self.driver=driver

    # 打开页面
    def into_testin(self,url):
        self.driver.get(url)

    # 定位元素
    def locate_element(self,args):
        return self.driver.find_element(*args)

    #定位一组元素
    def locate_eles(self,args):
        return self.driver.find_elements(*args)

    #输入值
    def input_(self,args,text):
        self.locate_element(args).send_keys(text)

    #点击按钮
    def click_button(self,args):
        self.locate_element(args).click()


