from Employee import Employee
from abc import ABC,abstractmethod
from db_1_query import *
from DB_code import establish_channel,retrive_data

class empServices(ABC):

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def get_single(self):
        pass

    @abstractmethod
    def add_employee(self):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def update_employee(self):
        pass

class EmployeeServImpl(empServices):

    def create_table(self):
        create_sql = Database_Queries["CREATE_TABLE"]
        establish_channel(create_sql)

    def get_single(self,empid):
        retrive_single = Database_Queries["RETRIVE_SINGLE"]
        retrive_single = retrive_single.format(empid)
        print(retrive_data(retrive_single, False))

    def add_employee(self,emp):
        insert_sql = Database_Queries["INSERT_RECORD"]
        insert_sql = insert_sql.format(emp.emp_id,emp.emp_name,emp.emp_city,emp.emp_sal,emp.emp_role)
        establish_channel(insert_sql)
        print(" Employee inserted")

    def get_all_employees(self):
        retrive_sql = Database_Queries["RETRIVE_ALL"]
        emp_db = retrive_data(retrive_sql)
        for emp in emp_db:
            print(Employee(emp[0],emp[1],emp[2],emp[3],emp[4]))

    def update_employee(self,emp,empid):
        update_sql = Database_Queries["UPDATE_RECORD"]
        update_sql = update_sql.format(emp.emp_name, emp.emp_role,empid )
        establish_channel(update_sql)

    def avarage_salary(self):
        avg = retrive_data("select avg(emp_sal) from emp_info", many=False)
        print("Avarage Salary===", avg)
e1 = EmployeeServImpl()

#e1.get_all_employees()
#e1.update_employee(Employee(102,"QQQ","Pune",1234.56,"Sr. Lead"),1002)
e1.get_all_employees()
e1.avarage_salary()
#e1.add_employee(Employee(emp_id=1002,emp_name="XXX",emp_city="Mumbai",emp_sal=7654,emp_role="Software Engineer"))
#e1.create_table()
#e1.get_all_employees()
#e1.get_single(1001)