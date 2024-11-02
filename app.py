from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data produk kecantikan
beauty_products = [
    {
        "id": 1,
        "name": "Serum Wajah Vitamin C",
        "description": "Serum wajah dengan kandungan vitamin C untuk mencerahkan kulit.",
        "price": 200,  # dalam ribuan
        "address": "Jl. Kebon Jeruk No.10, Jakarta"
    },
    {
        "id": 2,
        "name": "Moisturizer Gel Aloe Vera",
        "description": "Gel pelembab dengan ekstrak aloe vera untuk menyejukkan kulit.",
        "price": 150,  # dalam ribuan
        "address": "Jl. Tanah Abang No.20, Jakarta"
    },
    {
        "id": 3,
        "name": "Lipstik Matte",
        "description": "Lipstik dengan hasil akhir matte yang tahan lama.",
        "price": 120,  # dalam ribuan
        "address": "Jl. Sudirman No.15, Bandung"
    },
    {
        "id": 4,
        "name": "Face Mask Green Tea",
        "description": "Masker wajah dengan ekstrak green tea untuk kulit lebih segar.",
        "price": 50,  # dalam ribuan
        "address": "Jl. Malioboro No.50, Yogyakarta"
    },
    {
        "id": 5,
        "name": "Shampoo Anti Ketombe",
        "description": "Shampoo anti ketombe dengan bahan alami.",
        "price": 75,  # dalam ribuan
        "address": "Jl. Merdeka No.5, Surabaya"
    }
]

class BeautyProductList(Resource):
    def get(self):
        return jsonify(beauty_products)

class BeautyProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in beauty_products if p["id"] == product_id), None)
        if product:
            return jsonify(product)
        return {"message": "Product not found"}, 404

class AddBeautyProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": len(beauty_products) + 1,
            "name": data["name"],
            "description": data.get("description", "No description provided"),
            "price": data["price"],
            "address": data.get("address", "No address provided")
        }
        beauty_products.append(new_product)
        return jsonify(new_product)

class UpdateBeautyProduct(Resource):
    def put(self, product_id):
        product = next((p for p in beauty_products if p["id"] == product_id), None)
        if not product:
            return {"message": "Product not found"}, 404
        data = request.get_json()
        product.update(data)
        return jsonify(product)

class DeleteBeautyProduct(Resource):
    def delete(self, product_id):
        global beauty_products
        beauty_products = [p for p in beauty_products if p["id"] != product_id]
        return {"message": "Product deleted successfully"}

# Menambahkan resource ke API
api.add_resource(BeautyProductList, '/beauty-products')
api.add_resource(BeautyProductDetail, '/beauty-products/<int:product_id>')
api.add_resource(AddBeautyProduct, '/beauty-products/add')
api.add_resource(UpdateBeautyProduct, '/beauty-products/update/<int:product_id>')
api.add_resource(DeleteBeautyProduct, '/beauty-products/delete/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)

api.add_resource(DeleteBatikProduct, '/batik-products/delete/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
