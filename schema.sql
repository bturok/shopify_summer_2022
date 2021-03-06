DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    price NUMERIC NOT NULL,
    quantity_in_stock NUMERIC NOT NULL,
    quantity_on_order NUMERIC NOT NULL,
    upc NUMERIC NOT NULL,
    sku TEXT NOT NULL
)