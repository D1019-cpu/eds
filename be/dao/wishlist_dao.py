from db.db import execute_query
from models.wishlist import Wishlist


def add_to_wishlist(wishlist_item: Wishlist):
    query = "INSERT INTO wishlist (user_id, product_id, date) VALUES (%s, %s, %s)"
    params = (wishlist_item.user_id, wishlist_item.product_id, wishlist_item.date)
    execute_query(query, params)


def remove_from_wishlist(user_id: int, product_id: int):
    query = "DELETE FROM wishlist WHERE user_id = %s AND product_id = %s"
    params = (user_id, product_id)
    execute_query(query, params)


def get_wishlist_by_user_id(user_id: int):
    query = "SELECT user_id, product_id, date FROM wishlist WHERE user_id = %s"
    params = (user_id,)
    execute_query(query, params)


def is_in_wishlist(user_id: int, product_id: int) -> bool:
    query = "SELECT EXISTS(SELECT 1 FROM wishlist WHERE user_id = %s AND product_id = %s)"
    params = (user_id, product_id)
    result = execute_query(query, params)
    return result.fetchone()[0]


def clear_wishlist(user_id: int):
    query = "DELETE FROM wishlist WHERE user_id = %s"
    params = (user_id,)
    execute_query(query, params)
