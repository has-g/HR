"""
10. 1 Each candy costs Y cents/dollars
and you can return candy wrappers for Z dollars/cents.
Given X number of dollars,
find the maximum candies you can have from a buy + wrapper exchange arrangement.


Assumptions:
1. wrapper value < candy value
2. you can do repeated transactions
3. you stop when you don't have enough money to buy 1 candy
4. Optimising for runtime?
5.
"""
def buyMaxcandies(x, y, z):
    # edge cases:
    if y > x: return 0

    left_over_money = x
    total_candies = 0

    # Simple use case:
    # Money   X = 15
    # candy   y = 2
    # wrapper z = 1

    while left_over_money >= y:
        #First buy: candy = x//y = 15//2 = 7
        candy = left_over_money//y
        print('candy bought=', candy)
        total_candies += candy
        left_over_money = left_over_money%y

        #First sale: wrapper_sale = candy * z = 7*1 = 7
        # left_over_money = wrapper + previous leftover
        wrapper = candy * z
        left_over_money = left_over_money + wrapper
        print('leftover money = ', left_over_money)

    return total_candies

print(buyMaxcandies(16, 2, 2))