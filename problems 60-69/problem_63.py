#Powerful digit counts
#Problem 63

"""
The 5-digit number, 16807=75, is also a fifth power.
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def main():

    n = 0
    total = 0
    base = 1

    # Arbitrary limit
    while len(str(base)) < 100:
        n += 1
        base = int("1" + "0"*(n-1))
        starter = base**(1./n)
        if starter.is_integer():
            i = int(starter)
        else:
            i = int(starter) + 1

        while len(str(i**n)) == n:
            total += 1
            i += 1

    print "answer: " + str(total)



if __name__ == "__main__":
    main()
