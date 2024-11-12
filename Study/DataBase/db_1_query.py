# Raw Sql stmnts/ Quries
CREATE_SQL = """create table emp_info(emp_id int,emp_name varchar(40),emp_city varchar(40),emp_sal float,emp_role varchar(40))"""
INSERT_SQL = """insert into emp_info values({},"{}","{}", {}, "{}")"""
RETRIVE_SQL ="""Select * from emp_info"""
RETRIVE_SINGLE = """select * from emp_info where emp_id ={}"""
UPDATE_SQL = """update emp_info set emp_name = "{}" ,emp_role = "{}" where emp_id = {}"""
DELETE_SQL = """delete from emp_info where emp_id = {}"""

Database_Queries = {
    "CREATE_TABLE" : CREATE_SQL,
    "INSERT_RECORD" : INSERT_SQL,
    "UPDATE_RECORD" : UPDATE_SQL,
    "DELETE_RECORD" : DELETE_SQL,
    "RETRIVE_ALL" : RETRIVE_SQL,
    "RETRIVE_SINGLE" : RETRIVE_SINGLE


}