from flask import Flask, jsonify

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


if __name__=='__main__':
    app.run(debug=True, port=3000)

