""" Define CRUD operations for models """

from model import db, Warehouse, warehouse_items, Item, connect_to_db

# ========== Warehouse related functions ==========

def create_warehouse(address, current_capacity, max_capacity, description):
    """ Create and return a new warehouse """
    return Warehouse(address=address, current_capacity=current_capacity, max_capacity=max_capacity, description=description)

def get_all_warehouse():
    """ Returns a list of all Warehouses in database """
    return Warehouse.query.all()


def get_warehouse_by(**data):
    """ Search for and return a warehouse by specified parameters """
    return Warehouse.query.filter_by(**data).first()

# ========== Item related functions ==========

def create_item(sku, name, department, quantity, unit_price, description):
    """ Create and return a new Item """

    return Item(sku=sku, name=name, department=department, quantity=quantity, unit_price=unit_price, description=description)


def get_all_items():
    """ Returns a list of all items in database """
    return Item.query.all()


def get_item_by(**data):
    """ Search for and return an item by specified parameters """
    return Item.query.filter_by(**data).first()


def update_item(**data):
    """ Update attributes of selected item """

    item=get_item_by(item_id=data['item_id'])

    for key, value in data.items():
        setattr(item, key, value)

    db.session.commit()
    db.session.flush()

