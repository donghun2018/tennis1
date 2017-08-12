# input_parser.py
# 08/12/17
# Takes an input and parses them into a dictionary form
from sys import argv

class entry():
	def __init__(self, input_array):
		self.name1 = input_array[0]
		self.name2 = input_array[1]
		self.school = input_array[2]
		self.level = input_array[3]
		self.seed = input_array[4]
	def __str__(self):
		return(','.join([self.name1, self.name2, self.school, self.level, self.seed]) + '\n')

class input_parser():

	def __init__(self):
		self.__entry_dict = {}

	def parse_input(self, file_loc):
		input_f = open(file_loc)
		for line in input_f.readlines():
			arr = line.strip().split(',')
			Z = entry(arr)
			if Z.school not in self.__entry_dict:
				self.__entry_dict[Z.school] = {}
			if Z.level not in self.__entry_dict[Z.school]:
				self.__entry_dict[Z.school][Z.level] = {}
			self.__entry_dict[Z.school][Z.level][Z.seed] = Z
		return(self.__entry_dict)

	def print_dict(self):
		# Simple routine for printing all entries
		for school in self.__entry_dict:
			print('School: ' + school + '\n')
			for level in self.__entry_dict[school]:
				print('Level: ' + level + '\n')
				for seed in self.__entry_dict[school][level]:
					print('Seed: ' + seed + '\n')
					print(self.__entry_dict[school][level][seed])

if __name__ == "__main__":
	# execute only if run as a script
	input_location = argv[1]
	parser = input_parser()
	parser.parse_input(input_location)
	parser.print_dict()
