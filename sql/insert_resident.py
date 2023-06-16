from src.db_config import db_connect


def insert_resident():
    conn = db_connect()
    cursor = conn.cursor()
    sql ="""
    INSERT INTO residents (email, owner_name, employer, family_size) VALUES
    ('john@example.com', 'John Smith', 'ABC Company', 3),
    ('jane@example.com', 'Jane Doe', 'XYZ Corporation', 2),
    ('mike@example.com', 'Mike Johnson', '123 Industries', NULL),
    ('sarah@example.com', 'Sarah Thompson', NULL, NULL),
    ('alex@example.com', 'Alex Brown', 'DEF Corp', 4),
    ('emily@example.com', 'Emily Wilson', 'GHI Ltd', 2),
    ('matt@example.com', 'Matt Davis', NULL, 1),
    ('laura@example.com', 'Laura Clark', 'JKL Corporation', NULL),
    ('ben@example.com', 'Benjamin Lee', 'MNO Enterprises', 5),
    ('sophia@example.com', 'Sophia Rodriguez', 'PQR Co.', NULL),
    ('daniel@example.com', 'Daniel Martinez', NULL, 2),
    ('olivia@example.com', 'Olivia Anderson', 'STU Corporation', 3),
    ('liam@example.com', 'Liam Wilson', NULL, 2),
    ('ava@example.com', 'Ava Johnson', 'VWX Ltd', NULL),
    ('jackson@example.com', 'Jackson Taylor', 'YZ Corp', 4),
    ('mia@example.com', 'Mia Brown', NULL, 2),
    ('aiden@example.com', 'Aiden Davis', 'ABC Company', NULL),
    ('isabella@example.com', 'Isabella Anderson', 'XYZ Corporation', 3),
    ('ethan@example.com', 'Ethan Garcia', NULL, 2),
    ('sophia@example.com', 'Sophia Hernandez', '123 Industries', NULL),
    ('mason@example.com', 'Mason Wilson', 'GHI Ltd', 4),
    ('mia@example.com', 'Mia Thompson', NULL, 1),
    ('jacob@example.com', 'Jacob Lewis', 'JKL Corporation', NULL),
    ('ava@example.com', 'Ava White', 'MNO Enterprises', 5),
    ('william@example.com', 'William Davis', 'PQR Co.', NULL),
    ('olivia@example.com', 'Olivia Martinez', NULL, 2),
    ('logan@example.com', 'Logan Anderson', 'STU Corporation', 3),
    ('sofia@example.com', 'Sofia Wilson', NULL, 2),
    ('avery@example.com', 'Avery Johnson', 'VWX Ltd', NULL),
    ('lucas@example.com', 'Lucas Taylor', 'YZ Corp', 4),
    ('amelia@example.com', 'Amelia Brown', NULL, 2),
    ('henry@example.com', 'Henry Davis', 'ABC Company', NULL),
    ('ella@example.com', 'Ella Anderson', 'XYZ Corporation', 3),
    ('benjamin@example.com', 'Benjamin Garcia', NULL, 2),
    ('harper@example.com', 'Harper Hernandez', '123 Industries', NULL),
    ('jackson@example.com', 'Jackson Wilson', 'GHI Ltd', 4),
    ('scarlett@example.com', 'Scarlett Thompson', NULL, 1),
    ('sebastian@example.com', 'Sebastian Lewis', 'JKL Corporation', NULL),
    ('abigail@example.com', 'Abigail White', 'MNO Enterprises', 5),
    ('lily@example.com', 'Lily Davis', 'PQR Co.', NULL),
    ('owen@example.com', 'Owen Martinez', NULL, 2),
    ('zoey@example.com', 'Zoey Anderson', 'STU Corporation', 3),
    ('luke@example.com', 'Luke Wilson', NULL, 2),
    ('mila@example.com', 'Mila Johnson', 'VWX Ltd', NULL),
    ('gabriel@example.com', 'Gabriel Taylor', 'YZ Corp', 4),
    ('ella@example.com', 'Ella Brown', NULL, 2),
    ('dylan@example.com', 'Dylan Davis', 'ABC Company', NULL),
    ('hailey@example.com', 'Hailey Anderson', 'XYZ Corporation', 3),
    ('jacob@example.com', 'Jacob Garcia', NULL, 2),
    ('violet@example.com', 'Violet Hernandez', '123 Industries', NULL),
    ('levi@example.com', 'Levi Wilson', 'GHI Ltd', 4),
    ('sophie@example.com', 'Sophie Thompson', NULL, 1),
    ('samuel@example.com', 'Samuel Lewis', 'JKL Corporation', NULL),
    ('camila@example.com', 'Camila White', 'MNO Enterprises', 5),
    ('hannah@example.com', 'Hannah Davis', 'PQR Co.', NULL),
    ('nathan@example.com', 'Nathan Martinez', NULL, 2),
    ('zoe@example.com', 'Zoe Anderson', 'STU Corporation', 3);
    """
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    else:
        print("Insert residents successfully!")
        conn.close()


if __name__ == "__main__":
    insert_resident()