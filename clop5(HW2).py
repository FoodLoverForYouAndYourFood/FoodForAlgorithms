def clop5(prices):
    one_plus_wow = [1] * len(prices)
    wow = len(prices)
    for i in range(1, wow):
        if prices[i-1] - prices[i] == 1:
            one_plus_wow[i] = one_plus_wow[i-1] + 1

    return sum(one_plus_wow)


print(clop5([1]))