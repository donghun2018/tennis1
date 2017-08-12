# input_parser.py
# 08/12/17
# Takes an input and parses them into a dictionary form

from sys import argv

input_location = argv[1]
input_f = open(input_location)
entry_dict = {}

class entry():
	def __init__(self, input_array):
		self.name1 = input_array[0]
		self.name2 = input_array[1]
		self.school = input_array[2]
		self.level = input_array[3]
		self.seed = input_array[4]

for line in input_f.readlines():
	arr = line.strip().split(',')
	Z = entry(arr)
	if Z.school not in entry_dict:
		entry_dict[Z.school] = {}
	entry_dict[Z.school][Z.seed] = Z

print(entry_dict)