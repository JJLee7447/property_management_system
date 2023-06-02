import pymysql

conn = pymysql.connect(host='localhost', password='ljj030322@@', user='root', database='p_m_db', charset='utf8')
cursor = conn.cursor()
def insert_residents():


    sqls = """
    INSERT INTO residents (email, owner_name, employer, family_size)
VALUES 
  ('bob@example.com', 'Bob Johnson', 'DEF Industries', 3),
  ('alice@example.com', 'Alice Brown', 'GHI Corp', 1),
  ('tom@example.com', 'Tom Wilson', 'JKL Ltd', 2);
            """
    cursor.execute(sqls)
    conn.commit()
    cursor.close()
    conn.close()

def insert_staff():

    sql ="""INSERT INTO property_staff (position, staff_name)
VALUES 
  ('普通员工', '张三'),
  ('普通员工', '李四'),
  ('普通员工', '王五'),
  ('管理员', '赵六'),
  ('普通员工', '刘七');
"""
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def select():
    conn = pymysql.connect(host='localhost', password='ljj030322@@', user='root', database='p_m_db', charset='utf8')
    cursor = conn.cursor()

    sql = 'select * from residents'

    cursor.execute(query=sql)

    res = cursor.fetchall()
    print(res)


insert_staff()
