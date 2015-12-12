# Problem 59
# XOR decryption

"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher
text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using problem_59_cipher.txt
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text

"""


def applyXor(message, key):
    dexored = []
    i = 0
    dexored = []

    for c in message:
        dexored.append(key[i] ^ c)
        i += 1
        if i == 3:
            i = 0

    return dexored


def decript(dexored):
    # Get the char from the ascii for each element
    return "".join(map(chr,dexored))


def main():

    with open("problem_59_cipher.txt") as f:
        messageStr = f.read().split(',')

    message = []
    for s in messageStr:
        message.append(int(s))

    key = [ord('a'), ord('a'), ord('a')]

    for i in range(ord('a'), ord('z')+1):
        for j in range(ord('a'), ord('z')+1):
            for k in range(ord('a'), ord('z')+1):

                key = [i, j, k]

                ascii_message = applyXor(message, key)
                decripted_message = decript(ascii_message)

                # Trial and error
                if ("the" in decripted_message)and("and" in decripted_message) and("is" in decripted_message)and("when" in decripted_message):

                    print decripted_message

                    print "Answer: " + str(sum(ascii_message))


if __name__ == "__main__":
    main()
