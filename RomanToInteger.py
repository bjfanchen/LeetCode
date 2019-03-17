class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 先使用dict存放字母和数字的对应关系，便于映射
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # dict.get()方法便于获取指定key的value
        # map()表示对str中的每一个字符根据romans映射获取其数值
        # values是一个list，list中每个元素是int类型
        values = map(romans.get, s)  
        result = 0
        # 遍历list中元素，只有当前元素之后有比其大的值，则减去当前值，否则直接加上当前值
        for index in range(len(values)):
            if index < len(values) - 1 and values[index] < values[index + 1]:
                result -= values[index]
            else:
                result += values[index]
        return result
