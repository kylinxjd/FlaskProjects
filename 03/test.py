# _*_ coding: utf-8 _*_

# 一
# a = 89
# print(bin(a))
# print(str(bin(a)))
# for i in str(bin(a)[2:]):
#     if i == '0':
#         print(1, end='')
#     else:
#         print(0, end='')


# 二
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# 三、

#
# a = '1010'
# b = '1000'
# s1 = 0
# s2 = 0
# a1 = a[::-1]
# b1 = b[::-1]
# for i in range(len(a1)):
#     if a1[i] == '1':
#         s1 += 2 ** i
# print(s1)
#
# for j in range(len(b1)):
#     if b1[j] == '1':
#         s2 += 2 ** j
# print(s2)
#
# s = s1 + s2
#
# bs = bin(s)
# print(bs[2:])


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n == 1:
            result.append('()')
            return result
        else:
            length = n * 2 - 1
            for i in range(0, pow(2, length)):
                binary = bin(i)[2:]
                for j in range(-1, length - len(binary)):
                    binary = '0' + binary
                if self.Is_result(binary):
                    result.append(self.Is_result(binary))
            return result

    def Is_result(self, binary):
        number1 = 0
        number0 = 0
        result = ''
        for i in binary:
            if i == '0':
                result = result + '('
                number0 = number0 + 1
            else:
                result = result + ')'
                number1 = number1 + 1
            if number1 > number0:
                return False
        if number1 != number0:
            return False
        else:
            return result


#
#
s = Solution()
print(s.generateParenthesis(4))


#
# print(pow(2, 4))

def check(bin_str):
    """
    用列表模拟栈判断一串括号是否正确
    :param bin_str: 用二进制表示括号'('：0，')'：1
    :return:
    """
    if bin_str[0] == '1':
        return False
    li = [bin_str[0]]
    for i in bin_str[1:]:
        # 栈内有括号
        if len(li) > 0:
            # 不匹配，入栈
            if li[-1] == i:
                li.append(i)
            # 匹配，出栈
            else:
                li.pop()
        # 栈内为空
        else:
            if i == '1':
                # 出现右括号
                return False
            else:
                # 出现左括号
                li.append(i)
    # 栈内还有括号
    if len(li) > 0:
        return False
    else:
        return True


def parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    if n == 1:
        result.append('()')
        return result
    else:
        length = 2 * n
        # 列出所有可能的括号排列
        for i in range(0, pow(2, length)):
            binary = bin(i)[2:]
            # 将长度不足length 的左侧补0
            for j in range(0, length - len(binary)):
                binary = '0' + binary
            # print(binary)
            if check(binary):
                # 将01 转换成()
                b1 = binary.replace('0', '(')
                b2 = b1.replace('1', ')')
                result.append(b2)
        return result


print(parenthesis(3))
