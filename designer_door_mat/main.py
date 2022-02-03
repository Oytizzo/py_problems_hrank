# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a, b = input().split(" ")
    for i in range(int(a)):
        for j in range(int(b)):
            print("-", end="")
        print("\n")
