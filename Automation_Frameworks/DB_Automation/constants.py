class ALLCONSTANT:
    MAX=35000.00
    MIN=21000.00
    SUM=1674000.00
    total_record=60
def all_data():
    return 'select *from employee'

def specific_data(id,eq=None,noeq=None,le=None,gt=None):   #id,relation
    if eq:
        return f'select *from employee where id={id}'
    if noeq:
        return f'select *from employee where id!={id}'
    if le:
        return f'select *from employee where id<{id}'
    if gt:
        return f'select *from employee where id>{id}'

def show_columns(col1,col2):
    return f'select {col1},{col2} from employee'

def select_salary(max=None,min=None,sum=None):
    if max:
        return f'select max(salary) from employee'
    if min:
        return f'select min(salary) from employee'
    if sum:
        return f'select sum(salary) from employee'
    else:
        return 'select count(*) from employee'

def asc_order(val,desc=None):
    if desc:
        return f'select *from employee order by {val} desc'
    else:
        return f'select *from employee order by {val}'

def data_with_records(AND=None):
    if AND:
        return f'select *from employee where age>20 {"and"} age<30'
    else:
        return f'select *from employee where age>20 {"or"} age<30'

def data_in_between(yes=None):
    if yes:
        return 'select *from employee where age in (20,30,40)'
    else:
        return 'select *from employee where age not in (20,30,40)'

def data_based_single_or_more(char):
    return f'select *from employee where firstname like "sample%" '.replace('sample',f'{char}')

def data_based_on_single(char):
    return f'select *from employee where firstname like "U_" '.replace('U', f'{char}')

def max_salary_from_employee():
    return 'select max(salary) from employee where salary<(select max(salary) from employee)'



def copy_table(tbname):
    return f'create table {tbname} as select *from employee'

def delete_data_from_table_based_on_id(id,tbname):
    return f'delete from {tbname} where id={id}'

def truncate_table(tbname):   #table ----> data delete ---> table present
    return f'truncate table {tbname}'

def drop_table(tbname):
    return f'drop table {tbname}'


def show_all_tables():
    return 'show tables'



print('hi')