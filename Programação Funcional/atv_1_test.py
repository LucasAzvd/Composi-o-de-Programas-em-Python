from atv_1 import *

mSort(py2ll([5,5,4,3,2,1,2,3,4]))
# [1, 2, 2, 3, 3, 4, 4, 5, 5]
mSort(py2ll([5, 11, 2, 5, 3, 7, 2, 17, 3]))
# [2, 2, 3, 3, 5, 7, 11, 17]

max(py2ll([3, 4, 2, 5, 2, 1]))
# 5
max(py2ll([0, 0, 0, 0]))
# 0
max(py2ll([0, 0, 1, 0]))
# 1
sum(py2ll([0, 0, 1, 0]))
# 1
sum(py2ll([1, 2, 3, 4]))
# 10
get(py2ll([3, 4, 2, 5, 2, 1]), 0)
# 3
get(py2ll([3, 4, 2, 5, 2, 1]), 1)
# 4
get(py2ll([3, 4, 2, 5, 2, 1]), 2)
# 2

