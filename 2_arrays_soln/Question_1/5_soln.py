# 5. You returned an item that you bought in a month of April and Got a refund of 200$.
# Make a correction to your monthly expense list based on this

from typing import Dict
d : Dict[str,int] = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190 }

x = int(d.get("April")-200)
d["April"] = x
print(d)