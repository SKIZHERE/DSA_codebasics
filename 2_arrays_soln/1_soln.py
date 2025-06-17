from typing import Dict

d : Dict[str,int] = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190 }

# 1 In Feb, how many dollars you spent extra compare to January?

x = d.get("February") - d.get("January")
print(f"you spent {x} extra than January")

# 2. Find out your total expense in first quarter (first three months) of the year.

fin = sum(list(d.values())[0:3])
print(f"total expense of first quarter is {fin}")

# 3. Find out if you spent exactly 2000 dollars in any month

k = list(i for i,val in d.items() if val == 2000)
print(k)

