import string

def is_hex(str):
	return all(char in string.hexdigits for char in str)

exports = []

with open("windows_exports.txt") as file:
	lines = file.readlines()

	for line in lines:
		items = line.split()
		
		if len(items) == 4 and is_hex(items[1]) and is_hex(items[2]):
			exports.append("LINK_ENTITY_TO_FUNC(" + items[3] + ");")

for item in sorted(set(exports)):
	print(item)