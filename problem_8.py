# Largest product in a series
# Problem 8

"""
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product
"""

# File "problem_8_digits" has the digits of the proble 


def main():
    f = open("problem_8_digits", 'r')
    digits = f.read()
    f.close()

    # Remove the newline characters
    digits = digits.replace('\n', '')

    products = []
    digitsHolder = []

    for n in range(len(digits)-13):
        #Takes 13 chars of the string
        digitsHolder = digits[n:n+13]

        productTemp = 1
        # Funfact: if productTemp 0, it will always be 0
        # Realized the hard way

        #Multiply the 13 numbers and store the value
        for d in digitsHolder:
            productTemp *= int(d)

        products.append(productTemp)

    # All the products are stored, the max one is the answer
    answer = max(products)

    print answer


if __name__ == "__main__":
    main()
