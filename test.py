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
		with self.assertRaises(ValueError):
			text_to_num('one thousand hundred')

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

	def test_thousands(self):
		self.assertEqual(text_to_num('one thousand'), 1000)
		self.assertEqual(text_to_num('two thousand'), 2000)
		self.assertEqual(text_to_num('three thousand'), 3000)
		self.assertEqual(text_to_num('four thousand'), 4000)
		self.assertEqual(text_to_num('five thousand'), 5000)
		self.assertEqual(text_to_num('six thousand'), 6000)
		self.assertEqual(text_to_num('seven thousand'), 7000)
		self.assertEqual(text_to_num('eight thousand'), 8000)
		self.assertEqual(text_to_num('nine thousand'), 9000)
		self.assertEqual(text_to_num('ten thousand'), 10000)
		self.assertEqual(text_to_num('eleven thousand'), 11000)
		self.assertEqual(text_to_num('twelve thousand'), 12000)
		self.assertEqual(text_to_num('thirteen thousand'), 13000)
		self.assertEqual(text_to_num('fourteen thousand'), 14000)
		self.assertEqual(text_to_num('fifteen thousand'), 15000)
		self.assertEqual(text_to_num('sixteen thousand'), 16000)
		self.assertEqual(text_to_num('seventeen thousand'), 17000)
		self.assertEqual(text_to_num('eighteen thousand'), 18000)
		self.assertEqual(text_to_num('nineteen thousand'), 19000)
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
				self.assertEqual(text_to_num(f'{tens} {ones} thousand'), (i * 10 + j) * 1000)

	def test_hundred_thousand(self):
		self.assertEqual(text_to_num('one hundred thousand'), 100000)
		self.assertEqual(text_to_num('five hundred thousand'), 500000)
		self.assertEqual(text_to_num('fifteen hundred thousand'), 1500000)

	def test_compound_thousands(self):
		self.assertEqual(text_to_num('one thousand three hundred fifty'), 1350)
		self.assertEqual(text_to_num('twenty five thousand eight hundred ninety three'), 25893)
		self.assertEqual(text_to_num('one hundred one thousand'), 101000);

	def test_millions(self):
		self.assertEqual(text_to_num('one million'), 1000000)
		self.assertEqual(text_to_num('two million'), 2000000)
		self.assertEqual(text_to_num('three million'), 3000000)
		self.assertEqual(text_to_num('four million'), 4000000)
		self.assertEqual(text_to_num('five million'), 5000000)
		self.assertEqual(text_to_num('six million'), 6000000)
		self.assertEqual(text_to_num('seven million'), 7000000)
		self.assertEqual(text_to_num('eight million'), 8000000)
		self.assertEqual(text_to_num('nine million'), 9000000)
		self.assertEqual(text_to_num('ten million'), 10000000)
		self.assertEqual(text_to_num('eleven million'), 11000000)
		self.assertEqual(text_to_num('twelve million'), 12000000)
		self.assertEqual(text_to_num('thirteen million'), 13000000)
		self.assertEqual(text_to_num('fourteen million'), 14000000)
		self.assertEqual(text_to_num('fifteen million'), 15000000)
		self.assertEqual(text_to_num('sixteen million'), 16000000)
		self.assertEqual(text_to_num('seventeen million'), 17000000)
		self.assertEqual(text_to_num('eighteen million'), 18000000)
		self.assertEqual(text_to_num('nineteen million'), 19000000)
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
				self.assertEqual(text_to_num(f'{tens} {ones} million'), (i * 10 + j) * 1000000)

	def test_compound_millions(self):
		self.assertEqual(text_to_num('one million five thousand three hundred one'), 1005301)
		self.assertEqual(text_to_num('ten million one'), 10000001)

	def test_and(self):
		self.assertEqual(text_to_num('one million and one hundred and one thousand and one hundred and one'), 1101101)

	def test_billions(self):
		self.assertEqual(text_to_num('one billion'), 1000000000)
		self.assertEqual(text_to_num('two billion'), 2000000000)
		self.assertEqual(text_to_num('three billion'), 3000000000)
		self.assertEqual(text_to_num('four billion'), 4000000000)
		self.assertEqual(text_to_num('five billion'), 5000000000)
		self.assertEqual(text_to_num('six billion'), 6000000000)
		self.assertEqual(text_to_num('seven billion'), 7000000000)
		self.assertEqual(text_to_num('eight billion'), 8000000000)
		self.assertEqual(text_to_num('nine billion'), 9000000000)
		self.assertEqual(text_to_num('ten billion'), 10000000000)
		self.assertEqual(text_to_num('eleven billion'), 11000000000)
		self.assertEqual(text_to_num('twelve billion'), 12000000000)
		self.assertEqual(text_to_num('thirteen billion'), 13000000000)
		self.assertEqual(text_to_num('fourteen billion'), 14000000000)
		self.assertEqual(text_to_num('fifteen billion'), 15000000000)
		self.assertEqual(text_to_num('sixteen billion'), 16000000000)
		self.assertEqual(text_to_num('seventeen billion'), 17000000000)
		self.assertEqual(text_to_num('eighteen billion'), 18000000000)
		self.assertEqual(text_to_num('nineteen billion'), 19000000000)
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
				self.assertEqual(text_to_num(f'{tens} {ones} billion'), (i * 10 + j) * 1000000000)

if __name__ == '__main__':
	unittest.main()
