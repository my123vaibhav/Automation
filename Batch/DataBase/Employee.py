
class Employee:
    def __init__(self, emp_id,emp_name,emp_city,emp_sal,emp_role):
        self.emp_id =emp_id
        self.emp_name = emp_name
        self.emp_city = emp_city
        self.emp_sal = emp_sal
        self.emp_role = emp_role

    def __str__(self):
        return f"""
            Employee Id : {self.emp_id},
            Employee Name : {self.emp_name},
            Employee City : {self.emp_city},
            Employee Salary : {self.emp_sal},
            Employee Role : {self.emp_role}
            """
    def __repr__(self):
        return str(self)
