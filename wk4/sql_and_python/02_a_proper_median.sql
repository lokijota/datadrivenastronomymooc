import psycopg2
import numpy as np

def column_stats(table_name, column_name):
  # Establish the connection
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()

  # Execute an SQL query and receive the output
  cursor.execute('SELECT ' + column_name + ' from ' + table_name)
  results = cursor.fetchall()
  
  mean = np.mean(results)
  median = np.median(results)
  
  return mean, median

