def linear_search(elements, target):
    for i, element in enumerate(elements):
        if element == target:
            return i
    return -1

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

def all_occurances(elements,target):
    index = binary_search(elements, target)
    lst = [index]

    i = index -1
    while i>=0:
        if elements[i] == target:
            lst.append(i)
        else:
            break
        i = i-1

    i = index + 1
    while i < len(elements):
        if elements[i] == target:
            lst.append(i)
        else:
            break
        i = i + 1

    return sorted(lst)

if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 67
    if __name__ == '__main__':
        numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
        number_to_find = 15
        indices = all_occurances(numbers, number_to_find)
        print(f"Indices of occurances of {number_to_find} are {indices}")