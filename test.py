#!/usr/bin/env python3

import unittest
from text_to_num import text_to_num

class TextToNumTest(unittest.TestCase):
	'''meant to test text_to_num function'''

	def test_exists(self):
		text_to_num('three')

if __name__ == '__main__':
	unittest.main()
