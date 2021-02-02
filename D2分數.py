# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:22:08 2021

@author: MTAEXAM
"""

scort = []
while True:
    insort = int(input("分數"))
    if insort =="":
        break
    else:
        scort.append(insort)
        scort2 = sorted(scort,reverse=True)
        #scort.sort()
        # scort.reverse()
        print(scort2)

        
        


