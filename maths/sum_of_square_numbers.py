import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # TODO 超时原因未定
        # n = int(math.sqrt(c)) + 1
        # temp = []
        # for i in range(n):
        #     temp.append(i*i)
        #     if c - i*i in temp:
        #         return True
        # return False
        # xrange()返回的是一个生成器，c**.5表示c的二分之一次方，int()取整
        return any(self.is_square(c-a*a) 
                    for a in xrange(int(c**.5)+1))
    # 判断一个数是不是平方数
    def is_square(self, N):
            return int(N**.5)**2 == N
