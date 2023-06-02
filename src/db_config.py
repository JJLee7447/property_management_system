import pymysql

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ljj030322@@',
    'database': 'p_m_db'
}


def db_connect():
    conn = pymysql.connect(**db_config)
    return conn
