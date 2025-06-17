# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

from typing import Dict
d : Dict[str,int] = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190 }

d.update({"June":1980})
print(d)
