fileObject = open("D:\\pythonProject\\API-Backend-Automation\\DATA\\abc.txt", "r")
data = fileObject.read()
print(data)
data2=data.split(" ")
for wd in data2:
    print(wd)
