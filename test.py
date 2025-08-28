#!/usr/bin/env python3

import unittest
from text_to_num import text_to_num

class TextToNumTest(unittest.TestCase):
	'''meant to test text_to_num function'''

	def test_exists(self):
		text_to_num('three')

	def test_single_digit(self):
		for i, word in enumerate((
			'zero',
			'one',
			'two',
			'three',
			'four',
			'five',
			'six',
			'seven',
			'eight',
			'nine',
		)):
			self.assertEqual(text_to_num(word), i)

	def test_caps(self):
		self.assertEqual(text_to_num('THREE'), 3)

if __name__ == '__main__':
	unittest.main()
