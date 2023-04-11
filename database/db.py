import mysql.connector

# def get_db_connection():
#     # try:
#     db = mysql.connector.connect(
#             host="database",
#             user="user",
#             password="password",
#             database="ollivanders",
#         )
#     if db.is_connected():
#         return db
#     else:
#         return None
#     # except sqlite3.Error as e:  # pragma: no cover
#     #     print(f"Error connecting to database: {e}")
#     #     return None


def get_all_inventory():
    db = mysql.connector.connect(
        host="database",
        user="user",
        password="password",
        database="ollivanders",
    )
    conn = db.cursor()
    conn.execute("SELECT * FROM inventory")
    column_names = [col[0] for col in conn.description]
    query = conn.fetchall()

    INVENTORY = []
    for row in query:
        row_dict = {column_names[i]: row[i] for i in range(len(column_names))}
        INVENTORY.append(row_dict)

    conn.close()
    return INVENTORY


def get_item_by_id(id):
    db = mysql.connector.connect(
        host="database",
        user="user",
        password="password",
        database="ollivanders",
    )
    conn = db.cursor()
    conn.execute("SELECT * FROM inventory WHERE id = %s", (id,))
    column_names = [col[0] for col in conn.description]
    query = conn.fetchone()

    item = {column_names[i]: query[i] for i in range(len(column_names))}

    conn.close()
    return item


def get_item_by_name(name):
    db = mysql.connector.connect(
        host="database",
        user="user",
        password="password",
        database="ollivanders",
    )
    conn = db.cursor()
    item = conn.execute("SELECT * FROM inventory WHERE name = %s", (name,))
    column_names = [col[0] for col in conn.description]
    query = conn.fetchone()

    item = {column_names[i]: query[i] for i in range(len(column_names))}

    conn.close()
    return item


def update_item(sell_in, quality, id):
    db = mysql.connector.connect(
        host="database",
        user="user",
        password="password",
        database="ollivanders",
    )
    conn = db.cursor()
    conn.execute(
        "UPDATE inventory SET sell_in = %s, quality = %s WHERE id = %s",
        (sell_in, quality, id),
    )
    db.commit()
    conn.close()


def create_item(name, sell_in, quality, class_object):
    db = mysql.connector.connect(
        host="database",
        user="user",
        password="password",
        database="ollivanders",
    )
    conn = db.cursor()
    conn.execute(
        "INSERT INTO inventory (name, sell_in, quality, class_object) VALUES (%s, %s, %s, %s)",
        (name, sell_in, quality, class_object),
    )
    db.commit()
    conn.close()


def delete_item(id):
    db = mysql.connector.connect(
        host="database",
        user="user",
        password="password",
        database="ollivanders",
    )
    conn = db.cursor()
    conn.execute("DELETE FROM inventory WHERE id = %s", (id,))
    db.commit()
    conn.close()
