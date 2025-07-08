arr = []

with open("../nyc_weather.csv", "r") as f:
    f.readline()
    for i in f:
        sep = i.split(",")
        try:
            day = sep[0]
            temp = int(sep[1])
            arr.append(temp)
        except:
            print("ignore")
print(arr)
print(sum(arr[0:8])/7)
print(max(arr[0:10]))

