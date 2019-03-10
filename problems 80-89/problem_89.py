# Problem 89
# Roman numerals

values = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}

romanos = [ 
	(1000, 'M'),
	(900, 'CM'),
	(500, 'D'),
	(400, 'CD'),
	(100, 'C'),
	(90, 'XC'),
	(50, 'L'),
	(40, 'XL'),
	(10, 'X'),
	(9, 'IX'),
	(5, 'V'),
	(4, 'IV'),
	(1, 'I')	
]

def decimal(romano):
	num = 0
	i = 0
	while i < len(romano):

		# Si estoy sustrayendo
		if i < len(romano)-1 and values[ romano[i] ] < values[ romano[i+1] ]:
			num +=  values[ romano[i+1] ] - values[ romano[i] ]
			i += 2
		else:
			num += values[ romano[i] ]
			i += 1

	return num


def romano_optimo(dec):
	rom = ""

	i = 0
	while i < len(romanos):
		if dec - romanos[i][0] >= 0:
			dec -= romanos[i][0]
			rom += romanos[i][1]
		else:
			i += 1

	return rom


def solve(orig):
	optimo = romano_optimo(decimal(orig))
	return len(orig) - len(optimo)

if __name__ == '__main__':

	cuenta = 0
	with open('problem_89.txt') as f:
		for line in f:
			cuenta += solve(line[:-1]) # Asumo que ultimo caracter es '\n'

	print(cuenta)