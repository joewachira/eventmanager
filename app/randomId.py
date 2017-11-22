__author__ = 'joe'

import random

# method generated random integer to be used as event ID


def get_random_id():
	random_id = random.randrange(1, 100000)
	return random_id