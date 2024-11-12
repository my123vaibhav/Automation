import json

with open('D:\\pythonProject\\API-Backend-Automation\\DATA\\ExampleData.json') as f:
    datax1 = json.load(f)

with open('D:\\pythonProject\\API-Backend-Automation\\DATA\\ExampleData2.json') as d:
    datax2 = json.load(d)
    print(datax1 == datax2)
    assert datax1 == datax2
