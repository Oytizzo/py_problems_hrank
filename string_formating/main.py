def print_formatted(number):
    # your code goes here
    length_of_number = len(format(number, 'b'))
    for i in range(number):
        print(format(i+1, 'd').rjust(length_of_number), format(i+1, 'o').rjust(length_of_number),
              format(i+1, 'X').rjust(length_of_number), format(i+1, 'b').rjust(length_of_number))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
