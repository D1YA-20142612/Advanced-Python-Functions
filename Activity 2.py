s1 = {2, 1, 3}
s2 = {'c', 'b', 'a'}
s3 = list(zip(s1,s2))
print(s3)

l1 = [1,4,3,2,3,3,2,4,2,3,1,1,4,2,4,5,2,3]
l2 = [4,2,1,2,4,3,2,5,5,2,3,3,5,6,2,3,1,2,4,1,2,4]

for x, y in zip (l1, l2[::-1]):
    print(x, y)

stocks = {'reliance', 'infoysys', 'tcs'}
prices = {1242, 5343, 1314}

d = {stocks: prices for stocks,
    prices in zip(stocks, prices)}

print('\n{}'.format(d))