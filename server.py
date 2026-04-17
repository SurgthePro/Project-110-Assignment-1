from flask import Flask # This format/syntax is different from ReactJS.
from flask import jsonify
from flask import request # This is needed in order to use the POST method--it's a method from Flask.
import uuid 
from flask_cors import CORS

app = Flask(__name__) # Instance of Flask (What's that? We only want to use app of Flask, so that we can use all the powers of Flask--there's a lot of hidden logic behind this code; _ _ name _ _ is all the Dunder method in Python), app is a variable name.
CORS(app, origins=["http://localhost:5173", "https://myapp.com"])

# GET http://127.0.0.1:5000/home
# Now we will create an endpoint (with the five steps):
@app.route("/home", methods= ["GET"]) # Decorator (which has lots of hidden logic) Step 1: @app.route, 2z: URL path, 3: methodp
def home(): # Step 4 function def
    return {"message": "Welcome to Flask cohort#65"} # Step 5 Here is where we indicate the respond we want--it's actually an object (python dictionary).
# Note: After running this on the cp terminal, then we click on ThunderClient, then click on New Request, then on the URL window there, we choose the method on the left and insert the URL path on the right of the method, then press "Send."
# GET http://127.0.0.1:5000/cohort-65 (This endpoint works with http://127.0.0.1:5000/home) GET is the method we are using.
# Now we are creating a new/different endpoint:
@app.route("/cohort-65", methods=["GET"])
def get_students_65():
    students_list = ["Sergio", "Leomar", "Charles", "Aymen","Dejanirra", "Freysy", "Trishon"]
    return students_list # Here, we are returning an array (list in Python) variable.
# Note: After running this on the cp terminal, then we click on ThunderClient, then click on New Request, then on the URL window there, we choose the method on the left and insert the URL path on the right of the method, then press "Send."

# ----- Path Parameters in Flask----- (They work similar to how a filter method works in React)
@app.route("/greet/<string:name>", methods=["GET"]) # Here, "/greet/" is the path.  Path parameters are wrapped in angle brackets (note: white spaces should be avoided).  String is the type & name is the parameter name. Note: The data type by default is a string--this means that you actually don't need to specify a string type, but you do for all other data types. Nevertheless, it's good practice to specify the data type so that inexperienced developers can understand your code.  The data type is what you're entering as a parameter and also the data type you want to be returned.
def say_hi(name): # The path parameter name also goes here always.
    return jsonify({"message": f"Hello {name}"}), 200 # ok (f is a python method--not a flask method)
# Note: After running this on the cp terminal, then we click on ThunderClient, then click on New Request, then on the URL window there, we choose the method on the left and insert the URL path on the right of the method (http://127.0.0.1:5000/greet/somenameorstringtitle), then press "Send."
@app.route("/api/users/<int:user_id>", methods=["GET"]) # Note: route is essentially a function with parameters.
def get_user_by_id(user_id):
    return jsonify({"This is the user id": user_id}), 200 # OK Note: jsonify is a method, so it always comes with a set of parentheses--avoid spaces.
# Note: After running this on the cp terminal, then we click on ThunderClient, then click on New Request, then on the URL window there, we choose the method on the left and insert the URL path on the right of the method, then press "Send."

#  ------ Products (It is a list of dictionaries)
products = [
  {
    "_id": 1, 
    "title": "Nintendo Switch", 
    "price": 499.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2, 
    "title": "Smart Refrigerator", 
    "price": 999.99, 
    "category": "Kitchen", 
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3, 
    "title": "Bluetooth Speaker", 
    "price": 79.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/3/300/300"
  },
]
product_id_counter = 3 # The length of the products list.

# The following is an endpoint for the products list above:
# GET URL path: http//127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])
def get_products():
    return {"data": products} # This time we are returning data from the products dictionary list--our goal this time is to return a specific product from the products list by its specific id integer number.
# GET URL path: http//127.0.0.1:5000/api/products/#
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    # return "Testing"
    # return {"product_id": product_id} Note: This works correctly, so now we can develop the logic.
    for product in products: # Here, we are trying to see every single product from the products list; therefore, we would use some type of python looping tool, such as a for loop; product is analogous to the i (index) in an array, and products is analogous to an arrayName in JS (this is a good reason why a python list or dictionary should be named with a plural name, so that we can refer to each of its elements in the singular form);
            # print(product)
            # return {"product_id": product_id}
            # But we want to specify to print only the id from each successive product:
            print(product["_id"])
            # But what if we want to specify a condition so that only if we find a specified id number, do we want that product printed out (displayed)?
            if product["_id"] == product_id:
                # return "I found the product."
              # return {"product_id": product_id}
                return jsonify({
              "success": True,
              "message": "Product retrieved successfully!",
              "data": product
            }), 200 # OK
        
    return jsonify ({
        "success": False,
        "message": "Product not found."
        }), 404 # Not Found

