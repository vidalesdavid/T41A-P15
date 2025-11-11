import psycopg2
import pytest

DB_CONFIG = {
    "dbname": "test_db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432
}

@pytest.fixture(scope="module")
def db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    conn.close()

def fetch_scalar(conn, query, params=()):
    with conn.cursor() as cur:
        cur.execute(query, params)
        return cur.fetchone()[0]

def fetch_all(conn, query, params=()):
    with conn.cursor() as cur:
        cur.execute(query, params)
        return cur.fetchall()

def test_calcular_descuento(db_connection):
    precio_1 = fetch_scalar(db_connection, "SELECT calcular_descuento(%s, %s)", (100.0, 25.0))
    assert precio_1 == pytest.approx(75.0)

def test_validar_correo(db_connection):
    assert fetch_scalar(db_connection, "SELECT validar_correo('test@example.com')") == True
    assert fetch_scalar(db_connection, "SELECT validar_correo('invalido')") == False

def test_productos_stock_menor(db_connection):
    query = "SELECT * FROM productos_stock_menor(%s)"
    result = fetch_all(db_connection, query, (50,))
    productos = {row[0] for row in result}
    # Nuevos productos con stock menor a 50: Auriculares Bluetooth (35), Monitor Curvo (15), Base para Laptop (40), Adaptador USB-C (90) → solo los que están por debajo de 50
    assert productos == {"Auriculares Bluetooth", "Monitor Curvo 32\"", "Base para Laptop"}

def test_get_dia_by_fecha(db_connection):
    query = "SELECT get_dia_by_fecha(%s::date)"
    dia = fetch_scalar(db_connection, query, ("2025-01-01",))
    assert dia in ("Miércoles", "Wednesday")

def test_get_cantidad_empleados_departamento(db_connection):
    query = "SELECT get_cantidad_empleados_departamento(%s)"
    cantidad_desarrollo = fetch_scalar(db_connection, query, (2,))  # Desarrollo
    assert cantidad_desarrollo == 2  # Laura Méndez, Claudia Salinas

    cantidad_logistica = fetch_scalar(db_connection, query, (1,))  # Logística
    assert cantidad_logistica == 2  # Valeria Cruz, Andrés Navarro

