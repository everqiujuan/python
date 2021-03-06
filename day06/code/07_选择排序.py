

# 选择排序
#
#           [8,9,5,6,7,4,3,2,1]  # 升序
#   第1趟 i=0  [1, 9,8,6,7,5,4,3,2]
#   第2趟 i=1  [1,2, 9,8,7,6,5,4,3]
#   第3趟 i=2  [1,2,3, 9,8,7,6,5,4]
#   第4趟 i=3  [1,2,3,4, 9,8,7,6,5]
#   第5趟 i=4  [1,2,3,4,5, 9,8,7,6]
#   第6趟 i=5  [1,2,3,4,5,6, 9,8,7]
#   第7趟 i=6  [1,2,3,4,5,6,7, 9,8]
#   第8趟 i=7  [1,2,3,4,5,6,7,8, 9]
#

list1 = [8,9,5,6,7,4,3,2,1]

for i in range(len(list1)-1):  # 趟数
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1)


#             [8,9,5,6,7,4,3,2,1]  升序
#  第1趟 i=0   =>  [1, 9,5,6,7,4,3,2,8]
#  第2趟 i=1   =>  [1,2, 5,6,7,4,3,9,8]
#  第3趟 i=2   =>  [1,2,3, 6,7,4,5,9,8]
#  第4趟 i=3   =>  [1,2,3,4, 7,6,5,9,8]
#  第5趟 i=4   =>  [1,2,3,4,5, 6,7,9,8]
#  第6趟 i=5   =>  [1,2,3,4,5,6, 7,9,8]
#  第7趟 i=6   =>  [1,2,3,4,5,6,7, 9,8]
#  第8趟 i=7   =>  [1,2,3,4,5,6,7,8, 9]
#

list1 = [8,9,5,6,7,4,3,1,2]

for i in range(len(list1)-1):  # 趟数

    # 遍历剩下未排好序的数，并找出最小数的下标
    minIndex = i
    for j in range(i, len(list1)):
        if list1[j] < list1[minIndex]:
            minIndex = j

    # 交互最小数和第一个数
    # 剩下数中的第一个数: list1[i]
    # 剩下数中的最小数：list[minIndex]
    list1[i], list1[minIndex] = list1[minIndex], list1[i]

print(list1)
