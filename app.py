# Shopify Backend Developer Intern Challenge - Summer 2022
# Brandon Turok
# brandon.turok@gmail.com
# 19 January 2022

import csv
import io
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect, abort, Response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'L8HxF7PABLxo8mfv6f3yCC3oUgWcupMw'


def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_item(item_id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM inventory WHERE id = ?', (item_id,)).fetchone()
    conn.close()

    if item is None:
        abort(404)

    return item


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    conn = get_db_connection()
    inventory = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return render_template('index.html', items=inventory)


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'GET':
        return render_template('add.html')

    name = request.form['name']
    price = request.form['price']
    quantity_in_stock = request.form['quantity_in_stock']
    quantity_on_order = request.form['quantity_on_order']
    upc = request.form['upc']
    sku = request.form['sku']

    if name != '' and price != '' and quantity_in_stock != '' and quantity_on_order != '' and upc != '' and sku != '':
        conn = get_db_connection()
        conn.execute('INSERT INTO inventory (name, price, quantity_in_stock, quantity_on_order, upc, sku) '
                     'VALUES (?,?,?,?,?,?)', (name, price, quantity_in_stock, quantity_on_order, upc, sku))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    if name == '':
        flash('Name cannot be left blank!')

    if price == '':
        flash('Price cannot be left blank!')

    if quantity_in_stock == '':
        flash('Quantity in stock cannot be left blank!')

    if quantity_on_order == '':
        flash('Quantity on order cannot be left blank!')

    if upc == '':
        flash('UPC cannot be left blank!')

    if sku == '':
        flash('SKU cannot be left blank!')

    return redirect(url_for('add_item'))


@app.route('/edit', methods=['GET', 'POST'])
def edit_item():
    if request.method == 'GET':
        id = request.args.get('id')
        item = get_item(id)
        return render_template('edit.html', item=item)

    id = request.form['id']
    name = request.form['name']
    price = request.form['price']
    quantity_in_stock = request.form['quantity_in_stock']
    quantity_on_order = request.form['quantity_on_order']
    upc = request.form['upc']
    sku = request.form['sku']

    if name != '' and price != '' and quantity_in_stock != '' and quantity_on_order != '' and upc != '' and sku != '' and id != '':
        conn = get_db_connection()
        conn.execute('UPDATE inventory SET name = ?, price = ?, quantity_in_stock = ?, quantity_on_order = ?, upc = ?,'
                     ' sku = ? WHERE id = ?',
                     (name, price, quantity_in_stock, quantity_on_order, upc, sku, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    if name == '':
        flash('Name cannot be left blank!')

    if price == '':
        flash('Price cannot be left blank!')

    if quantity_in_stock == '':
        flash('Quantity in stock cannot be left blank!')

    if quantity_on_order == '':
        flash('Quantity on order cannot be left blank!')

    if upc == '':
        flash('UPC cannot be left blank!')

    if sku == '':
        flash('SKU cannot be left blank!')

    return redirect(url_for('add_item'))


@app.route('/delete', methods=['GET', 'POST'])
def delete_item():
    if request.method == 'GET':
        id = request.args.get('id')
        item = get_item(id)
        return render_template('delete.html', item=item)

    id = request.args.get('id')
    conn = get_db_connection()
    conn.execute('DELETE FROM inventory WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/export', methods=['GET'])
def export_db():
    conn = get_db_connection()
    inventory = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    line = ['id', 'created_at', 'name', 'price', 'quantity_in_stock', 'quantity_on_order', 'upc', 'sku']
    writer.writerow(line)

    for row in inventory:
        id = row['id']
        created_at = row['created_at']
        name = row['name']
        price = row['price']
        quantity_in_stock = row['quantity_in_stock']
        quantity_on_order = row['quantity_on_order']
        upc = row['upc']
        sku = row['sku']

        line = [id, created_at, name, price, quantity_in_stock, quantity_on_order, upc, sku]
        writer.writerow(line)

    output.seek(0)

    return Response(output, mimetype='text/csv', headers={"Content-Disposition":"attachment;filename=db.csv"})


if __name__ == '__main__':
    app.run()
