from collections import defaultdict
from collections import Counter     #
from collections import OrderedDict
from collections import namedtuple


s= [1,5,2,3,4,1,3,5,2,4,1,3,5,1,4]

dd = defaultdict(int)
for key in s:
    dd[key]+=1
    
print(dd)


def sump(a,b):
    return a+b, a*b

s, p = sump(2,3)

print(s,p)