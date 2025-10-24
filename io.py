with open("iotest.txt", "a") as f:
    f.write("dikazgeci\n")

with open("iotest.txt", "r") as f:
    for line in f:
        print(line, end="")
    print(f.tell())

