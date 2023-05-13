import re
import matplotlib.pyplot as plt

path = 'data.txt'
#read an array from path
file = open(path,"r")
data = file.read()
file.close()
#remove symbol like [ ] and \n
data = re.sub('[\[\]\n]', '', data)

#convert the string to array
data = data.split(',')
#convert the string to int
for i in range(len(data)):
    data[i] = int(data[i])
#sort the array
data.sort()

#remove the largest value in data
data.pop()
#visualize the array to historgram

#get the average of data
avg = sum(data)/(len(data)-1)
print('average:',avg)

plt.hist(data)
#set x axis label as 播放量
plt.xlabel('play')
#set y axis label as 影片數量
plt.ylabel('movie numbers')
plt.show()