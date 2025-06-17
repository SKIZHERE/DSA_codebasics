# 2. Find out your total expense in first quarter (first three months) of the year.

from typing import Dict
d : Dict[str,int] = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190 }

fin = sum(list(d.values())[0:3])
print(f"total expense of first quarter is {fin}")
