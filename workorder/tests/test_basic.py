from django.utils  import unittest

class TestBasic(unittest.TestCase):
  "Basic Tests"

  def test_basic(self):
    a = 1
    self.assertEqual(1,a)

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