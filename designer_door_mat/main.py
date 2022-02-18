# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    c = '.|.'
    message = 'WELCOME'
    for i in range(a):
        if i < int(a/2):
            print((c * i).rjust(b//2-1, '-') + c + (c * i).ljust(b//2-1, '-'))
        elif i == int(a/2):
            print(message.center(b, '-'))
        elif i > int(a/2):
            print((c * (a-1-i)).rjust(b//2-1, '-') + c + (c * (a-1-i)).ljust(b//2-1, '-'))
