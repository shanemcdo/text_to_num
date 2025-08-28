#!/usr/bin/env python3

import unittest
from text_to_num import text_to_num

class TextToNumTest(unittest.TestCase):
	'''meant to test text_to_num function'''

	def test_exists(self):
		text_to_num('three')

	def test_lte_20(self):
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
			'ten',
			'eleven',
			'twelve',
			'thirteen',
			'fourteen',
			'fifteen',
			'sixteen',
			'seventeen',
			'eighteen',
			'nineteen',
			'twenty',
		)):
			self.assertEqual(text_to_num(word), i)

	def test_caps(self):
		self.assertEqual(text_to_num('THREE'), 3)

	def test_by_10(self):
		self.assertEqual(text_to_num('ten'), 10)
		self.assertEqual(text_to_num('twenty'), 20)
		self.assertEqual(text_to_num('thirty'), 30)
		self.assertEqual(text_to_num('fourty'), 40)
		self.assertEqual(text_to_num('fifty'), 50)
		self.assertEqual(text_to_num('sixty'), 60)
		self.assertEqual(text_to_num('seventy'), 70)
		self.assertEqual(text_to_num('eighty'), 80)
		self.assertEqual(text_to_num('ninety'), 90)

	def test_21to99(self):
		for i, tens in enumerate((
			'twenty',
			'thirty',
			'fourty',
			'fifty',
			'sixty',
			'seventy',
			'eighty',
			'ninety',
		), 2):
			for j, ones in enumerate((
				'one',
				'two',
				'three',
				'four',
				'five',
				'six',
				'seven',
				'eight',
				'nine',
			), 1):
				self.assertEqual(text_to_num(f'{tens} {ones}'), i * 10 + j)

	def test_malformed(self):
		# TODO: consider making these allowed
		with self.assertRaises(ValueError):
			text_to_num('one one')
		with self.assertRaises(ValueError):
			text_to_num('one ninety')
		with self.assertRaises(ValueError):
			text_to_num('nine twenty')
		with self.assertRaises(ValueError):
			text_to_num('twenty twenty')

	def test_hundreds(self):
		self.assertEqual(text_to_num('one hundred'), 100)
		self.assertEqual(text_to_num('two hundred'), 200)
		self.assertEqual(text_to_num('three hundred'), 300)
		self.assertEqual(text_to_num('four hundred'), 400)
		self.assertEqual(text_to_num('five hundred'), 500)
		self.assertEqual(text_to_num('six hundred'), 600)
		self.assertEqual(text_to_num('seven hundred'), 700)
		self.assertEqual(text_to_num('eight hundred'), 800)
		self.assertEqual(text_to_num('nine hundred'), 900)
		self.assertEqual(text_to_num('ten hundred'), 1000)
		self.assertEqual(text_to_num('eleven hundred'), 1100)
		self.assertEqual(text_to_num('twelve hundred'), 1200)
		self.assertEqual(text_to_num('thirteen hundred'), 1300)
		self.assertEqual(text_to_num('fourteen hundred'), 1400)
		self.assertEqual(text_to_num('fifteen hundred'), 1500)
		self.assertEqual(text_to_num('sixteen hundred'), 1600)
		self.assertEqual(text_to_num('seventeen hundred'), 1700)
		self.assertEqual(text_to_num('eighteen hundred'), 1800)
		self.assertEqual(text_to_num('nineteen hundred'), 1900)
		for i, tens in enumerate((
			'twenty',
			'thirty',
			'fourty',
			'fifty',
			'sixty',
			'seventy',
			'eighty',
			'ninety',
		), 2):
			for j, ones in enumerate((
				'one',
				'two',
				'three',
				'four',
				'five',
				'six',
				'seven',
				'eight',
				'nine',
			), 1):
				self.assertEqual(text_to_num(f'{tens} {ones} hundred'), (i * 10 + j) * 100)

if __name__ == '__main__':
	unittest.main()
