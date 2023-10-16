import pytest
from time import sleep
from selenium import webdriver
from common.excel import read_excel
from pageobject.page_object import LoginPage
from .pageobject.page_object import SelectPage

class TestTestIn:

    #打开浏览器
    def setup(self) -> None:
        self.driver=webdriver.Chrome()
        driver=self.driver

    def teardown(self) -> None:
        sleep(1)
        self.driver.close()

    '''利用excel导入登录测试数据'''
    @pytest.mark.parametrize('case',read_excel('./data/data.xlsx','login'))
    def test_01_login(self,case):
        '''测试登录模块'''
        xh,case_name,username,password,is_exc,result,bz=case
        lp=LoginPage(self.driver)
        lp.testin_login(username,password)

    def test_02_select_iphone_12(self):
        '''测试根据品牌选择手机'''
        lp = LoginPage(self.driver)
        lp.testin_login()
        ps=SelectPage(self.driver)
        ps.testin_select_01_iphone()


    def test_03_select_androi_sys(self):
        '''测试根据安卓系统选择手机'''
        lp = LoginPage(self.driver)
        lp.testin_login()
        ps=SelectPage(self.driver)
        ps.testin_select_02_android()

    def test_04_select_online_time(self):
        '''测试根据上市时间来选择手机'''
        lp = LoginPage(self.driver)
        lp.testin_login()
        ps=SelectPage(self.driver)
        ps.testin_select_03_onlin_time()

