"""Dynamic Programming for change problem
basic concept:
for c in coins
find the minimum number of coins such to change amount - c

"""

def DPChange(money, coins):
    minimum_coins = {0: 0}
    denominations = {0: 0}
    for m in range(1, money + 1):
        minimum_coins[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                num_coins = minimum_coins[m - coins[i]] + 1
                if num_coins < minimum_coins[m]:
                    minimum_coins[m] = num_coins
                    denominations[m] = coins[i]

    # Denominations:
    coins_returned = []
    amount_pending = money
    while amount_pending > 0:
        coins_returned.append(denominations[amount_pending])
        amount_pending -= denominations[amount_pending]
    return minimum_coins[money], coins_returned

coins = [1, 5, 10, 25]
money = 22
print(DPChange(money, coins))
