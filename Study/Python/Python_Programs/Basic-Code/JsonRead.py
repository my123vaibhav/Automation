import json

course = '{"name": "morpheus", "job": "leader","id": ["358", "123456"]}'

dict_course = json.loads(course)
# print(type(dict_course))
# print(dict_course['id'][1])

print("-------------------------------------File read Program1----------------------------")

with open('D:\\pythonProject\\API-Backend-Automation\\DATA\\ExampleData.json') as f:
    data = json.load(f)
    print(data['data'])
    emp_data = data['data']
    print(type(emp_data))
    print(emp_data[1])
    print(type(emp_data[1]))
    emp_details = emp_data[1]
    print(emp_details['last_name'])

print("-------------------------------------File read Program2----------------------------")
with open('D:\\pythonProject\\API-Backend-Automation\\DATA\\ExampleData.json') as f:
    datax = json.load(f)
    print(datax['data'])
    empx = datax['data']
    for x in empx:
        print(x['email'])
        if x['email'] == "tobias.funke@reqres.in":
            print(x['email'])
    # print(empx[1])
    # print(type(empx[1]))
    # print(empx[1]['email'])
