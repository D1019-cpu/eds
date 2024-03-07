from dao.user_dao import create_user, check_email_is_exits, check_username_is_exits, get_user_by_email
from dao.category_dao import create_category, deltete_category, get_all_categories, get_category_by_id, get_category_by_name, update_category
from models.category import Category
from models.user import User, UserLoginForm 
from passlib.context import CryptContext
import jwt 
import secrets 
from datetime import datetime, timedelta
import uuid  
from dao.vendor_dao import create_vendor, get_vendor_by_id, update_vendor, delete_vendor
from dao.product_dao import create_product, get_product_by_id, update_product, delete_product
from models.vendor import Vendor
from models.product import Product
from dao.product_dao import create_product_review, get_product_review_by_id, update_product_review, delete_product_review
from models.product import ProductReview
from typing import List


SECRET_KEY = secrets.token_urlsafe(32)


# Phần quản lý tài khoản người dùng
class UserService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def register_user(self, user: User):
        try:
            existing_email = check_email_is_exits(user.email)
            existing_username = check_username_is_exits(user.username)
            if existing_email:
                return {
                    'message': "Email is already exist!!!",
                    'success': False
                }
            
            if existing_username:
                return {
                    'message': "Username is already exist!!!",
                    'success': False
                }

            hashed_password = self.pwd_context.hash(user.password)
            user.password = hashed_password

            create_user(user)

            return {
                'message': "User registered successfully!!!",
                'success': True
            }
        except Exception as e:
            print(f"Lỗi xảy ra trong khi đăng ký: {e}")
            return None
    

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)


    def login_user(self, user_form: UserLoginForm):
        user = get_user_by_email(user_form.email)
        if user and self.verify_password(user_form.password, user.password):
            jwt_payload = {
                'user_email': user.email,
                'username': user.username,
                'user_type': user.user_type.value,
                'exp': datetime.utcnow() + timedelta(days=1) # thời gian hết hạn của JWT
            }
            jwt_token = jwt.encode(jwt_payload, SECRET_KEY, algorithm='HS256')
            return {'token': jwt_token}
        else:
            return None 
        

    def update_user(self, user_id: int, new_user_data: User):
        pass 

    
    def delete_user(self, user_id: int):
        pass 

    
    def get_user_by_id(self, user_id: int):
        pass 


    def get_user_by_email(self, email: str):
        pass 


    def get_user_by_username(self, username: str):
        pass 


class CategoryService:
    def create_category(self, category_name: str, image: bytes):
        try:
            # Check if category name already exists
            existing_category = self.get_category_by_name(category_name)
            if existing_category:
                return {
                    'message': "Category already exists!",
                    'success': False
                }

            # Create the new category
            category_id = str(uuid.uuid4())
            new_category = Category(name=category_name, category_id=category_id, image=image)
            create_category(new_category)

            return {
                'message': "Category created successfully!",
                'success': True
            }
        except Exception as e:
            print(f"Error occurred while creating category: {e}")
            return None

    def get_category_by_id(self, category_id: int):
        return get_category_by_id(category_id)

    def get_all_categories(self):
        return get_all_categories()

    def update_category(self, category_id: int, new_category_name: str):
        try:
            category = self.get_category_by_id(category_id)
            if category:
                category.name = new_category_name
                update_category(category)
                return {
                    'message': "Category updated successfully!",
                    'success': True
                }
            else:
                return {
                    'message': "Category not found!",
                    'success': False
                }
        except Exception as e:
            print(f"Error occurred while updating category: {e}")
            return None

    def delete_category(self, category_id: int):
        try:
            category = self.get_category_by_id(category_id)
            if category:
                deltete_category(category)
                return {
                    'message': "Category deleted successfully!",
                    'success': True
                }
            else:
                return {
                    'message': "Category not found!",
                    'success': False
                }
        except Exception as e:
            print(f"Error occurred while deleting category: {e}")
            return None

    def get_category_by_name(self, category_name: str):
        # You'll need to implement this method in your category DAO
        pass 


class VendorService:
    def create_vendor(self, vendor: Vendor):
        return create_vendor(vendor)

    def get_vendor_by_id(self, vendor_id: int):
        return get_vendor_by_id(vendor_id)

    def update_vendor(self, vendor_id: int, new_vendor_data: Vendor):
        return update_vendor(vendor_id, new_vendor_data)

    def delete_vendor(self, vendor_id: int):
        return delete_vendor(vendor_id)


class ProductService:
    def create_product(self, product: Product):
        return create_product(product)

    def get_product_by_id(self, product_id: int):
        return get_product_by_id(product_id)

    def update_product(self, product_id: int, new_product_data: Product):
        return update_product(product_id, new_product_data)

    def delete_product(self, product_id: int):
        return delete_product(product_id)


class ProductReviewService:
    def create_product_review(self, product_review: ProductReview):
        return create_product_review(product_review)

    def get_product_review_by_id(self, review_id: int):
        return get_product_review_by_id(review_id)

    def update_product_review(self, review_id: int, new_review_data: ProductReview):
        return update_product_review(review_id, new_review_data)

    def delete_product_review(self, review_id: int):
        return delete_product_review(review_id)

    def get_products_paginated(self, page: int = 1, page_size: int = 10, category_id: str = None, vendor_id: str = None, min_price: float = None, max_price: float = None) -> List[Product]:
        return self.product_dao.get_products_paginated(page, page_size, category_id, vendor_id, min_price, max_price)
