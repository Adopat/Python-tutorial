import unittest
from NameFunction import get_formatted_name


# 必须继承 unittest.TestCase类，才能进行单元测试
class NamesTestCase(unittest.TestCase):
    """测试NameFunction.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('james', 'hardon')
        self.assertEqual(formatted_name, 'James Hardon')

    def test_first_last_middle_name(self):
        """测试能否返回 middle 名字"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
