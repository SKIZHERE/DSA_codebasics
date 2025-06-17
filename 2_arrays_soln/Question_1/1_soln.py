# 1 In Feb, how many dollars you spent extra compare to January?

from typing import Dict
d : Dict[str,int] = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190 }

x = d.get("February") - d.get("January")
print(f"you spent {x} extra than January")
