from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    cates = dao.load_categories()
    prod = dao.load_products(q =q, cate_id = cate_id)
    return render_template("index.html" ,  cates = cates, prod = prod)

@app.route("/products/<int:id>")
def details(id):
    return render_template("products-details.html", prod = dao.get_product_by_id(id))

if __name__== "__main__":
    with app.app_context():
        app.run(debug=True)