# This is a newly created ENDPOINT (with the POST method); here we are inserting a new product to our products list:
@app.route("/api/products", methods=["POST"])
def create_product():
    # return "working on it"
    # print(request.get_json())
    print(f"new product: {request.get_json()}") # Here, we are using the request method to have access to get_json(), this is the way to get JSON formatting from the request. ThunderClient will be sending the new product info. We are using python f-string (which is like template string--string interpolation).
    # We need to push the new product to our already existing list:
    new_product = request.get_json() # Here, whatever we are requesting, we are assigning it to a variable.
    # new_product["_id"] = len(products) + 1 # Note: This automatically creates a new product _id property and VALUE (the value is created on the right side fo the equation, and the new property (which is not included in the ThunderClient window for the data being POSTed) is added on the left side) for the new product (the user will not do this to avoid issues with multiple products with the same id, which would not be unique). Note: The logic on the right was created first, then it was assigned to a normal variable (with a property that is not included with the data being POSTED) The new_product is the variable_name for the entire object/dictionary being created in ThunderClient API POST request. This code has been replaced by a better option on the following line.
    new_product["_id"] = product_id_counter + 1 # This prevents the new product added from having the same id integer as another product.  
    product_id_counter +1
    # new_product["_id"] = uuid.uuid4() # uuid stands for (represents) hexadecimal numbers -4-4-8. This is a very long combination of strings, integers, and symbols. This can be used instead of the code directly above this code.
    products.append(new_product) # This is how we add/push a new product to the products list.
    return jsonify({
        "success": True,
        "message": "Product added successfully!",
        "data": new_product
    }), 201 # Created


# Put Method
# Basic Structure of the endpoint:
# @app.route("/api/products/<int:product_id>", methods=["PUT"])
# def update_product_by_id(product_id):
# logic of function
# return "Working on it"
@app.route("/api/products/<int:product_id>", methods=["PUT"]) # Note: With this method, in the request (with ThunderClient) we don't send the id to be updated/modified. Note: The path always begins with a forward slash inside the quotes.  
def update_product_by_id(product_id):
    updated_product = request.get_json() # The request method is the way we get the updated data from the API.  We get it in json format by using the method get_json()
    print(updated_product) # This displays the updated data in the cp terminal.
    for product in products: # If we have a thousdand products, this process will take a long time to complete, so before the for-loop, we need to have validation (are we getting those dictiionary properties?  If so, use the for-loop. If not, don't use the for-loop.)
        if product["_id"] == product_id: # If it finds the product you specified by id integer, the following intended code will be executed.
            product["title"] = updated_product["title"] # This tells the system that we want to override the current value to whatever we send it.
            product["price"] = updated_product["price"] # If you only want to change the price of the product, only include this line of code and omit the other lines.
            product["category"] = updated_product["category"]
            product["image"] = updated_product["image"]
            return jsonify({
                "success": True,
                "message": "Product updated successfully!",
                "data": product
            }), 200 # OK
    return jsonify({
        "success": False,
        "message": "Product not found."
        }), 404 # Not Found

# Delete Method Endpoint -- Use the following to create the skeleton for the endpoint:
# DELETE http://127.0.0.1:5000/api/products/
# def delete_product_by_id()
# return "working on it"
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product_by_id(product_id):
    for product in products: # Here, we use a python for-loop to search thru every element in the python products list.
        if product["_id"] == product_id: # Here, we use a conditional boolean statement so that if a product id value is equal to (matches) the id value input in the URL path (a path parameter), the following code instructions will be executed.
            products.remove(product) # delete product with that _id value from products & executute return function.
        # id_counter = product_id # This stores the id integer of the deleted product, so that when and if another product is added, it will be assigned a different id integer. Note: This code does not work bc the variable cannot be accessed globally by the create_product() function.
          #  return "I'm just before the return statement."
            return jsonify({
            "success": True,
            "message": (f"Product {product_id} deleted successfully!")
            }), 204 # No Content found anymore.
        
        return jsonify({
            "success": False,
            "message": (f"Product {product_id} not found.")
        }), 404 # Not Found

