import unittest
from Unittest.demo.Calculator import Calculator

print(dir(unittest.TestCase))
class TestCaculator(unittest.TestCase):
    def testdemo01(self):
        cal = Calculator()
        result = cal.divide(10,2)
        self.assertEqual(result,4) #TODO 断言，如果不等则退出。注意 python2.7之后 用assertEquals替代assertEqual

    def testdemo02(self):
        cal = Calculator()
        result = cal.divide(20,0.5)
        self.assertEqual(result,40)

    def testdemo03(self): #TODO  ZeroDivisionError: division by zero
        cal = Calculator()
        result = cal.divide(20,0)
        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()  #调用unittest.main()方法可以方便的将测试类里的以“test”命名开头的测试方法以脚本的形式自动执行。