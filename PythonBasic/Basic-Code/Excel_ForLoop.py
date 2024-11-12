from openpyxl import load_workbook

wb = load_workbook(filename='D:\\pythonProject\\API-Backend-Automation\\DATA\\Excel-Data.xlsx', read_only=True)
ws = wb['Sheet2']

emp = ""
for row in ws.rows:
    for cell in row:
        # emp = emp + ''.join(str(cell.value))
        emp = emp + " " + str(cell.value)
    # print(cell.value, end=" ")
    # emptstr = empstr+str(cell.value)
# Close the workbook after reading
wb.close()
# print(emptstr)
li = emp.strip(" ").split(" ")
li1 = []
li2 = []
# print(li)
for i in range(len(li)):
    if li[i].isalpha():
        li1.append(li[i])
print(li1)

for i in range(len(li)):
    if li[i].isnumeric():
        li2.append(li[i])
print(li2)

print(li)
