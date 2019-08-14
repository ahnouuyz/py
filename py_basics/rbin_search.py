def rbin_search(a_list, target, i0=0):
    'Assume a_list is sorted.'
    print(a_list)
    if a_list:
        midx = len(a_list) // 2
        if a_list[midx] == target:
            return midx + i0
        elif a_list[midx] > target:
            return rbin_search(a_list[:midx], target, i0=i0)
        elif a_list[midx] < target:
            return rbin_search(a_list[midx:], target, i0=i0 + midx)

def main():
    lst = [1, 3, 4, 5, 7, 10, 11]
    for i in lst:
        print(rbin_search(lst, i))

if __name__ == '__main__':
    main()
