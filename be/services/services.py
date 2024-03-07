from models.product import Product
from models.category import Category
from models.product import ProductReview
from models.vendor import Vendor
from business.business import ProductService, ProductReviewService, VendorService, CategoryService
from fastapi import HTTPException, UploadFile, File
from typing import List

from fastapi import FastAPI, status, Path, Header, HTTPException
from models.user import User 
from business.business import UserService, CategoryService, SECRET_KEY
import jwt 
from fastapi import Query


app = FastAPI()
user_uservice = UserService()
category_service = CategoryService()


product_service = ProductService()
product_review_service = ProductReviewService()
vendor_service = VendorService()
category_service = CategoryService()


@app.post("/api/register/")
def register_user(user: User):
    res = user_uservice.register_user(user)
    if res is not None:
        # print(res['success'])
        if res['success'] == True:
            return {
                'message': res['message'],
                'status': 201,
            }, status.HTTP_201_CREATED
        else:
            return {
                'message': res['message'],
                'status': 409,
            }, status.HTTP_409_CONFLICT
    else:
        return {
            'message': 'Lỗi xảy ra trong quá trình đăng ký',
            'status': 405
        }, status.HTTP_405_METHOD_NOT_ALLOWED
    

@app.post("/api/login/")
def login_user(email: str, password: str):
    res = user_uservice.login_user(email, password)
    if res is not None:
        return {
            'message': 'Đăng nhập thành công!!',
            'token': res['token']
        } 
    else:
        return {
            'message': 'Email không tồn tại hoặc password không đúng!!!'
        }


@app.post("/products/", status_code=201)
def create_product(product: Product, authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_type = payload.get('user_type')
        if user_type != "admin":
            raise HTTPException(status_code=403, detail="Only admin can create products!")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
        
    return product_service.create_product(product)


@app.get("/products/{id}", response_model=Product)
def get_product_by_id(id: int = Path(...)):
    product = product_service.get_product_by_id(id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@app.put("/products/{id}", response_model=Product)
def update_product_by_id(product: Product, id: int = Path(...)):
    return product_service.update_product(id, product)


@app.delete("/products/{id}")
def delete_product_by_id(id: int = Path(...)):
    product_service.delete_product(id)
    return {"message": "Product deleted successfully"}


@app.post("/categories/", status_code=201)
def create_category(category_name: str, image: UploadFile = File(...), authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_type = payload.get('user_type')
        if user_type != "admin":
            raise HTTPException(status_code=403, detail="Only admin can create categories!")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return category_service.create_category(category_name, image)


@app.get("/categories/{id}", response_model=Category)
def get_category_by_id(id: int = Path(...)):
    category = category_service.get_category_by_id(id)
    if category:
        return category
    else:
        raise HTTPException(status_code=404, detail="Category not found")


@app.put("/categories/{id}", response_model=Category)
def update_category_by_id(category_name: str, id: int = Path(...), image: UploadFile = File(...)):
    return category_service.update_category(id, category_name, image)


@app.delete("/categories/{id}")
def delete_category_by_id(id: int = Path(...)):
    category_service.delete_category(id)
    return {"message": "Category deleted successfully"}


@app.post("/product_reviews/", status_code=201)
def create_product_review(product_review: ProductReview):
    return product_review_service.create_product_review(product_review)


@app.get("/product_reviews/{id}", response_model=ProductReview)
def get_product_review_by_id(id: int = Path(...)):
    product_review = product_review_service.get_product_review_by_id(id)
    if product_review:
        return product_review
    else:
        raise HTTPException(status_code=404, detail="Product review not found")


@app.put("/product_reviews/{id}", response_model=ProductReview)
def update_product_review_by_id(product_review: ProductReview, id: int = Path(...)):
    return product_review_service.update_product_review(id, product_review)


@app.delete("/product_reviews/{id}")
def delete_product_review_by_id(id: int = Path(...)):
    product_review_service.delete_product_review(id)
    return {"message": "Product review deleted successfully"}


@app.post("/vendors/", status_code=201)
def create_vendor(vendor: Vendor):
    return vendor_service.create_vendor(vendor)


@app.get("/vendors/{id}", response_model=Vendor)
def get_vendor_by_id(id: int = Path(...)):
    vendor = vendor_service.get_vendor_by_id(id)
    if vendor:
        return vendor
    else:
        raise HTTPException(status_code=404, detail="Vendor not found")


@app.put("/vendors/{id}", response_model=Vendor)
def update_vendor_by_id(vendor: Vendor, id: int = Path(...)):
    return vendor_service.update_vendor(id, vendor)


@app.delete("/vendors/{id}")
def delete_vendor_by_id(id: int = Path(...)):
    vendor_service.delete_vendor(id)
    return {"message": "Vendor deleted successfully"}


@app.get("/product/")
def get_products_paginated(page: int = Query(1, gt=0), page_size: int = Query(10, gt=0), category_id: str = None, vendor_id: str = None, min_price: float = None, max_price: float = None):
    products = product_service.get_products_paginated(page, page_size, category_id, vendor_id, min_price, max_price)
    return products

