"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
思路：
1、台阶数小于2，不难发现cost为0
2、台阶数为2，最小cost必为其中较小者
3、台阶数大于2，不难发现最终方案必是以下其一：包括最后一个台阶和不包括最后一个台阶，取两者中较小者即可
初始值设置为cost[0]和cost[1]，依次迭代，min_cost0存放不包含最后一个台阶的方案，min_cost1存放包含最后一个台阶的方案
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 0 or n == 1:return 0
        min_cost0, min_cost1 = cost[0], cost[1]
        for i in range(2, n):
            min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + cost[i]
        return min(min_cost0, min_cost1)
