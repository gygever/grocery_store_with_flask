from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    order = db.relationship('Orders', backref='users', uselist=False)

    def get_id(self):
        return self.userid


class Product(db.Model):
    productid = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_product = db.relationship('Order_item', backref='product', uselist=False)


class Orders(db.Model):
    orderid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'))
    order_item = db.relationship('Order_item', backref='orders', uselist=False)


class Order_item(db.Model):
    itemid = db.Column(db.BigInteger, primary_key=True)
    productid = db.Column(db.Integer, db.ForeignKey('product.productid'))
    orderid = db.Column(db.Integer, db.ForeignKey('orders.orderid'))
