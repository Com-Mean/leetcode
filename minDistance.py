#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: minDistance.py
# Author: lpqiu
# mail: qlp_1018@126.com
# Created Time: 2014年10月27日 星期一 05时19分45秒
#########################################################################

# recusive version
def minDist(sortedList):
    if not sortedList:
        return ([], [])

    large = sortedList[-1]
    secondLarge = sortedList[-2]

    largeList, smallList = minDist(sortedList[:-2])
    largeList.append(secondLarge)
    smallList.append(large)
    #print('LargeList:', largeList, 'SmallList', smallList)

    if sum(largeList) > sum(smallList):
        return (largeList, smallList)
    else:
        return (smallList, largeList)

# iteriation version
def minDistIterVer(sortedList):
    largeList, smallList = [], []

    for i in range(0, len(sortedList), 2):
        if sum(largeList) > sum(smallList):
            largeList.append(sortedList[i])
            smallList.append(sortedList[i + 1])
        else:
            largeList.append(sortedList[i + 1])
            smallList.append(sortedList[i])

    if sum(largeList) > sum(smallList):
        return (largeList, smallList)
    else:
        return (smallList, largeList)
    
def testMain(listA, listB):                     # len(listA) == len(listB) = n
    print("Sorted List: ", sorted(listA + listB))
    largeList, smallList = minDist(sorted(listA + listB))
    print(largeList, smallList, "distance: ", sum(largeList) - sum(smallList))

    largeListIterVer, smallListIterVer = minDistIterVer(sorted(listA + listB))
    print(largeListIterVer, smallListIterVer, "distance: ", sum(largeListIterVer) - sum(smallListIterVer))


if __name__ == "__main__":
    listA = [1,-1,2,3,6,189]; listB = [2,3,4,6,7,123]
    testMain(listA, listB)
