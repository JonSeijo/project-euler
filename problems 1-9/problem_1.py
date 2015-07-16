#Problem 1

"""
If we list all the natural numbers below 10 
that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of 
all the multiples of 3 or 5 below 1000.

"""

MAXNUM = 1000

def findMultiples(number):
    """Return a list with the multiples of the number,
        between 1 and MAXNUMBER"""

    multiples = []
    for n in range(1, MAXNUM):
        #If remainder is zero, is multiple
        if n % number == 0: 
            multiples.append(n)
        
    return multiples

def main():
    answer = 0

    multiples = findMultiples(3) + findMultiples(5)

    #Remove numbers multiples of both 3 and 5 using set
    multiples = set(multiples)

    #Sum all the multiples
    for n in multiples:
        answer += n

    print answer

if __name__ == "__main__":
    main()