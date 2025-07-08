arr = {}

with open("../nyc_weather.csv", "r") as f:
    f.readline()
    for i in f:
        sep = i.split(",")
        try:
            day = sep[0]
            temp = int(sep[1])
            arr[day] = temp
        except:
            print("ignore")
print(arr["Jan 9"])
print(arr["Jan 4"])