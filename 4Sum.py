#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: 4Sum.py
# Author: lpqiu
# mail: qlp_1018@126.com
# Created Time: 2014年10月27日 星期一 01时03分53秒
#########################################################################

def get4sum(srcData, target):
    tmpData = [data for data in srcData]
    retList = []

    tmpData.sort()
    sum2KeysMap = {}
    for i in range(0, len(tmpData)):
        for j in range(i + 1, len(tmpData)):
            tmpsum = tmpData[i] + tmpData[j] - target/2.0  # make the 4sum equal the target
            if not sum2KeysMap.get(tmpsum):
                sum2KeysMap[tmpsum] = [(i,j)]
            else:
                sum2KeysMap[tmpsum].append((i,j))

    sum4Keys = set(sum2KeysMap.keys())
    sum4Keys = [val for val in sum4Keys if (val < 0 and -val in sum4Keys) or val == 0]

    retValDict = {}
    for sumVal in sum4Keys:
        for l in sum2KeysMap[-sumVal]:
            for r in sum2KeysMap[sumVal]:
                if l == r:               # avoid if sumVal == 0, l,r = l,l
                    continue
                valIndSet = list(set((l[0], l[1], r[0], r[1])))   # avoid srcData=[1,1,-1] target = 0=> result = [-1,-1,1,1]
                if len(valIndSet) == 4:
                    valIndSet.sort() # tmpData is sorted, so sorted index can get sorted subList
                    retValDict[tuple(tmpData[i] for i in valIndSet)] = None

    retList = [sorted(list(k)) for k in retValDict.keys()]

    return retList

if __name__ =="__main__":
    srcData = [ 0, 0, 0, 0] # 4
    target = 0
    print(get4sum(srcData, target))
