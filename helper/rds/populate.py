import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Replace these with your actual values
RDS_HOST = "rds-postgres-minimal-rdsinstance-mxdcpdxhiu5l.ckbqs4miivqy.us-east-1.rds.amazonaws.com"
RDS_PORT = 5432
MASTER_DB = "mydb"
USERNAME = "admin"
PASSWORD = "password"
NEW_DB_NAME = "mydb2"

# Step 1: Connect to the default 'postgres' database
conn = psycopg2.connect(
    host=RDS_HOST,
    port=RDS_PORT,
    dbname=MASTER_DB,
    user=USERNAME,
    password=PASSWORD
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # Needed to create a DB
cur = conn.cursor()

# Step 2: Create a new database
try:
    cur.execute(f"CREATE DATABASE {NEW_DB_NAME};")
    print(f"✅ Database '{NEW_DB_NAME}' created.")
except psycopg2.errors.DuplicateDatabase:
    print(f"⚠️ Database '{NEW_DB_NAME}' already exists.")
cur.close()
conn.close()

# Step 3: Connect to the new database and insert mock data
conn = psycopg2.connect(
    host=RDS_HOST,
    port=RDS_PORT,
    dbname=NEW_DB_NAME,
    user=USERNAME,
    password=PASSWORD
)
cur = conn.cursor()

# Step 4: Create a table and insert mock data
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    );
""")
cur.execute("""
    INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Jane', 'jane@example.com'),
    ('John', 'john@example.com'),
    ('Jill', 'jill@example.com');     
""")
conn.commit()
print("✅ Mock data inserted into 'users' table.")

# Step 5: Verify
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()
print("📊 Data in 'users':")
for row in rows:
    print(row)

cur.close()
conn.close()
