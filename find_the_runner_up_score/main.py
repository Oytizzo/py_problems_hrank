if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    set_of_arr = set(arr)
    list_of_arr = list(set_of_arr)
    list_of_arr.sort(reverse=True)
    print(list_of_arr[1])
