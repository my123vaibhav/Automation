from dbconnection import exute_query_and_return_output
from constants import *
def check_id_from_db(id):
    try:
        query=specific_data(id,eq=True)
        result=exute_query_and_return_output(query,oneout=True)
        if result[0]==id:
            return True
        else:
            return False
    except TypeError:
        return True

def chek_name_based_on_id(id,name):
    query = specific_data(id, eq=True)
    result = exute_query_and_return_output(query, oneout=True)
    if result[1]==name:
        return True
    else:
        False

def check_less_than(id):
    queue=specific_data(id,le=True)
    result=exute_query_and_return_output(queue,allout=True)
    print(result)
    for item in result:
        if item[0]<id:
            return True
        else:
            return False

def check_gt_than(id):
    queue=specific_data(id,gt=True)
    result=exute_query_and_return_output(queue,allout=True)
    for item in result:
        if item[0]>id:
            return True
        else:
            return False

def check_notequl_than(id):
    queue=specific_data(id,noeq=True)
    result=exute_query_and_return_output(queue,allout=True)
    for item in result:
        if item[0]!=id:
            return True
        else:
            return False

def check_columns_of_table():
    queue=show_columns("id","city")
    result = exute_query_and_return_output(queue, allout=True)
    for item in result:
        if len(item)==2:
            return True
        else:
            return False

def check_columns_value_from_table():
    queue=show_columns("id","firstname")
    result = exute_query_and_return_output(queue, allout=True)
    list_of_all_id=[]
    list_of_all_firstname=[]
    for item in result:
        list_of_all_id.append(item[0])
        list_of_all_firstname.append(item[1])
    return list_of_all_id,list_of_all_firstname   #(id,firstname)

def check_columns_value_from_table_based_age():
    queue=show_columns("id","age")
    result = exute_query_and_return_output(queue, allout=True)
    list_of_all_id=[]
    list_of_all_ages=[]
    for item in result:
        list_of_all_id.append(item[0])
        list_of_all_ages.append(item[1])
    return list_of_all_id,list_of_all_ages   #(id,firstname)

def check_columns_value_from_table_based_contry():
    queue=show_columns("id","Country")
    result = exute_query_and_return_output(queue, allout=True)
    list_of_all_id=[]
    list_of_all_Country=[]
    for item in result:
        list_of_all_id.append(item[0])
        list_of_all_Country.append(item[1].lower())
    return list_of_all_id,list_of_all_Country   #(id,firstname)


def check_max_salary():
    queue=select_salary(max=True)
    result=exute_query_and_return_output(queue,oneout=True)
    if result[0]==ALLCONSTANT.MAX:
        return True
    else:
        return False

def check_min_salary():
    queue=select_salary(min=True)
    result = exute_query_and_return_output(queue, oneout=True)
    if result[0] == ALLCONSTANT.MIN:
        return True
    else:
        return False

def check_sum_salary():
    queue=select_salary(sum=True)
    result = exute_query_and_return_output(queue, oneout=True)
    if result[0] == ALLCONSTANT.SUM:
        return True
    else:
        return False

def check_count_salary():
    queue=select_salary()
    print(queue)
    result = exute_query_and_return_output(queue, oneout=True)
    if result[0] == ALLCONSTANT.total_record:
        return True
    else:
        return False


def check_sorting_of_data_age_asc():
    queue=asc_order("age")
    result = exute_query_and_return_output(queue, allout=True)
    for i in range(len(result)):
        if (result[0]<result[len(result)-1]):
            return True
        else:
            return False

def check_sorting_of_data_age_desc():
    queue=asc_order("age",desc=True)
    result = exute_query_and_return_output(queue, allout=True)
    for i in range(len(result)):
        if (result[0]>result[len(result)-1]):
            return True
        else:
            return False

def check_or_with_range():
    queue=data_with_records()
    all_ages=[]
    result=exute_query_and_return_output(queue,allout=True)
    for i in result:
        all_ages.append(i[4])
    return all_ages


def check_and_with_range():
    queue=data_with_records(AND=True)
    all_ages=[]
    result=exute_query_and_return_output(queue,allout=True)
    for j in result:
        all_ages.append(j[4])
    return all_ages


def check_in_between():
    queue=data_in_between(yes=True)
    result=exute_query_and_return_output(queue,oneout=True)
    return result[4]

def check_char_in_firstname(char):
    queue=data_based_single_or_more(char)
    result=exute_query_and_return_output(queue,oneout=True)
    return result[1].lower()

def check_total_char_in_firstname(char):
    queue=data_based_on_single(char)
    result=exute_query_and_return_output(queue,oneout=True)
    return (len(result[1]))


def check_name_not_present_in_table():
    list1=['Bob','vaibhav']
    allablnames=check_columns_value_from_table()[1]
    result= [i for i in list1 if i not in allablnames]
    return result

def create_dict_of_id_name():
    id = check_columns_value_from_table()[0]
    names = check_columns_value_from_table()[1]
    print(dict(zip(id,names)))
    d1={}
    for i in id:
        for j in names:
            d1[i]=j
    print(d1)


def show_all_table():
    all_table=[]
    q=show_all_tables()
    result=exute_query_and_return_output(q,allout=True)
    for item in result:
        all_table.append(item[0])
    return all_table

def check_table_copy(tablename):
    query=copy_table(tablename)
    result=exute_query_and_return_output(query,allout=True)
    if tablename in show_all_table():
        return True
    else:
        return False

def trucate_table(table):
    query=truncate_table(table)
    check_table_copy(table)
    exute_query_and_return_output(query, allout=True)
    if table in show_all_table():
        return True
    else:
        return False

def check_drop_table(table):
    queue=drop_table(table)
    check_table_copy(table)
    exute_query_and_return_output(queue,allout=True)
    if table not in show_all_table():
        return True
    else:
        return False












