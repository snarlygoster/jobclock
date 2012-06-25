from django.utils    import unittest

from workorder.models import

class TestBasic(unittest.TestCase):
    "Basic Tests"

    def test_selecting_product_creates_workorder(self):
     pass



    def  test_basic_2(self):
        a = 1
        assert a == 1

    def test_fail(self):
        "this test should fail"
        a = 1
        assert a == 2

class TestForm(unittest.TestCase):
    def test_two(self):
        b = 1
        assert b == 2