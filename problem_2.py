#Problem 2
#Even Fibonacci numbers

""" By considering the terms in 
the Fibonacci sequence whose values 
do not exceed four million, 
find the sum of the even-valued terms. """

def fibonac(maxnumber):
	"""Returns a list with the Fibonacci numbers
	smaller than  'maxnumber'
	"""
	i = 1
	sequence = [1, 2]
	reached_max = False

	while(not reached_max):
		next_fib= sequence[i] + sequence[i-1]

		if next_fib >= maxnumber: 
			reached_max = True;
		else:
			sequence.append(next_fib)

		i += 1

	return sequence

def main():
	print fibonac(20)

if __name__ == "__main__":
    main()