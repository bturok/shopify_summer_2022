# Shopify Backend Developer Intern Challenge - Summer 2022
# Brandon Turok
# brandon.turok@gmail.com
# 19 January 2022

import sqlite3


connection = sqlite3.connect('inventory.db')


with open('schema.sql') as f:
    connection.executescript(f.read())
