DATA_10cm = "graphs/us_sensor/us_sensor_10cm.csv"
DATA_20cm = "graphs/us_sensor/us_sensor_20cm.csv"
DATA_30cm = "graphs/us_sensor/us_sensor_30cm.csv"

file1 = open(DATA_10cm, "r")
list1 = []
sum = 0
for i in file1.readlines():
    list1.append(int(i))
    sum += int(i)
mean = sum/(list1.length)
st_dev_sum = 0
for i in list1:
    st_dev_sum += (i - mean)**2
st_dev = (st_dev_sum/list1.length)**0.5


print("us sensor 10cm \nmax:" + max(list1) + "\nmin:" + min(list1) + "\nmean:"+ mean + "\nstandard deviation:" + st_dev)
print()

