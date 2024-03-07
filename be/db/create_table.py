import mysql.connector

conn = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    user="root",
    password="H16HaFd5-cb4dAd1dFGdBa2c1-22Cb2-",
    database="railway",
    port=15826
)

# Tạo một đối tượng cursor
cursor = conn.cursor()

# Câu lệnh SQL để tạo bảng User
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    user_type ENUM('admin', 'customer') NOT NULL
);
"""

# Thực thi câu lệnh tạo bảng
cursor.execute(create_table_query)
print(f"Tạo bảng user thành công!!")


create_category_table_query = """
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id NVARCHAR(255),
    name NVARCHAR(255),
    image LONGBLOB
)
"""

cursor.execute(create_category_table_query)
print(f"Tạo bảng category thành công!!!")


create_address_table_query = """
CREATE TABLE IF NOT EXISTS address (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT, 
    address NVARCHAR(255),
    status BOOLEAN
)
"""
cursor.execute(create_address_table_query)
print(f"Tạo bảng address thành công!!")

create_cart_order_table_query = """
CREATE TABLE IF NOT EXISTS cart_order (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    price DECIMAL(15, 2),
    paid_status BOOLEAN,
    order_date DATETIME,
    product_status ENUM('Processing', 'Shipped', 'Delivered')
)
"""
cursor.execute(create_cart_order_table_query)
print("Tạo bảng card_order thành công!")


create_cart_order_item_table_query = """
CREATE TABLE IF NOT EXISTS cart_order_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    invoive_no NVARCHAR(255),
    product_status NVARCHAR(255),
    item NVARCHAR(255),
    image LONGBLOB,
    qty INT,
    price DECIMAL(15, 2),
    total DECIMAL(15, 2)
)
""" 
cursor.execute(create_cart_order_item_table_query)
print("Tạo bảng card_order_item thành công!")


create_product_table_query = """
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id NVARCHAR(255),
    user_id INT, 
    category_id INT,
    vendor_id INT,
    name NVARCHAR(255),
    image LONGBLOB,
    description NVARCHAR(255),
    price DECIMAL(15, 2),
    old_price DECIMAL(15, 2),
    specifications NVARCHAR(255),
    type NVARCHAR(255),
    stock_count INT,
    life DATETIME, 
    mfd NVARCHAR(255),
    product_status ENUM('Draft', 'Disabled', 'Rejected', 'In Review', 'Published'),
    featured BOOLEAN,
    status BOOLEAN,
    digital BOOLEAN,
    sku NVARCHAR(255),
    created_at DATETIME,
    updated_at DATETIME
)
"""
cursor.execute(create_product_table_query)
print(f"Tạo bảng products thành công!")


create_product_review_table_query = """
CREATE TABLE IF NOT EXISTS product_review (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    review NVARCHAR(255),
    rating ENUM('★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★'),
    date DATETIME
)
"""
cursor.execute(create_product_review_table_query)
print(f"Tạo bảng product_review thành công!")


create_vendor_table_query = """
CREATE TABLE IF NOT EXISTS vendors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_id NVARCHAR(255),
    image LONGBLOB,
    description NVARCHAR(255),
    user_id INT,
    address NVARCHAR(255),
    contact NVARCHAR(255),
    date DATETIME
)
"""
cursor.execute(create_vendor_table_query)
print(f"Tạo bảng vendors thành công!")


create_wishlist_table_query = """
CREATE TABLE IF NOT EXISTS wishlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    date DATETIME
)
"""
cursor.execute(create_wishlist_table_query)
print(f"Tạo bảng wishlist thành công!")



# Commit các thay đổi vào cơ sở dữ liệu
conn.commit()

# Đóng kết nối
cursor.close()
conn.close()