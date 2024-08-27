#
# @lc app=leetcode id=2043 lang=python3
#
# [2043] Simple Bank System
#

# @lc code=start
class Bank:

    def __init__(self, balance: List[int]):
        self.accountBalances = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        balances = self.accountBalances

        if  account1 < len(balances) and \
            account2 < len(balances) and \
            balances[account1] >= money:

            balances[account1] -= money
            balances[account2] += money

            return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        balances = self.accountBalances

        if  account < len(balances):
            balances[account] += money
            
            return True

        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        balances = self.accountBalances

        if  account < len(balances) and \
            balances[account] >= money:

            balances[account] -= money

            return True

        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end

