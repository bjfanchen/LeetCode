# 已知一个数组，第i个元素代表第i天的股票价格，如何获取最大收益？
# 提示：股票必须先买后卖，最多只能进行一次交易，获取最大收益必然是低买高卖
# 思路：
# 1.数组2次遍历，找出后面的元素与其前面的元素之间最大的差值，即最大收益，不可取！！！当数组极大时，溢出
# 2.要获取最大收益，必然是一个较小元素和其之后的一个最大（相对）元素之间的差值，
#   通过遍历找出其中的较小的元素，通过计算其后元素与它的差值，将其与当前最大收益比较，最终得到最大收益
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price  # 每次做减法得到当前元素与其之前的最小元素的差值，即当日卖出的收益
            max_profit = max(max_profit, profit)
        return max_profit
