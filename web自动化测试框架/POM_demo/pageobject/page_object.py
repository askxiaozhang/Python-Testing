from web自动化测试框架.POM_demo.basepage.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
class LoginPage(BasePage):
    '''定位页面元素'''
    # url
    testin_url = 'https://www.testin.cn/account/login.htm'

    # 输入用户名和密码
    username_loc = (By.ID, 'email')
    password_loc = (By.ID, 'pwd')

    # 点击登录按钮
    login_button = (By.ID, "submitBtn")

    # 登录邮箱操作流程
    def testin_login(self, username='18170710339', password='Quyun1230'):
        self.into_testin(self.testin_url)
        sleep(2)
        self.locate_element(self.username_loc).send_keys(username)
        sleep(1)
        self.locate_element(self.password_loc).send_keys(password)
        sleep(1)
        self.click_button(self.login_button)

