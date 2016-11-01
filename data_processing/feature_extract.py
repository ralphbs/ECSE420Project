import sys
import json
import time
import zlib

import argparse

DATA_FILE = '../log.txt'

def process_data(data):
	# Magic happens here
	pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = 'Compress the logged data.')
	parser.add_argument('-f', '--input', dest = 'input_file', default = DATA_FILE, help = 'Input data file')
	parser.add_argument('-l', '--limit', dest = 'limit', default = 500, help = 'Limit number of lines to process. 0 to process everything.', type = int)
	args = parser.parse_args()

	with open(args.input_file, 'r') as f:
		count = 0

		for line in f:
			count += 1
			new_data = json.loads(line)
			process_data(new_data)

			if count == args.limit and args.limit != 0:
				break
