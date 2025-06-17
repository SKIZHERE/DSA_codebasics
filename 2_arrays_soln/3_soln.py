# 3. Find out if you spent exactly 2000 dollars in any month
d = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190 }
k = list(i for i,val in d.items() if val == 2000)
print(k)
print(list(d.items()))