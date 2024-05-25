import sqlite3
from sqlite3 import Error
import hashlib

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('src/database/database.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_admin_and_sector(conn):
    """Insere um setor inicial (Adm) e um usuário (Admin) no banco de dados."""
    try:
        sql_insert_sector = """INSERT INTO sectors (name) VALUES ('Adm');"""
        c = conn.cursor()
        c.execute(sql_insert_sector)
        sector_id = c.lastrowid  
        password = "123"
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()  
        sql_insert_user = """INSERT INTO users (name, role, sector_id, password) VALUES (?, ?, ?, ?);"""
        c.execute(sql_insert_user, ("Admin", "Administrator", sector_id, encrypted_password))
        
        conn.commit()
    except Error as e:
        print(e)

def main():
    conn = create_connection()

    sql_create_sectors_table = """
    CREATE TABLE IF NOT EXISTS sectors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    ); """

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        sector_id INTEGER,
        password TEXT,
        FOREIGN KEY (sector_id) REFERENCES sectors(id)
    ); """

    sql_create_machine_table = """
    CREATE TABLE IF NOT EXISTS machine (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sector_id INTEGER,
        FOREIGN KEY (sector_id) REFERENCES sectors(id)
    ); """

    sql_create_operations_table = """
    CREATE TABLE IF NOT EXISTS operations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sector_id INTEGER,
        FOREIGN KEY (sector_id) REFERENCES sectors(id)
    ); """

    sql_create_time_of_production_table = """
    CREATE TABLE IF NOT EXISTS time_of_production (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        machine_id INTEGER,
        operation_id INTEGER,
        time TEXT,
        item INTEGER,
        FOREIGN KEY (machine_id) REFERENCES machine(id),
        FOREIGN KEY (operation_id) REFERENCES operations(id)
    ); """

    sql_create_entries_and_exits_table = """
    CREATE TABLE IF NOT EXISTS entries_and_exits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        entry_type TEXT CHECK(entry_type IN ('stopping', 'setup', 'production')),
        sector_id INTEGER,
        machine_id INTEGER,
        entry_at TEXT,
        exit_at TEXT,
        item INTEGER,
        time_of_production_id INTEGER,
        production_order INTEGER,
        operation_id INTEGER,
        amount_produced INTEGER,
        reason_for_stopping_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (sector_id) REFERENCES sectors(id),
        FOREIGN KEY (machine_id) REFERENCES machine(id),
        FOREIGN KEY (operation_id) REFERENCES operations(id),
        FOREIGN KEY (reason_for_stopping_id) REFERENCES reason_for_stopping(id),
        FOREIGN KEY (time_of_production_id) REFERENCES time_of_production(id)
    ); """

    sql_create_reason_for_stopping_table = """
    CREATE TABLE IF NOT EXISTS reason_for_stopping (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    ); """

    sql_create_reason_for_discard_table = """
    CREATE TABLE IF NOT EXISTS reason_for_discard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    ); """

    sql_create_unconformities_table = """
    CREATE TABLE IF NOT EXISTS unconformities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reason_for_discard_id INTEGER,
        amount INTEGER,
        FOREIGN KEY (reason_for_discard_id) REFERENCES reason_for_discard(id)
    ); """

    # Criação das tabelas
    if conn:
        create_table(conn, sql_create_sectors_table)
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_machine_table)
        create_table(conn, sql_create_operations_table)
        create_table(conn, sql_create_time_of_production_table)
        create_table(conn, sql_create_entries_and_exits_table)
        create_table(conn, sql_create_reason_for_stopping_table)
        create_table(conn, sql_create_reason_for_discard_table)
        create_table(conn, sql_create_unconformities_table)
        #insere o usuário padrão
        insert_admin_and_sector(conn)
        conn.close()
        print("Banco de dados criado com sucesso!")
    else:
        print("Erro ao conectar ao banco de dados.")

main()
