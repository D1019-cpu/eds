from db.db import execute_query
from models.vendor import Vendor


def create_vendor(vendor: Vendor):
    query = "INSERT INTO vendors (vendor_id, name, image, description, user_id, address, contact, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    params = (
        vendor.vendor_id,
        vendor.name,
        vendor.image,
        vendor.description,
        vendor.user_id,
        vendor.address,
        vendor.contact,
        vendor.date
    )
    execute_query(query, params)


def get_vendor_by_id(id: int) -> Vendor:
    query = "SELECT vendor_id, name, image, description, user_id, address, contact, date FROM vendors WHERE id = %s"
    params = (id,)
    execute_query(query, params)


def get_vendor_by_vendor_id(vendor_id: str) -> Vendor:
    query = "SELECT vendor_id, name, image, description, user_id, address, contact, date FROM vendors WHERE vendor_id = %s"
    params = (vendor_id,)
    execute_query(query, params)


def get_vendor_by_name(name: str) -> Vendor:
    try:
        query = "SELECT vendor_id, name, image, description, user_id, address, contact, date FROM vendors WHERE name = %s"
        params = (name,)
        result = execute_query(query, params)
        vendor_data = result.fetchone()
        if vendor_data:
            return Vendor(**vendor_data)
        else:
            return None
    except Exception as e:
        print(f"Lỗi: {e}")
        return None


def get_all_vendors():
    query = "SELECT vendor_id, name, image, description, user_id, address, contact, date FROM vendors"
    execute_query(query)


def update_vendor(id: int, vendor_data: Vendor):
    query = "UPDATE vendors SET name = %s, image = %s, description = %s, user_id = %s, address = %s, contact = %s, date = %s WHERE id = %s"
    params = (
        vendor_data.name,
        vendor_data.image,
        vendor_data.description,
        vendor_data.user_id,
        vendor_data.address,
        vendor_data.contact,
        vendor_data.date,
        id
    )
    execute_query(query, params)


def delete_vendor(id: int):
    query = "DELETE FROM vendors WHERE id = %s"
    params = (id,)
    execute_query(query, params)
