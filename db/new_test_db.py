



import csv

from collections import namedtuple

class PickUp(dict):
	cnt=1
	print(cnt)
	


def load_map(filename):
	with open(filename) as f:
		cnt = 0
		for reader in csv.reader(f):
			print(reader)
			cnt += 1
			if cnt == 3:
				break



if __name__ == '__main__':
	load_map('israel.csv')

