from selenium import webdriver
import re



#get the html text from driver



def store_array(arr,index):
    url = 'https://space.bilibili.com/4877053/video?tid=0&pn='+str(index)+'&keyword=&order=pubdate'
    driver = webdriver.Chrome('data')
    driver.get(url)
    data = driver.page_source
    #save the data in path
    path = 'save'+str(index)+'.txt'
    file = open(path,"w")
    file.write(data)
    file.close()
    #get all html text where has the tag of <span class="play">...</span> and store it in arr
    tmparr = re.findall('<span class="play"><i class="icon"></i>.*?\s', data)
    #remove all the html tags in arr
    for i in range(len(tmparr)):
        tmparr[i] = re.sub('<.*?>', '', tmparr[i])
    #remove all the spaces in arr
    for i in range(len(tmparr)):
        tmparr[i] = tmparr[i].strip()
    #for all alement in arr, if the string include 万, remove and convert the string to double and multiply by 10000,then turn it into int
    #for all element in arr,if the string not include 万, turn it into int
    for i in range(len(tmparr)):
        if '万' in tmparr[i]:
            tmparr[i] = tmparr[i].replace('万', '')
            tmparr[i] = float(tmparr[i]) * 10000
            tmparr[i] = int(tmparr[i])
        else:
            tmparr[i] = int(tmparr[i])
    arr += tmparr

#for loop from index 1 to 6
arr = []
for i in range(1,7):
    store_array(arr,i)

#store the arr as data in data.txt
path = 'data.txt'
file = open(path,"w")
file.write(str(arr))
file.close()
