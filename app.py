from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Data dummy untuk produk salon spa
products = [
    {
        "id": "1",
        "name": "Body Scrub",
        "price": 120000,
        "description": "Layanan body scrub untuk melembutkan kulit."
    },
    {
        "id": "2",
        "name": "Aromatherapy Massage",
        "price": 150000,
        "description": "Pijat aromaterapi untuk relaksasi."
    }
]

# Helper function untuk menemukan produk berdasarkan ID
def find_product(product_id):
    return next((product for product in products if product["id"] == product_id), None)

# Endpoint untuk mendapatkan daftar produk
class ProductList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(products),
            "products": products
        }

# Endpoint untuk mendapatkan detail produk berdasarkan ID
class ProductDetail(Resource):
    def get(self, product_id):
        product = find_product(product_id)
        if product:
            return {
                "error": False,
                "message": "success",
                "product": product
            }
        return {"error": True, "message": "Product not found"}, 404

# Endpoint untuk menambahkan produk baru
class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": str(len(products) + 1),
            "name": data.get("name"),
            "price": data.get("price"),
            "description": data.get("description")
        }
        products.append(new_product)
        return {
            "error": False,
            "message": "Product added",
            "product": new_product
        }

# Endpoint untuk memperbarui produk
class UpdateProduct(Resource):
    def put(self, product_id):
        data = request.get_json()
        product = find_product(product_id)
        if product:
            product["name"] = data.get("name", product["name"])
            product["price"] = data.get("price", product["price"])
            product["description"] = data.get("description", product["description"])
            return {
                "error": False,
                "message": "Product updated",
                "product": product
            }
        return {"error": True, "message": "Product not found"}, 404

# Endpoint untuk menghapus produk
class DeleteProduct(Resource):
    def delete(self, product_id):
        product = find_product(product_id)
        if product:
            products.remove(product)
            return {
                "error": False,
                "message": "Product deleted"
            }
        return {"error": True, "message": "Product not found"}, 404

# Menambahkan endpoint ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/product/<string:product_id>')
api.add_resource(AddProduct, '/product')
api.add_resource(UpdateProduct, '/product/<string:product_id>')
api.add_resource(DeleteProduct, '/product/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
