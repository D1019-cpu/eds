from db.db import execute_query
from models.address import Address


def create_address(address: Address):
    query = "INSERT INTO addresses (user_id, address, status) VALUES (%s, %s, %s)"
    params = (address.user_id, address.address, address.status)
    execute_query(query, params)


def get_address_by_user_id(user_id: int) -> Address:
    query = "SELECT user_id, address, status FROM addresses WHERE user_id = %s"
    params = (user_id,)
    execute_query(query, params)


def get_address_by_address(address: str) -> Address:
    query = "SELECT user_id, address, status FROM addresses WHERE address = %s"
    params = (address,)
    execute_query(query, params)


def get_all_addresses():
    query = "SELECT user_id, address, status FROM addresses"
    execute_query(query)


def update_address(user_id: int, address_data: Address):
    query = "UPDATE addresses SET address = %s, status = %s WHERE user_id = %s"
    params = (address_data.address, address_data.status, user_id)
    execute_query(query, params)


def delete_address(user_id: int):
    query = "DELETE FROM addresses WHERE user_id = %s"
    params = (user_id,)
    execute_query(query, params)
