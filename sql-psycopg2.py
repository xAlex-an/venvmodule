import os, psycopg2

conn = psycopg2.connect(  # libpq odczyta PG* z env
    host=os.getenv("PGHOST"),
    port=os.getenv("PGPORT"),
    dbname=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD"),
)

# Create a cursor object of the database
cursor = connection.cursor()

# Execute a query
cursor.execute('SELECT * FROM "Artist"')

# Fetch all results
results = cursor.fetchall()

# fetch the single result
# results = cursor.fetchone()

# close the connection

connection.close()

# print the result

for result in results:
    print(result)