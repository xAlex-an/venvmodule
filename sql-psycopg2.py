import psycopg2

# Connect to the database
connection = psycopg2.connect(database="chinook")


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