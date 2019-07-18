

# 快速排序

#        [4,1,6,3,8,5,0,9,7,2]
#        [4,1,3,0,2]             [5]   [6,8,9,7]
#        [1,0,2]        [3] [4]  [5]   [6,7]    [8] [9]
#        [][0] [1,2]    [3] [4]  [5]   [6][7][] [8] [9]
#        [][0] [1][2][] [3] [4]  [5]   [6][7][] [8] [9]

# 快速排序
def quick_sort(mylist):
    # 判断临界值
    if len(mylist) <= 1:
        return mylist

    # 找基准数
    n = mylist.pop(len(mylist)//2)

    # 遍历，把小于基准数的元素放在左边列表，大于基准数的放在右边列表中
    left = []
    right = []
    for i in mylist:
        if i < n:
            left.append(i)
        else:
            right.append(i)
    # print(left, [n], right) # [4, 1, 3, 0, 2] [5] [6, 8, 9, 7]

    # 递归调用
    return quick_sort(left) + [n] + quick_sort(right)


list1 = [4,1,6,3,8,5,0,9,7,2]
print(quick_sort(list1))