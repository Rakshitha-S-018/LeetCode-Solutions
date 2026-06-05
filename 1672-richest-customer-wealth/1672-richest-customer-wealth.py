class Solution:
    def maximumWealth(self, accounts):
        wealth = 0

        for i in accounts:
            wealth = max(wealth, sum(i))

        return wealth