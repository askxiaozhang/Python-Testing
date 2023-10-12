# Python-Testing
The learning stage from testing novices to testing masters.

## Unittest
unittest.main()会运行继承自unittest.TestCase类中的以'test'命名开头的方法
例如：
    class TestDemo(unittest.TestCase):
        def test01(self):
            pass #就会自动运行此方法
可以结合 self.assertEqual(x,y) 判断x和y是否相等，或者报错会返回异常，用于快速找到测试中的问题