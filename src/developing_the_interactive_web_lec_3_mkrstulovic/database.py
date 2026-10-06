import psycopg

# Connect to an existing database
with psycopg.connect("dbname=test user=postgres") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:
      cur.execute("""
        insert into guestbook (name) values ('John');""")
      conn.commit()