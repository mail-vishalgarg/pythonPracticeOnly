"""
Rotate a list by nth times
Input : n = 2
List_1 = [1, 2, 3, 4, 5, 6]
Output : List_1 = [5, 6, 1, 2, 3, 4]
We get output list after right rotating
"""


def rotateList(lst,n):
    while n > 0:
        tmp = lst[0]
        for index in range(len(lst) - 1):
            lst[index] = lst[index +1]

        lst[index + 1] = tmp
        n -= 1
    print lst

lst = [20,40,30,60]
rotateList(lst,2)
