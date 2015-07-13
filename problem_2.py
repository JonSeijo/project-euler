#Problem 2
#Even Fibonacci numbers

""" By considering the terms in 
the Fibonacci sequence whose values 
do not exceed four million, 
find the sum of the even-valued terms. """

MAX_NUMBER = 4000000

def getFibonac(maxnumber):
	"""Returns a list with the Fibonacci numbers
	smaller than  'maxnumber'
	"""
	i = 1
	sequence = [1, 2]
	reached_max = False

	while(not reached_max):
		#Number will be current index plus 
		next_fib = sequence[i] + sequence[i-1]

		#Stop adding if the next fibbonacci number is greater than the max
		if next_fib >= maxnumber: 
			reached_max = True;
		else:
			sequence.append(next_fib)

		i += 1

	return sequence

def getEvenNumbers(number_list):
	"""Takes a list of numbers and 
	returns a list with the even"""

	even_numbers = []
	for n in number_list:
		if n % 2 == 0:
			even_numbers.append(n)

	return even_numbers


def main():
	sum_of_evens = 0
	for n in getEvenNumbers(getFibonac(MAX_NUMBER)):
		sum_of_evens += n

	print sum_of_evens


if __name__ == "__main__":
    main()