# -----  Coupons  -----
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2,"code": "SPOOKY25","discount": 25},
    {"_id": 3,"code": "VIP50","discount": 50}
] 
coupon_id_counter = 3

# GET  /api/coupons:
# GET URL path: http//127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return ({"data": coupons})

# GET /api/coupons/count
@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return ({"coupons_counter":len(coupons)})

# POST /api/coupons (The following endpoint adds a new coupon to the coupons list (however, this posted coupon will not be saved anywhere bc there's no database--we are not using a database yet in this course. Whenever you stop the program in the terminal--server, all memeory of the post is lost.):)
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    print(f"new coupon: {request.get_json()}")
    new_coupon = request.get_json()
    new_coupon["_id"] = coupon_id_counter + 1
    coupon_id_counter +1
    coupons.append(new_coupon)
    return jsonify({
        "success": True,
        "message": "Coupon added successfully!",
        "data": new_coupon
    }), 201 # Created

# GET /api/coupons/<int: id>
@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupon_by_id(coupon_id):
    for coupon in coupons:
        print(coupon["_id"])
        if coupon["_id"] == coupon_id: # If coupon id from the list is the same as the coupon passed as the argument, then return it.
            return jsonify({
              "success": True,
              "message": "Coupon retrieved successfully!",
              "data": coupon
            }), 200 # OK
        
    return jsonify ({
        "success": False,
        "message": "Coupon not found."
        }), 404 # Not Found

#  PUT /api/coupons/<int: id>
@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"]) # Note: With this method, in the request (with ThunderClient) we don't send the id to be updated/modified. Note: The path always begins with a forward slash inside the quotes.  
def update_coupon_by_id(coupon_id):
    updated_coupon = request.get_json() # The request method is the way we get the updated data from the API.  We get it in json format by using the method get_json()
    print(updated_coupon) # This displays the updated data in the cp terminal.
    for coupon in coupons: # If we have a thousdand products, this process will take a long time to complete, so before the for-loop, we need to have validation (are we getting those dictiionary properties?  If so, use the for-loop. If not, don't use the for-loop.)
        if coupon["_id"] == coupon_id: # If it finds the product you specified by id integer, the following intended code will be executed.
            coupon["code"] = updated_coupon["code"] # This tells the system that we want to override the current value to whatever we send it.
            coupon["discount"] = updated_coupon["discount"] # If you only want to change the price of the product, only include this line of code and omit the other lines.
            return jsonify({
                "success": True,
                "message": "Coupon updated successfully!",
                "data": coupon
            }), 200 # OK
    return jsonify({
        "success": False,
        "message": "Coupon not found."
        }), 404 # Not Found

# Delete Method Endpoint -- Use the following to create the skeleton for the endpoint:
# DELETE http://127.0.0.1:5000/api/coupons/
# def delete_coupon_by_id()
# return "working on it"
@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon_by_id(coupon_id):
    for coupon in coupons: # Here, we use a python for-loop to search thru every element in the python products list.
        if coupon["_id"] == coupon_id: # Here, we use a conditional boolean statement so that if a product id value is equal to (matches) the id value input in the URL path (a path parameter), the following code instructions will be executed.
            coupons.remove(coupon) # delete product with that _id value from products & executute return function.
        # id_counter = product_id # This stores the id integer of the deleted product, so that when and if another product is added, it will be assigned a different id integer. Note: This code does not work bc the variable cannot be accessed globally by the create_product() function.
          #  return "I'm just before the return statement."
            return jsonify({
            "success": True,
            "message": f"Product {coupon_id} deleted successfully!"
            }), 204 # No Content found anymore.
        
        return jsonify({
            "success": False,
            "message": f"Product {coupon_id} not found."
        }), 404 # Not Found


if __name__ == "__main__": # Note: We have double underscores here (four times). We should run the application after the system reads our endpoints--not before. Once the app is run, the endpoints that may be placed afterwards will not be read anymore.
    app.run(debug=True) # Here we are executing the app if the condition is met (true). We're going to execute the run method, and it's going to execute the application (which is the file).
 # When this file is run directly: __name__ == "__main__" (It means you're trying to execute the file directly--so it is true.) Name is gonna change to main bc you're trying to run this file directly.
 # When this file is imported as module: __name__ == "server.py" (If this is the case, the app will not run.)