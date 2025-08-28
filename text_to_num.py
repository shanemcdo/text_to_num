#!/usr/bin/env python3

text_num_table = {
	'zero': 0,
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9,
}

def text_to_num(text: str) -> int:
	'''
	:text: the number to be converted into an integer in plain english
		e.g. one hundred
		e.g. three thousand two hundred and fifty
		case does not matter
	:return: the number represented by the text
	'''
	text = text.lower()
	return text_num_table[text]
