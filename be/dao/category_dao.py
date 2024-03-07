from db.db import execute_query 
from models.category import Category 


def create_category(category: Category):
    query = "INSERT INTO categories (category_id, name, image) VALUES (%s, %s, %s)"
    params = (category.category_id, category.name, category.image)
    execute_query(query, params)


def get_category_by_id(id: int) -> Category:
    query = "SELECT id, category_id, name, image FROM categories WHERE id = %s"
    params = (id, )
    execute_query(query, params)


def get_category_by_category_id(category_id: str) -> Category:
    query = "SELECT id, category_id, name, image FROM categories WHERE category_id = %s"
    params = (category_id, )
    execute_query(query, params)


def get_category_by_name(name: str) -> Category:
    try:
        query = "SELECT category_id, name, image FROM categories WHERE name = %s"
        params = (name, )
        result = execute_query(query, params) 
        category_data = result.fetchone()
        if category_data:
            return Category(**category_data)
        else:
            return None 
    except Exception as e:
        print(f"Lỗi: {e}")
        return None 


def get_all_categories():
    query = "SELECT id, category_id, name, image FROM categories"
    execute_query(query)


def update_category(id: int, category_data: Category):
    query = "UPDATE category SET name = %s, image = %s WHERE id = %s"
    params = (category_data.name, category_data.image, category_data.id)
    execute_query(query, params)


def deltete_category(id: int):
    query = "DELETE FROM categories WHERE id = %s"
    params = (id, )
    execute_query(query, params)
