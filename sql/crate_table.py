import pymysql

# 与数据库进行链接并创建表

# 打开数据库连接
conn = pymysql.connect(host='localhost', password='ljj030322@@', user='root', database='p_m_db', charset='utf8')
cursor = conn.cursor()

# 创建表

sql1 = """
CREATE TABLE residents (
resident_id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(50),
  owner_name VARCHAR(50),
  employer VARCHAR(100),
  family_size INT
);
"""
sql2 = """
CREATE TABLE property_staff (
  property_id INT AUTO_INCREMENT PRIMARY KEY,
  position VARCHAR(50) DEFAULT '普通员工',
  property_name CHAR(50) NOT NULL
);
"""
sql3 = """
CREATE TABLE buildings (
  building_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id INT,
  FOREIGN KEY (property_id) REFERENCES property_staff (property_id)
);
"""
sql4 = """
CREATE TABLE house (
  house_id INT AUTO_INCREMENT PRIMARY KEY,
  building_id INT,
  area DECIMAL(10,2),
  resident_id INT,
  FOREIGN KEY (building_id) REFERENCES buildings (building_id),
  FOREIGN KEY (resident_id) REFERENCES residents (resident_id)
);

"""
sql_ = """
    CREATE CLUSTERED INDEX idx_building ON house (building_id);
    CREATE CLUSTERED INDEX idx_resident ON house (resident_id);
"""

sql5 = """
CREATE TABLE property_fees (
  property_fee_id INT AUTO_INCREMENT PRIMARY KEY,
  year INT,
  month INT,
  due_property_fee DECIMAL(10,2),
  paid_property_fee DECIMAL(10,2),
  payment_date DATE,
  property_id INT,
  payment_number VARCHAR(50),
  FOREIGN KEY (property_id) REFERENCES property_staff (property_id) ON DELETE CASCADE
);
"""

sql6 = """
CREATE TABLE parking_spaces (
  parking_space_id INT AUTO_INCREMENT PRIMARY KEY,
  building_number VARCHAR(50),
  room_number VARCHAR(50),
  license_plate VARCHAR(20)
);
"""

sql7 = """
CREATE TABLE parking_fees (
  parking_fee_id INT AUTO_INCREMENT PRIMARY KEY,
  parking_space_id INT,
  year INT,
  month INT,
  due_parking_fee DECIMAL(10,2),
  paid_parking_fee DECIMAL(10,2),
  payment_date DATE,
  property_id INT,
  payment_number VARCHAR(50),
  FOREIGN KEY (parking_space_id) REFERENCES parking_spaces (parking_space_id) ,
  FOREIGN KEY (property_id) REFERENCES property_staff (property_id) ON DELETE CASCADE
);
"""

sql8 = """
CREATE TABLE maintenance (
  maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
  resident_id INT,
  description VARCHAR(200),
  report_date DATE,
  repair_date DATE,
  amount DECIMAL(10,2),
  is_from_repair_fund BOOLEAN,
  repair_person INT,
  FOREIGN KEY (resident_id) REFERENCES residents (resident_id),
  FOREIGN KEY (repair_person) REFERENCES property_staff (property_id)
);
"""

sqls = [sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8]

# for sql in sqls:
#     cursor.execute(sql)
#cursor.execute(sql_)

cursor.close()
conn.close()
