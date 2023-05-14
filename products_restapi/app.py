from flask import Flask, jsonify, request

app =Flask(__name__)

from products import products

#El metodo get no es necesario escribirlo ya que si no tiene ningun metodo especificado
# el servidor da por echo que es una peticion get
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message":"pong"})

@app.route('/products')
def get_products():
    return jsonify({"products":products, "message":"Products list"})

@app.route('/products/<string:product_name>')
def get_product(product_name):
    product_found=[product for product in products if product['name']==product_name]
    print(product_found)
    if (len(product_found)>0):
        return jsonify({"product": product_found[0], "message":"Product found"})
    else:
        return jsonify({"Message":"Product not found"})
    
@app.route('/products', methods=['POST'])
def add_product():
    print(request.json)
    new_products ={
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity":request.json['quantity']
    }
    products.append(new_products)
    return jsonify({"message":"product added succesfully",
                    "products":products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    product_found= [product for product in products if product['name']== product_name]
    if(len(product_found)>0):
        product_found[0]['name']=request.json['name']
        product_found[0]['price']=request.json['price']
        product_found[0]['quantity']=request.json['quantity']
        return jsonify({"message":"Product edited succesfully",
                        "product_found":product_found[0]})
    else:
        return jsonify({"Message":"product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    product_found= [product for product in products if product['name']== product_name]
    if (len(product_found)>0):
        products.remove(product_found[0])
        return jsonify({"message":"product removed succesfully",
                        "products":products})
    else:
        return jsonify({"message":"Product not found"})


if __name__=='__main__':
    app.run(debug=True, port=3000)

