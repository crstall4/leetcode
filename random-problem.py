import pandas as pd
import random

difficulty = "All"  # Options: "Easy", "Medium", "Hard", "All"
group = "回溯" # Options: '堆', '链表', '栈', '图', '分治', 'Kadane 算法', '区间', '二叉树', '二分查找', '二叉搜索树', '哈希表', '数组 / 字符串', '滑动窗口', '多维动态规划', '一维动态规划', '数学', '矩阵', '位运算', '二叉树层次遍历', '图的广度优先搜索', '双指针', '字典树', '回溯'

data = pd.read_csv("leetcode_top150.csv")

if difficulty != "All":
    data = data[data['difficulty'] == difficulty.upper()]

if group != "All":
    data = data[data['group'] == group]

random_int = random.randint(0, len(data)-1)
print(data.iloc[random_int])