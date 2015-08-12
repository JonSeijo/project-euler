# Sub-string divisibility
# Problem 43

"""
The number, 1406357289, is a 0 to 9 pandigital number because
it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


def main():
    print "Patience, this takes 4 minutes.. \n\n"

    # Start with the smallest 0-9 pandigital
    number = "0123456789"
    primes = [2, 3, 5, 7, 11, 13, 17]
    answer = 0

    # End with the biggest 0-9 pandigital
    while int(number) < 9876543210:
        number = str(number)

        # When converting to int, the 0 from the start dissapears,
        # If there are 9 digits, the starting 0 dissapeard, so add it
        if len(number) == 9:
            number = '0' + str(number)

        digitsFromRight = 0
        isPandigital = True

        # This goes through every digit of the number
        for i in range(0, 10):
            digit = number[i]

            # loop throgh every digit after number[i]
            for d in range(i+1, 10):

                # If digits are equal, it is NOT pandigital
                # Count how many digits are, counting from the right
                # Explanation at end
                if digit == number[d]:
                    isPandigital = False
                    digitsFromRight = 9 - d
                    break
            # Stop looping if not pandigital
            if not isPandigital:
                break

        if isPandigital:
            hasProperty = True
            for index in range(0, 7):
                # Takes three digits and see if is divisible by the prime
                # Then takes the next three digits ..
                if int(str(number)[index+1: index+4]) % primes[index] != 0:
                    hasProperty = False
                    break

            if hasProperty:
                print ".. " + str(number) + " .. "
                answer += int(number)

        # example
        # 51257893   is NOT pandigital, it repeats the 5
        # if I try the next number, number += 1
        # 51257894  is NOT pandigital, the problem is the 5
        # So I need to change the 5 to start being pandigital
        # Thats why I counted how many digits from right are in the digit
        # if I add 10000, it becomes 51267894, wich is pandigital

        number = int(number) + int('1' + '0' * digitsFromRight)

    print "\n" + "answer: " + str(answer)





if __name__ == "__main__":
    main()
