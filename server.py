""" Server for HackBright capstone project """

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import jinja2, crud, requests
import json

app = Flask(__name__)
app.secret_key = "temp"

# ================= General =================

# Homepage
@app.route ("/")
def homepage():
    """ Displays homepage """

    return render_template("index.html") 

# ================= Warehouse Related =================

@app.route ("/create_warehouse", methods = ["GET", "POST"])
def create_warehouse():
    """ Creates a warehouse """
    # GET method fetches a form for warehouse creation
    # POST method processes form to create a warehouse in DB

    if request.method == "GET":
        return render_template("create_warehouse.html")
    else:

        address = request.form['address']
        max_capacity = request.form['max_capacity']
        description = request.form['description']

        new_warehouse = crud.create_warehouse(address, 0, max_capacity, description)
        db.session.add(new_warehouse)
        db.session.commit()
        flash("warehouse created!")

        return redirect("/")

# ================= Item Related =================

@app.route ("/create_item", methods = ["GET", "POST"])
def create_item():
    """ Creates an item """
    # GET method fetches a form for item creation
    # POST method processes form to create an item in DB

    if request.method == "GET":
        return render_template("create_item.html")
    else:
        sku = int(request.form['sku'])
        name = request.form['name']
        department = request.form['department']
        quantity = int(request.form['quantity'])
        unit_price = float(request.form['unit_price'])
        description = request.form['description']

        new_item = crud.create_item(sku, name, department, quantity, unit_price, description)
        db.session.add(new_item)
        db.session.commit()
        flash("item created!")

        return redirect("/")


@app.route ("/view_items")
def view_items():
    """ View all items """

    items = crud.get_all_items()

    return render_template("view_items.html", items=items)


@app.route ("/remove_item")
def remove_item():
    """ Remove an item"""

    removal_id = request.args['remove_id']
    remove_item = crud.get_item_by(item_id = removal_id)
    db.session.delete(remove_item)
    db.session.commit()

    return redirect("/view_items")


@app.route ("/edit_item", methods=["GET", "POST"])
def edit_item():
    """ Edit an item"""
    # GET method loads form to edit the item
    # POST method updates item attributes based on form input

    if request.method == "GET":
        edit_id = request.args['edit_id']
        edit_item = crud.get_item_by(item_id = edit_id)
        warehouses = crud.get_all_warehouse()

        return render_template("edit_item.html", item=edit_item, warehouses=warehouses)
    else:
        item_id = request.form['item_id']
        sku = int(request.form['sku'])
        name = request.form['name']
        department = request.form['department']
        quantity = int(request.form['quantity'])
        unit_price = float(request.form['unit_price'])
        description = request.form['description']
        warehouse_id = int(request.form['warehouse_location'])

        warehouse = [crud.get_warehouse_by(warehouse_id = warehouse_id)]

        edit_item = crud.get_item_by(item_id = item_id)
        edit_item = crud.update_item(item_id=item_id, sku=sku, name=name, department=department, quantity=quantity, unit_price=unit_price, description=description, warehouse=warehouse)

        return redirect("view_items")


# ================= System Related =================

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug = True)

