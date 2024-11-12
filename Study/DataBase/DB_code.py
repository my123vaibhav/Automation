import pymysql
# laptop ---65k---single service hou shakti
#defulat mysql=3306, oracle-1521, postgres=5432
def get_database_connection():
    try:
        conn = pymysql.connect(host="localhost",user="root",password="root",database="db2",port=3306)
        print("Connection is successful")
        return conn
    except:
        print("Problem occured")

def establish_channel(sql):
    conn = None
    channel = None
    try:
        conn = get_database_connection()
        channel = conn.cursor()
        channel.execute(sql) # this is line actually responsible exe query on mysql db
    except BaseException as b:
        print("problem in query execution",b)
    else:
        conn.commit()
    finally:
        if channel:
            channel.close()
        if conn:
            conn.close()

def retrive_data(sql,many = True):
    conn = None
    channel = None
    try:
        conn = get_database_connection()
        channel = conn.cursor()
        channel.execute(sql)
        if many:
            return channel.fetchall()
        else:
            return channel.fetchone()
    except:
        print("problem in query execution")
    else:
        conn.commit()
    finally:
        if channel:
            channel.close()
        if conn:
            conn.close()
