#Find the thirteen adjacent digits in the 1000-digit number
# that have the greatest product. What is the value of this product?

big_num = """731671765313306249192251196744265747423553
49194934969835203127745063262395783180169848018694
78851843858615607891129494954595017379583319528532
088055111254069874715852386305071569329096329522744
3043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

big_num = ''.join(big_num.split())
big_num=list(big_num)


j=0
products = []
while j < len(big_num)-13:
    i= 0
    product = 1
    while i < 13:
        current = (i) + j
        print(int(big_num[current]))
        product = product * int(big_num[current])

        i +=1
    print( "Product ", product)
    products.append(product)
    j +=1

maximal = max(products)
print(maximal)


# for x in range(0,len(big_num)):
#     product = big_num[x]
#     if x <= (len(big_num)-13):
#         for y in range(0, 14):
#             product = product*int(product[x+y])
#     print(product)