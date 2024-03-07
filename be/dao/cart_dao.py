from db.db import execute_query
from models.cart import CartOrder, CartOrderItem


def create_cart_order(cart_order: CartOrder):
    query = "INSERT INTO cart_orders (user_id, price, paid_status, order_date, product_status) VALUES (%s, %s, %s, %s, %s)"
    params = (
        cart_order.user_id,
        cart_order.price,
        cart_order.paid_status,
        cart_order.order_date,
        cart_order.product_status.value  # Chuyển đổi Enum thành giá trị chuỗi
    )
    execute_query(query, params)


def get_cart_order_by_id(order_id: int) -> CartOrder:
    query = "SELECT user_id, price, paid_status, order_date, product_status FROM cart_orders WHERE order_id = %s"
    params = (order_id,)
    execute_query(query, params)


def get_all_cart_orders():
    query = "SELECT order_id, user_id, price, paid_status, order_date, product_status FROM cart_orders"
    execute_query(query)


def update_cart_order(order_id: int, cart_order_data: CartOrder):
    query = "UPDATE cart_orders SET price = %s, paid_status = %s, order_date = %s, product_status = %s WHERE order_id = %s"
    params = (
        cart_order_data.price,
        cart_order_data.paid_status,
        cart_order_data.order_date,
        cart_order_data.product_status.value,  # Chuyển đổi Enum thành giá trị chuỗi
        order_id
    )
    execute_query(query, params)


def delete_cart_order(order_id: int):
    query = "DELETE FROM cart_orders WHERE order_id = %s"
    params = (order_id,)
    execute_query(query, params)


def create_cart_order_item(cart_order_item: CartOrderItem):
    query = "INSERT INTO cart_order_items (order_id, invoice_no, product_status, item, image, qty, price, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    params = (
        cart_order_item.order_id,
        cart_order_item.invoice_no,
        cart_order_item.product_status,
        cart_order_item.item,
        cart_order_item.image,
        cart_order_item.qty,
        cart_order_item.price,
        cart_order_item.total
    )
    execute_query(query, params)


def get_cart_order_item_by_id(order_item_id: int) -> CartOrderItem:
    query = "SELECT order_id, invoice_no, product_status, item, image, qty, price, total FROM cart_order_items WHERE order_item_id = %s"
    params = (order_item_id,)
    execute_query(query, params)


def get_cart_order_items_by_order_id(order_id: int):
    query = "SELECT order_item_id, order_id, invoice_no, product_status, item, image, qty, price, total FROM cart_order_items WHERE order_id = %s"
    params = (order_id,)
    execute_query(query, params)


def update_cart_order_item(order_item_id: int, cart_order_item_data: CartOrderItem):
    query = "UPDATE cart_order_items SET invoice_no = %s, product_status = %s, item = %s, image = %s, qty = %s, price = %s, total = %s WHERE order_item_id = %s"
    params = (
        cart_order_item_data.invoice_no,
        cart_order_item_data.product_status,
        cart_order_item_data.item,
        cart_order_item_data.image,
        cart_order_item_data.qty,
        cart_order_item_data.price,
        cart_order_item_data.total,
        order_item_id
    )
    execute_query(query, params)


def delete_cart_order_item(order_item_id: int):
    query = "DELETE FROM cart_order_items WHERE order_item_id = %s"
    params = (order_item_id,)
    execute_query(query, params)
