# coding=utf-8
'''
@Author: Ulysses
@Description: 面试算法题
@Date: 2020-06-22 19:21:32
@LastEditors: Ulysses
@LastEditTime: 2020-06-22 20:20:12
'''
# %%
"""
有两个序列a,b，大小都为n,序列元素的值任意整数，无序；要求：通过交换a,b 中的元素，
使[序列a 元素的和]与[序列b 元素的和]之间的差最小。
"""
"""
当前数组a和数组b的和之差为A = sum(a) - sum(b)，a的第i个元素和b的第j个元素交换后，
a和b的和之差为 A’ = sum(a) - a[i] + b[j] - （sum(b) - b[j] + a[i]) 
                = sum(a) - sum(b) - 2 (a[i] - b[j]) = A - 2 (a[i] - b[j]) 
设x = a[i] - b[j]，那么 A’ = |A - 2x|，当然A’ 越小也好，
所以当x 在 (0,A)之间时，做这样的交换才能使得交换后的a和b的和之差变小，
x越接近A/2效果越好,如果找不到在(0,A)之间的x，则当前的a和b就是答案。 
所以算法大概如下：在a和b中寻找使得x在(0,A)之间并且最接近A/2的i和j，
交换相应的i和j元素，重新计算A后，重复前面的步骤直至找不到(0,A)之间的x为止。
"""

l1 = [100,99,98,1,2, 3]
l2 = [1, 2, 3, 4,5,40]

def change(l1, l2):
    flag = True
    n = len(l1)
    while flag:
        flag = False
        best_position = ()
        min_diff = float('inf')
        for i in range(n):
            for j in range(n):
                m = l1[i] - l2[j]
                diff_sum = abs(sum(l1) - sum(l2))
                diff_sum_2_m = abs(m - diff_sum / 2)
                if 0<m<diff_sum and diff_sum_2_m < min_diff:
                    min_diff = diff_sum_2_m
                    best_position = (i, j)
                    # l1[i], l2[j] = l2[j], l1[i]
                    flag = True
        if flag:
            i, j = best_position
            l1[i], l2[j] = l2[j], l1[i]


change(l1, l2)
print(l1)
print(l2)
print(sum(l1), sum(l2))


# %%
# 有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
data=['-','-','+','-','+','+','-','+','+','-','-','+','-']
num_string = {
    '-':0,
    '+':1
}
sorted(num_string[i] for i in data)
def string_sort(data):
    num_string = {
        '-':1,
        '+':0
    }
    string_num = {0:'+', 1:'-'}
    return [string_num[j] for j in sorted(num_string[i] for i in data)]
    
print(string_sort(data))

def string_sort1(data):
    n = len(data)
    start = end = 0
    while start + end < n:
        if data[start] == '-':
            data[start], data[n-end-1] = data[n-end-1], data[start]
            end += 1
        else:
            start += 1
    return data
print(string_sort1(data))
# %%
"""
 2、人类的数字是：1、2、3、4、5、6、7、8、9、10、11、12、13、14、15、16、17、
 18、19、20、21、22、23、24、25、26、27、28、29、30。。。。。

      外星人数字是：1、2、4、5、6、7、9、10、11、12、14、15、16、17、19、20、
      21、22、24、25、26、27、29、40、41、42、44、45、46、47、49。。。。。

需求：输入一个外星人数字，输出对应的人类数字，比如外星人9数字，对应人类数字7
无 3 和 8
"""
def alien_to_human(n):
    three = '3'
    eight = '8'
    l = 0
    for i in range(1, n+1):
        s = str(i)
        if (three in s) or (eight in s):
            continue
        else:
            l += 1
    return l
print(alien_to_human(29))

# %%
# 给定任意一个正整数，求比这个数大且最小的“不重复数”，“
# 不重复数”的含义是相邻两位不相同，
# 例如1101是重复数，而1201是不重复数


def find_no_repeat(num):
    def is_repeat(num):
        lst = list(str(num))
        n = len(lst)
        for i in range(1, n):
            if lst[i] == lst[i-1]:
                return True
        return False
    res = num
    while True:
        res += 1
        if not is_repeat(res):
            return res

find_no_repeat(11230)

# %%
"""
数轴上从左到右有n各点a[0], a[1], ……,a[n -1]，给定一根长度为L的绳子，求绳子最多能覆盖其中的几个点
"""
rope_len = 26
array = [-20, -10, -5, 0 , 1, 6, 10, 18, 25]
def rope(array, rope_len):
    max_res = 1
    n = len(array)
    distance = [array[i+1] - array[i] for i in range(n-1)]
    index = 0
    for i in range(n-1):
        templen = 0
        j = 0
        temp = 0
        while templen <= rope_len and j < n-1-i:
            temp += 1
            templen += distance[i+j]
            j += 1 
        if temp > max_res:
            max_res = temp
            index = i
    return max_res, index
print(rope(array, rope_len))

# %%
