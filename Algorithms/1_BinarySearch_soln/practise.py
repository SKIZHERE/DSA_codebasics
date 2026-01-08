from util import time_it

@time_it
def linear_search(elements, target):
    for i, element in enumerate(elements):
        if element == target:
            return i
    return -1

@time_it
def binary_search(elements, target):
    l_index = 0
    r_index = len(elements)-1
    m_index = 0

    while l_index <= r_index:
        m_index = (l_index + r_index)//2
        if elements[m_index] == target:
            return m_index

        if elements[m_index] < target:
            l_index = m_index+1
        else:
            r_index = m_index-1
    return -1

def binary_search_recursive(elements, target, l_index, r_index):
    if r_index<l_index:
        return -1

    m_index = (l_index+r_index)//2

    if m_index>= len(elements) or m_index<0:
        return -1

    if elements[m_index] == target:
        return m_index
    if elements[m_index] < target:
        l_index = m_index + 1
    else:
        r_index = m_index - 1
    return binary_search_recursive(elements,target,l_index,r_index)

if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 67
    numbers_list = range(10000001)
    number_to_find = 10000000

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")