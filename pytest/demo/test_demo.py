import pytest
from time import sleep
import threading
class TestDemo:
    def setup(self):
        print("ea1")
    def teardown(self):
        print("end")
    def setup_class(self): #TODO setup every class==开始类
        print("begin")
    def teardown_class(self): #结束类 after every class==每个类结束之后
        print("end")
    def test_01_hua1(self,pz):
        sleep(2)
        print("this is one ")
        assert 1 + 1 == 2

    def test_02_hua2(self):
        sleep(2)
        print('this is two')
        assert 1 + 1 == 3

    @pytest.mark.test
    def test_03_hua3(self):
        sleep(2)
        print("this is three")
        assert 1 + 1 == 2

    @pytest.mark.run(order=1)
    def test_04_hua4(self):
        sleep(2)
        print("this is four")
        assert 1 + 1 == 2


def fuc1():
    sleep(2)
    print(1)
def fuc2():
    sleep(2)
    print(2)

if __name__ == '__main__':
    pytest.main(['-vs'])
 #TODO -vs 显示详细信息 ; 启动多线程模式 加入参数-n=x 其中x是多线程的数量 也可以在命令行加入test_demo.py -n 2