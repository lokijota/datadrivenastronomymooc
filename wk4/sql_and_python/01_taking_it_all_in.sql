import psycopg2

def select_all(table_name):
  # Establish the connection
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()

  # Execute an SQL query and receive the output
  cursor.execute('SELECT * from ' + table_name)
  return cursor.fetchall()


