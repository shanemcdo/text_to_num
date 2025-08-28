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

multiplier_table = {
	'hundred': 100,
	'thousand': 1000,
	'million': 1000000,
}


class State(Enum):
	START = 1
	ONES = 2
	TENS = 3
	MULT = 4

def text_to_num(text: str) -> int:
	'''
	:text: the number to be converted into an integer in plain english
		e.g. one hundred
		e.g. three thousand two hundred and fifty
		case does not matter
	:return: the number represented by the text
	'''
	sub_result = 0
	result = 0
	state = State.START
	prev_mult = None
	for word in text.lower().split():
		if state == State.START:
			if word in ones_table:
				sub_result = ones_table[word]
				state = State.ONES
			elif word in tens_table:
				sub_result = tens_table[word]
				state = State.TENS
			else:
				raise ValueError('unexpected word')
		elif state == State.ONES:
			if word in ones_table or word in tens_table:
				raise ValueError('Malformed number: a ones or tens places cannot follow a ones places')
			elif word in multiplier_table:
				prev_mult = multiplier_table[word]
				sub_result *= prev_mult
				state = State.MULT
				result += sub_result
				sub_result = 0
			else:
				raise ValueError('unexpected word')
		elif state == State.TENS:
			if word in ones_table:
				sub_result += ones_table[word]
				state = State.ONES
			elif word in tens_table:
				raise ValueError('Malformed number: a tens place (twenty) cannot follow another tens place')
			elif word in multiplier_table:
				prev_mult = multiplier_table[word]
				sub_result *= prev_mult
				state = State.MULT
				result += sub_result
				sub_result = 0
			else:
				raise ValueError('unexpected word')
		elif state == State.MULT:
			if word in ones_table:
				sub_result += ones_table[word]
				state = State.ONES
			elif word in tens_table:
				sub_result += tens_table[word]
				state = State.TENS
			elif word in multiplier_table:
				mult = multiplier_table[word]
				if prev_mult > mult:
					raise ValueError('Malformed number: multipliers (e.g.) hundred cannot be bigger than the previous mulitplier')
				prev_mult = mult
				result *= prev_mult
			else:
				raise ValueError('unexpected word')
		else:
			raise ValueError('unexpected state')
	result += sub_result
	return result
