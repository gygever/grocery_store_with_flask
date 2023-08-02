from flask import Flask, render_template, url_for, request, flash, redirect
from model import db, Users, Product, Orders, Order_item
from config.config import DATABASE_URI, SECRET_KEY
from flask_login import LoginManager, current_user, login_user, logout_user

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.secret_key = SECRET_KEY
db.init_app(app)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def index():
    products = Product.query.order_by(Product.productid.desc()).all()
    return render_template('index.html', products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            user = Users.query.filter_by(username=username).first()
            if user is None or password != user.password:
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user)
            flash('Login successfully')
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out!')
        return redirect(url_for('index'))
    else:
        flash("You aren't login")
        return redirect(url_for('login'))


@app.route('/sign_up', methods=['GET', 'POST'])
def sing_up():
    if current_user.is_authenticated:
        return redirect(url_for('show'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            if Users.query.filter_by(username=username).first():
                flash(f'Username {username} not available')
                return redirect(url_for('sign_up'))
            if len(password) < 8:
                flash('The password too short, min length 8')
                return redirect(url_for('sign_up'))
            else:
                user = Users(username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
    return render_template('sign_up.html')


@app.route('/order', methods=['POST', 'GET'])
def order():
    if current_user.is_authenticated:
        if request.method == 'POST':
            form = request.form
            order_product = []
            for key in form.keys():
                product = Product.query.filter_by(productid=key).first()
                if product.quantity >= int(form[key]) > 0:
                    order_product.append(product)
                elif int(form[key]) != 0:
                    flash(f'Wrong quantity of the product {product.productname}')
                    return redirect(url_for('index'))
            if order_product:
                order = Orders(userid=current_user.userid, price=0)
                db.session.add(order)
                db.session.commit()
                order_price = 0
                for or_prod in order_product:
                    productname = or_prod.productname
                    productid = or_prod.productid
                    orderid = order.orderid
                    quantity = int(form[str(or_prod.productid)])
                    price = or_prod.price * int(form[str(or_prod.productid)])
                    db.session.add(Order_item(productid=productid, orderid=orderid, quantity=quantity, price=price, productname=productname))
                    order_price += price
                    or_prod.quantity -= quantity
                order.price = order_price
                db.session.commit()
    else:
        flash("You aren't login")
        return redirect(url_for('login'))
    orders = Orders.query.filter_by(userid=current_user.userid).order_by(Orders.orderid.desc()).all()
    or_items = []
    for ord in orders:
        ord_items = Order_item.query.filter_by(orderid=ord.orderid).all()
        or_items.append(ord_items)
    return render_template('order.html', orders=orders, or_items=or_items)


if __name__ == '__main__':
    app.run(debug=True)
