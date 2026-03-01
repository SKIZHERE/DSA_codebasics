def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
                arr[j] = anchor
        gap -=1
    for i in range(size-1, 0, -1):
        if arr[i]==arr[i-1]:
            arr.pop(i)

if __name__ == "__main__":

    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    shell_sort(elements)
    print(elements)

