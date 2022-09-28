#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1 = 0 
    sum2 = 0
    for t in my_list:
        sum2 += t[0] * t[1]
        sum1 += t[1]
    return (sum2 / sum1)
