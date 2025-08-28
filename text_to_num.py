#!/usr/bin/env python3

from enum import Enum

ones_table = {
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
	'ten': 10,
	'eleven': 11,
	'twelve': 12,
	'thirteen': 13,
	'fourteen': 14,
	'fifteen': 15,
	'sixteen': 16,
	'seventeen': 17,
	'eighteen': 18,
	'nineteen': 19,
}

tens_table = {
	'twenty': 20,
	'thirty': 30,
	'fourty': 40,
	'fifty': 50,
	'sixty': 60,
	'seventy': 70,
	'eighty': 80,
	'ninety': 90,
}


class State(Enum):
	START = 1
	ONES = 2
	TENS = 3

def text_to_num(text: str) -> int:
	'''
	:text: the number to be converted into an integer in plain english
		e.g. one hundred
		e.g. three thousand two hundred and fifty
		case does not matter
	:return: the number represented by the text
	'''
	result = 0
	state = State.START
	for word in text.lower().split():
		if state == State.START:
			if word in ones_table:
				result = ones_table[word]
				state = State.ONES
			elif word in tens_table:
				result = tens_table[word]
				state = State.TENS
		elif state == State.ONES:
			if word in ones_table or word in tens_table:
				raise ValueError('Malformed number')
		elif state == State.TENS:
			if word in ones_table:
				result += ones_table[word]
				state = State.ONES
			elif word in tens_table:
				raise ValueError('Malformed number')
	return result
