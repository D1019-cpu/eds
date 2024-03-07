import mysql.connector 


# Hàm kết nối với MySQl
def connect_to_mysql():
    return mysql.connector.connect(
        host="roundhouse.proxy.rlwy.net",
        user="root",
        password="H16HaFd5-cb4dAd1dFGdBa2c1-22Cb2-",
        database="railway",
        port=15826
    )


# Các hàm truy vấn
def execute_query(query, params=None):
    conn = connect_to_mysql()
    cursor = conn.cursor(buffered=True)
    cursor.execute(query, params)
    conn.commit()
    conn.close()
    return cursor 


def drop_all_tables():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")

    for table in cursor.fetchall():
        table_name = table[0]
        drop_query = f"DROP TABLE {table_name}"
        cursor.execute(drop_query)
    
    conn.commit()
    conn.close()
    print("Đã xóa tất cả các bảng trong database!!")
    return cursor
