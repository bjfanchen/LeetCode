"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)  # 将string转为list
        carry, res = 0, []  # carry表示进位数，res表示加法结果
        while len(num1) > 0 or len(num2) > 0:
            # num1.pop()获取低位数，ord()获取其ASCII码值，将其与0的ASCII码做减法获取数值
            n1 = ord(num1.pop()) - ord("0") if len(num1) > 0 else 0  
            n2 = ord(num2.pop()) - ord("0") if len(num2) > 0 else 0
            n = n1 + n2 + carry  # 两位数值相加，再加上低位的进位
            res.append(n % 10)  # res添加进该位的值，考虑到可能会有进位，所以取余
            carry = n // 10  # carry表示进位数
        if carry:res.append(carry)  # 最高位的进位数不可忘记
        return ''.join([str(i) for i in res])[::-1]  
        # res最终结果是list，各元素是各位的数，首元素是个位数，元素类型是int，需要强制转换为str
        # 元素转换为str后，需要将各元素拼接成一个字符串，通过join()实现，最终实现字符串反转得到最终结果
