import psycopg2


connection = psycopg2.connect(database="chinook")
cursor = connection.cursor()