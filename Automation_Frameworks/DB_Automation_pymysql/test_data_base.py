import pytest
from helper_database import *
def test_id_from_table_4():
    assert check_id_from_db(4),'failed due to id'
def test_id_from_table_5():
    assert check_id_from_db(5),'failed due to id'
def test_id_from_table_6():
    assert check_id_from_db(6),'failed due to id'
def test_id_from_table_66():
    assert check_id_from_db(66),'failed due to id'
def test_id_from_table_str():
    assert check_id_from_db('6'),'failed due to id'
def test_id_from_table_empty():
    assert check_id_from_db(' '),'failed due to id'

def test_idname_from_table1():
    assert chek_name_based_on_id(1,'Garett'),'failed due to id'

def test_idname_from_table2():
    assert chek_name_based_on_id(3,'Bob'),'failed due to id'

def test_idname_from_table3():
    assert chek_name_based_on_id(41,'Nick'),'failed due to id'
def test_idname_from_table4():
    assert chek_name_based_on_id(50,'Wendy'),'failed due to id'

def test_id_from_table_str():
    assert check_id_from_db('6'),'failed due to id'

def test_lessthan_id_50():
    assert check_less_than(50),'failed due to id'

def test_lessthan_id_10():
    assert check_less_than(10),'failed due to id'

def test_lessthan_id_3():
    assert check_less_than(3),'failed due to id'

def test_geterthan_id_50():
    assert check_gt_than(50),'failed due to id'

def test_greterthan_id_10():
    assert check_gt_than(10),'failed due to id'

def test_greterthan_id_3():
    assert check_gt_than(3),'failed due to id'

def test_not_equal_id_10():
    assert check_notequl_than(10),'failed due to id'

def test_not_equal_id_3():
    assert check_notequl_than(3),'failed due to id'

def test_check_coulumn_of_table():
    assert check_columns_of_table(),'failed due to id'

def test_check_specifi_id_10():
    id=10
    assert id in check_columns_value_from_table()[0]

def test_check_specifi_id_0():
    id=0
    assert id not in check_columns_value_from_table()[0]

def test_check_specifi_id_55():
    id=55
    assert id in check_columns_value_from_table()[0]

def test_check_specifi_id_55():
    id="#"
    assert id not in check_columns_value_from_table()[0]


def test_check_specifi_name_tina():
    name="Tina"
    assert name in check_columns_value_from_table()[1]

def test_check_specific_name_bob():
    name="Bob"
    assert name in check_columns_value_from_table()[1]

def test_check_specifi_name_nina():
    name="Nina"
    assert name in check_columns_value_from_table()[1]

def test_check_specific_anyname():
    name="1@32345"
    assert name in check_columns_value_from_table()[1]

def test_check_specific_age_100():
    age=100
    assert age not in check_columns_value_from_table_based_age()[1]


def test_india_contry_in_data():
    Country='india'
    assert Country in check_columns_value_from_table_based_contry()[1]

def test_uk_contry_in_data():
    Country='uk'
    assert Country in check_columns_value_from_table_based_contry()[1]


def test_max_salary_from_emp():
    assert check_max_salary(),'failed due to max salary'


def test_min_salary_from_emp():
    assert check_min_salary(),'failed due to min salary'

def test_total_salary_from_emp():
    assert check_sum_salary(),'failed due to total salary'

def test_count_from_emp():
    assert check_count_salary(),'failed due to count of the records salary'


def test_sort_age_asc():
    assert check_sorting_of_data_age_asc(),'failed due to asc order of age'



def test_sort_age_desc():
    assert check_sorting_of_data_age_desc(),'failed due to desc order of age'


def test_age_with_or():
    assert 19 in check_or_with_range(),'failed due to desc order of age'


def test_age_with_and():
    assert 19 not in check_and_with_range(),'failed due to desc order of age'


def test_age_with_inbetween():
    assert check_in_between() in [10,20,40,30],'failed due to desc order of age'


def test_first_start_with_a():
    ch='a'
    assert ch in check_char_in_firstname(ch),'failed due to desc order of age'


def test_first_start_with_b():
    ch='b'
    assert ch in check_char_in_firstname(ch),'failed due to desc order of age'


def test_first_start_with_z():
    ch='z'
    assert ch in check_char_in_firstname(ch),'failed due to desc order of age'

def test_first_name_with_3char():
    assert 3 == check_total_char_in_firstname("__"),'failed due to desc order of age'

def test_create_table():
    t='Employee1'
    assert check_table_copy(t),'failed due to desc order of age'

def test_create_table2():
    t='Employee2'
    assert check_table_copy(t),'failed due to desc order of age'

def test_create_table3():
    t='Table1'
    assert check_table_copy(t),'failed due to desc order of age'

def test_trucate_table1():
    t='Table2'
    assert trucate_table(t),'failed due to desc order of age'

def test_trucate_table3():
    t='Table3'
    assert trucate_table(t),'failed due to desc order of age'

def test_drop_table1():
    t='Table1'
    assert check_drop_table(t),'failed due to desc order of age'

def test_drop_table2():
    t='Table2'
    assert check_drop_table(t),'failed due to desc order of age'
