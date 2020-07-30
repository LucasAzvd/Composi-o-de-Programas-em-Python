from atv_5 import *

delInitials(['Fer', 'mag', 'Q', 'pereira'])
# 'Fer, Mag, Pereira'
delInitials(['Fer', 'm', 'Q', 'pereira'])
# 'Fer, Pereira'
delInitials(['Fer', 'mag', 'Q', 'pereira', 'S', 'Sa'])
# 'Fer, Mag, Pereira, Sa'
delInitials(['a', 'aa', 'b', 'bb'])
# 'Aa, Bb'
everyOccurrence('Fernando', 'aeiou')
# [1, 4, 7]
everyOccurrence('xaxbxaxyza', 'aeiou')
# [1, 5, 9]
everyOccurrence('0a1e2i3o4u', 'aeiou')
# [1, 3, 5, 7, 9]
factors(6)
# [2, 3]
factors(10)
# [2, 5]
factors(12)
# [2, 3, 4, 6]
factors(28)
# [2, 4, 7, 14]
isPerfect(6)
# True
isPerfect(10)
# False
isPerfect(12)
# False
isPerfect(28)
# True