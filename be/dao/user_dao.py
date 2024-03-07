from typing import List 
from db.db import execute_query 
from models.user import User 


def create_user(user: User):
    query = "INSERT INTO users (username, email, password, user_type) VALUES (%s, %s, %s, %s)"
    params = (user.username, user.email, user.password, user.user_type.value)
    execute_query(query, params)


def get_user_by_id(user_id: int) -> User:
    try:
        query = "SELECT * FROM users WHERE id = %s"
        params = (user_id, )
        result = execute_query(query, params)
        user_data = result.fetchone()
        if user_data:
            return User(**user_data)
        else:
            return None
    except Exception as e:
        print(f"Lỗi khi trích xuất user by ID = {user_id}, {e}")
        return None 


def get_user_by_email(email: str) -> User:
    try:
        query = "SELECT * FROM users WHERE email = %s"
        params = (email, )
        result = execute_query(query, params)
        user_data = result.fetchone()
        print(user_data)
        if user_data:
            return User(
                username=user_data[1],
                email=user_data[2],
                password=user_data[3],
                user_type=user_data[4]
            )
        else:
            return False 
    except Exception as e:
        print(f"Lỗi khi trích xuất user by Email = {email}, {e}")
        return False 


def check_email_is_exits(email: str) -> bool:
    try:
        query = "SELECT * FROM users WHERE email = %s"
        params = (email, )
        result = execute_query(query, params)
        user_data = result.fetchone()
        if user_data:
            return True 
        else:
            return False 
    except Exception as e:
        return False 


def get_user_by_username(username: str) -> User:
    try:
        query = "SELECT * FROM users WHERE username = %s"
        params = (username, )
        result = execute_query(query, params)
        user_data = result.fetchone()
        if user_data:
            return User(**user_data)
        else:
            return False 
    except Exception as e:
        print(f"Lỗi khi trích xuất user by Username  = {username}, {e}")
        return False 


def check_username_is_exits(username: str) -> bool:
    try:
        query = "SELECT * FROM users WHERE username = %s"
        params = (username, )
        result = execute_query(query, params)
        user_data = result.fetchone()
        if user_data:
            return True
        else:
            return False 
    except Exception as e:
        return False


def get_all_users() -> List[User]:
    try:
        query = "SELECT * FROM users"
        result = execute_query(query)
        user_data = result.fetchall()
        return [User(**user) for user in user_data] 
    except Exception as e:
        print(f"Lỗi khi trích xuất tất cả user, {e}")
        return []


def update_user(user_id: int, new_user_data: User):
    query = "UPDATE users GET username = %s, email = %s, password = %s, user_type = %s WHERE id  = %s"
    params = (new_user_data.username, new_user_data.email, new_user_data.password, new_user_data.user_type.value, user_id)
    execute_query(query, params)


def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id = %s"
    params = (user_id, )
    execute_query(query, params)
