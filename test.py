#!/usr/bin/env python3

import unittest

class TextToNumTest(unittest.TestCase):
	'''meant to test text_to_num function'''

	def test_exists(self):
		text_to_num('three')

if __name__ == '__main__':
	unittest.main()
