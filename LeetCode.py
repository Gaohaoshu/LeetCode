import sys


# 算法
def twoSum(nums, target):  # 两数之和
    l = []
    for i in range(len(nums)):
        data = int(target - nums[i])
        rest = nums.copy()
        del rest[i]
        # rest = set(nums) - {nums[i]}  # 存在部分问题，【3,3】这种连带的重复值会被删光，变成空值
        # print(data, rest, nums)
        if data in rest:
            l.append(i)
            j = rest.index(data) + 1
            l.append(j)
            # print(l)
            break
        else:
            i += 1

    print(l)
    return l


def isPalindrome(x):  # 是否回文数
    num = str(x)
    l = len(num)
    total = int(0)
    if l % 2 == 0:
        for i in range(int(l / 2)):
            j = int(l - i - 1)
            if num[i] == num[j]:
                total += 0
            else:
                total += 1
    elif l == 0:
        total = total
    else:
        for i in range(int((l - 1) / 2)):
            j = int(l - i - 1)
            if num[i] == num[j]:
                total += 0
            else:
                total += 1
    # print(total)
    if total == 0:
        return True
    else:
        return False


def longestCommonPrefix(strs):  # 最长前缀判断
    min_index = 0
    len_str = len(strs[0])
    stack = [strs[0]]
    for index, string in enumerate(strs):
        if len(string) < len_str:
            stack.pop()
            min_index = index
            len_str = len(string)
            stack.append(string)
    # print(stack)
    s = ''
    listlen = len(strs)
    slen = len(strs[min_index])
    break_flag = False
    for i in range(slen):
        for j in range(listlen):
            if strs[j][i] == stack[0][i]:
                j += 1
                if j == int(listlen):
                    s = s + str(stack[0][i])
            else:
                break_flag = True
                # l.pop()
                break
        if break_flag:
            break
    print(s)
    return s


def isValid(s: str) -> bool:  # 有效括号问题
    dict = {'(': ')', '{': '}', '[': ']'}
    # 判断是否是键，如果是加入栈，如果不是则出栈，判断键值是否配对
    stack = []
    if len(s) == 0:
        return False
    else:
        for i in range(len(s)):  # 这里可以有 for item in s: 这种写法更清楚
            if s[i] in dict:
                stack.append(s[i])
                i += 1
            else:
                if len(stack) != 0:
                    if dict.get(stack[-1]) == s[i]:
                        stack.pop()
                        i += 1
                    else:
                        stack.append('N')
                        break
                else:
                    stack.append('N')
                    break
    print(stack)
    return len(stack) == 0


def strStr(haystack: str, needle: str) -> int:  # 一个字符串里面包含另一个字符串
    if len(needle) == 0:
        return 0
    else:
        if needle in haystack:
            print(haystack.find(needle))
            return haystack.find(needle)
        else:
            return '-1'


def lengthOfLastWord(s: str) -> int:  # 不包含空格的最后一个单词的长度
    # 思路一： 先通过rfind判断最后一位是否空格
    #       是空格则反转 ，replace空格之后相减，得到最后有几个空格，再enumerate
    #       不是空格则直接enumerate方法
    # l = []
    # print(len(s))
    # for i, element in enumerate(s):
    #     if element == ' ':
    #         l.append(i)
    # print(l)
    # if s.count(' ') > 0:
    #     if s.rfind(' ') == len(s) - 1:
    #         lreverse = s[::-1]
    #         num = (len(lreverse)) - len(lreverse.lstrip())
    #         if l[0] != l[-num]:
    #             final = l[-num] - l[-num - 1] - 1
    #         else:
    #             final = l[-num]
    #     else:
    #         final = len(s)-l[-1]-1
    # else:
    #     final = len(s)
    # print(final)
    # return final

    # 思路二 去掉两边空格之后再用空格分割，取最后一个的长度
    print(len(s.strip(' ').split(' ')[-1]))
    return len(s.strip(' ').split(' ')[-1])


def plusOne(digits):  # 非负整数加一
    #  思路用.join()方法拼接
    s1 = int(''.join(map(str, digits))) + 1
    # print(s1)
    print(list(map(int, list(str(s1)))))
    return list(map(int, list(str(s1))))


def joinlist(*args):  # list连接
    l = []
    for i in range(len(args)):
        l = sum((l, args[i]), [])
        i += 1
    print(l)
    return l


def climbStairs(n: int) -> int:  # 爬楼梯，动态规划中的斐波那契数
    #  动态规划五步，详见网站收藏栏
    if n == 1:
        step = 1
    elif n == 2:
        step = 2
    else:
        step = climbStairs(n - 1) + climbStairs(n - 2)  # 递归的方式可能比较慢
    print(step)
    return step

    # dp = [0] * (n+1)  # 动态规划的思路
    # dp[0] = 1
    # for i in range(n+1):
    #     for j in range(1,3):
    #         if i >= j:
    #             dp[i] += dp[i-j]
    # return dp[-1]


def maxProfit() -> int:
    return ''
    # 添加注释测试用


if __name__ == '__main__':
    # twoSum([100,3,4,3], 6)
    # isPalindrome(123456789)
    # longestCommonPrefix(["flower", "flow", "flight"])
    # isValid('{[]')
    # strStr('mississippi', 'issip')
    # lengthOfLastWord('ac')
    # plusOne([1, 9, 9])
    # joinlist([1, 2, 3], [3, 4], [7, 8, 0])
    climbStairs(5)