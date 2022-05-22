""" Create database & seed with data for development """

import os, json, model, server, crud
from datetime import datetime as dt

os.system('dropdb shopify')
os.system('createdb shopify')

model.connect_to_db(server.app)
model.db.create_all()


# ====== create sample Warehouse ==========
santa_cruz = crud.create_warehouse("1156 High St, Santa Cruz, CA 95064", 0, 1000, "Santa Cruz Location")
fremont = crud.create_warehouse("38442 Fremont Blvd, Fremont, CA 94536", 0, 1000, "Fremont Location")
san_francisco = crud.create_warehouse("972 Mission St, San Francisco, CA 94103", 0, 1000, "San Francisco Location")


model.db.session.add_all([santa_cruz, fremont, san_francisco])


# ====== create sample items ==========
books = crud.create_item(111111, "Textbook", "books", 10, 4.99, "learn things")
chips = crud.create_item(222222, "chips", "groceries", 50, 3.49, "Canadian Cheddar & Bacon flavor")
water = crud.create_item(333333, "nestle water", "groceries", 30, 1.99, "Stolen water from municipal sources")

model.db.session.add_all([books, chips, water])

books.warehouse.append(santa_cruz)
chips.warehouse.append(fremont)
water.warehouse.append(fremont)


model.db.session.commit()


