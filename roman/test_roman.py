import unittest
from unittest import TestCase
from roman_rec import roman_rec as ROMAN

class PulbicTestSuite(TestCase):
    def test_zero_error(self):
        with self.assertRaises(AssertionError):
            ROMAN(0)
    
    def test_non_int(self):
        with self.assertRaises(AssertionError):
            ROMAN(1.)
    
    def test_5(self):
        expected = "V"
        self.assertEqual(ROMAN(5),expected)
    
    def test_8(self):
        expected = "VIII"
        self.assertEqual(ROMAN(8),expected)
    
    def test_44(self):
        expected = "XLIV"
        self.assertEqual(ROMAN(44),expected)
    
    def test_99(self):
        expected = "XCIX"
        self.assertEqual(ROMAN(99),expected)
    
    def test_4444(self):
        expected = "MMMMCDXLIV"
        self.assertEqual(ROMAN(4444),expected)
    