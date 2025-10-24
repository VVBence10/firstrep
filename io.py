from random import randint

def random_number(x):
    return str(randint(1, x))

def main():
    pwlength = int(input("Strength of your password: "))
    with open("pw.txt", "a") as f:
        for i in range(pwlength):
            f.write(
                random_number(100) + "la" 
                )

    with open("pw.txt", "r") as f:
        for line in f:
            print(line, end="")

if __name__ == "__main__":
    main()

""" 
just a test 2
"""

