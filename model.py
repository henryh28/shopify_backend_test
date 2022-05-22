""" Models definitions """

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# =============== Model definitions ===================

# Association table for Warehouse & Items
warehouse_items = db.Table('warehouse_items', 
    db.Column('warehouse_id', db.Integer, db.ForeignKey('warehouses.warehouse_id')),
    db.Column('item_id', db.Integer, db.ForeignKey('items.item_id'))
)


class Warehouse (db.Model):
    """ Define a Warehouse """
    __tablename__ = 'warehouses'

    warehouse_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    address = db.Column(db.String)
    current_capacity = db.Column(db.Integer)
    max_capacity = db.Column(db.Integer)
    description = db.Column(db.String)

    # items = lists all items assigned to this warehouse

    #inventory = db.relationship('Item', secondary = warehouse_items, backref = 'location')
    inventory = db.relationship('Item', secondary=warehouse_items, back_populates='warehouse')

    def __repr__(self):
        """ Returns warehouse info """
        return (f"< Warehouse warehouse_id: {self.warehouse_id} | address: {self.address} | description: {self.description} >")


class Item (db.Model):
    """ Define an Item """
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sku = db.Column(db.Integer)
    name = db.Column(db.String)
    department = db.Column(db.String)
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    description = db.Column(db.String)

    # warehouse: Warehouse(s) that this Inventory item belongs to

    # items = db.relationship('Item', secondary = warehouse_items, backref = 'warehouse')
    warehouse = db.relationship('Warehouse', secondary=warehouse_items, back_populates='inventory')

    def __repr__(self):
        """ Returns Item info """
        return (f"< Item item_id: {self.item_id} | sku: {self.sku} | name: {self.name} | department: {self.department} | quantity: {self.quantity} | unit_price: {self.unit_price} | description: {self.description}> | warehouse: {self.warehouse} ")




# ================== Utility functions ===================

def connect_to_db(flask_app, db_uri = "postgresql:///shopify", echo = True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print ("   >>>>>>>>>>> Database Connected <<<<<<<<<<   ")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)


