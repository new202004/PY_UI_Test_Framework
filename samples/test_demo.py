import unittest


class Tasta(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:   # 类级别的
        print('class')
    @classmethod
    def tearDownClass(cls) -> None:
        print('t-class')

    def setUp(self) -> None:  # 方法级别的
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test_01(self):
        print('1')
        self.assertTrue(True)

    def test_02(self):
        print('2')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()