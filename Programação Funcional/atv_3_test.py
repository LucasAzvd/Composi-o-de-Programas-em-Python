from atv_3 import * 

L0 = ['amar', 'o', 'estranho', 'deixa', 'confuso', 'este', 'coracao']
L1 = [1, 2, 3]
print(list(firstChars(L0)))
# ['a', 'o', 'e', 'd', 'c', 'e', 'c']
print(sum(L1))
# 6
print(avg(L1))
# 2
print(maxString(L0))
# 'estranho'
print((buildLenFreq(L0)))
# {8: ['estranho'], 1: ['o'], 4: ['amar', 'este'], 5: ['deixa'], 7: ['confuso', 'coracao']}
print((countFirsts(L0)))
# {'a': 1, 'c': 2, 'e': 2, 'd': 1, 'o': 1}
print(mostCommonFirstChar(L0))
# 'c'

D = {1: ['b'], 2: ['xd'], 3: ['abc']}
add2Dict(D, 2, 'ww')
# {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}


