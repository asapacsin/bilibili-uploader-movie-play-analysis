import re
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

#remove the largest value in data
data.remove(max(data))
#reverse the data
data.reverse()


#create a linear regression model
model = LinearRegression()
#reshape the data to 2D array
x_index = [[i+1] for i in range(len(data))]
#fit the data to model
model.fit(x_index,data)
y_predict = model.predict(x_index)
#visualize the data to do scatter plot

plt.scatter(x_index,data,c="blue")
#make a linear fit  on plt
plt.plot(x_index,y_predict,c='red')
#show the regression line equation
print('y = ',model.coef_[0],'x + ',model.intercept_)
#show the r value
print('r = ',model.score(x_index,data))
#set x axis label as 影片編號
plt.xlabel('movie number')
#set y axis label as 播放量
plt.ylabel('play')
plt.show()
