import pymysql
from constants import *
def exute_query_and_return_output(query,oneout=None,allout=None,manyout=None):
    conn=pymysql.connect(host='localhost',port=3306,database='testdb',user='root',password='Vaibhav@22')
    result=''  #local
    try:
        if conn:
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()  #if want to save the data  #rollback --- undo
            if oneout:
                result=cur.fetchone()  #single record retrive
            if allout:
                result=cur.fetchall()   #all record retrive
            if manyout:
                result=cur.fetchmany(5)  # number of records
            return result
    except Exception as e:
        print(str(e))
    finally:
        cur.close()
        conn.close()
