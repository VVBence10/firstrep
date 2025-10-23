from random import randint

def get_random_number(x, y):
    return randint(x, y)

def print_number(x):
    for i in range(x):
        print(get_random_number(1, 100))

def main():
    print_number(5)
    
    
if __name__ == "__main__":
    main()

