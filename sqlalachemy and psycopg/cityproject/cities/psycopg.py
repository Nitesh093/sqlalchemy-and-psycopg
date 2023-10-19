import psycopg2
conn = psycopg2.connect(
    dbname="dbname",
    user="postgres",
    password="Nitesh123",
    host=""
)
cursor = conn.cursor()
