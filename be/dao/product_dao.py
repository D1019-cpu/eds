from db.db import execute_query
from models.product import Product, Status
from models.product import ProductReview, Rating
from typing import List

def create_product(product: Product):
    query = """
        INSERT INTO products (
            product_id, user_id, category_id, vendor_id, name, image, description, 
            price, old_price, specifications, type, stock_count, life, mfd, 
            product_status, featured, status, digital, sku, created_at, updated_at
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        product.product_id, product.user_id, product.category_id, product.vendor_id, product.name, 
        product.image, product.description, product.price, product.old_price, product.specifications, 
        product.type, product.stock_count, product.life, product.mfd, product.product_status.value, 
        product.featured, product.status, product.digital, product.sku, product.created_at, product.updated_at
    )
    execute_query(query, params)

def get_product_by_id(product_id: str) -> Product:
    query = "SELECT * FROM products WHERE product_id = %s"
    params = (product_id,)
    result = execute_query(query, params)
    product_data = result.fetchone()
    if product_data:
        return Product(**product_data)
    else:
        return None

def get_all_products() -> List[Product]:
    query = "SELECT * FROM products"
    result = execute_query(query)
    products = []
    for product_data in result:
        products.append(Product(**product_data))
    return products

def update_product(product_id: str, new_product_data: Product):
    query = """
        UPDATE products SET 
        user_id = %s, category_id = %s, vendor_id = %s, name = %s, image = %s, description = %s, 
        price = %s, old_price = %s, specifications = %s, type = %s, stock_count = %s, life = %s, 
        mfd = %s, product_status = %s, featured = %s, status = %s, digital = %s, sku = %s, 
        updated_at = %s 
        WHERE product_id = %s
    """
    params = (
        new_product_data.user_id, new_product_data.category_id, new_product_data.vendor_id, new_product_data.name, 
        new_product_data.image, new_product_data.description, new_product_data.price, new_product_data.old_price, 
        new_product_data.specifications, new_product_data.type, new_product_data.stock_count, new_product_data.life, 
        new_product_data.mfd, new_product_data.product_status.value, new_product_data.featured, new_product_data.status, 
        new_product_data.digital, new_product_data.sku, new_product_data.updated_at, product_id
    )
    execute_query(query, params)

def delete_product(product_id: str):
    query = "DELETE FROM products WHERE product_id = %s"
    params = (product_id,)
    execute_query(query, params)

def create_product_review(review: ProductReview):
    query = "INSERT INTO product_reviews (user_id, product_id, review, rating, date) VALUES (%s, %s, %s, %s, %s)"
    params = (review.user_id, review.product_id, review.review, review.rating.value, review.date)
    execute_query(query, params)

def get_product_review_by_id(review_id: int) -> ProductReview:
    query = "SELECT * FROM product_reviews WHERE id = %s"
    params = (review_id,)
    result = execute_query(query, params)
    review_data = result.fetchone()
    if review_data:
        return ProductReview(**review_data)
    else:
        return None

def update_product_review(review_id: int, new_review_data: ProductReview):
    query = "UPDATE product_reviews SET review = %s, rating = %s, date = %s WHERE id = %s"
    params = (new_review_data.review, new_review_data.rating.value, new_review_data.date, review_id)
    execute_query(query, params)

def delete_product_review(review_id: int):
    query = "DELETE FROM product_reviews WHERE id = %s"
    params = (review_id,)
    execute_query(query, params)


def get_products_paginated(page: int = 1, page_size: int = 10, category_id: str = None, vendor_id: str = None, min_price: float = None, max_price: float = None) -> List[Product]:
    offset = (page - 1) * page_size
    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if category_id:
        query += " AND category_id = %s"
        params.append(category_id)
    if vendor_id:
        query += " AND vendor_id = %s"
        params.append(vendor_id)
    if min_price is not None:
        query += " AND price >= %s"
        params.append(min_price)
    if max_price is not None:
        query += " AND price <= %s"
        params.append(max_price)

    query += " LIMIT %s OFFSET %s"
    params.extend([page_size, offset])

    result = execute_query(query, params)
    products = []
    for product_data in result:
        products.append(Product(**product_data))
    return products
