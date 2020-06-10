# SQL queering homework
import pyodbc

## make a new connection
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

new_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

## make a new cursor
new_cursor = new_connection.cursor()

#execute queries and get out the needed responses

execute_queries = new_cursor.execute('SELECT * FROM Orders')

# Queries
# Q1 - How many orders in NWDB?
# Query:
print(len(execute_queries.fetchall()))
# Response: 830orders

# Q2 - How many order that the Ship City is Rio de Janeiro?
# Query:
# all_results_list = execute_queries.fetchall()
# for data in all_results_list:
#     print(data.ShipCity == 'Rio de Janeiro')

query_2 = new_cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro'")
print(len(query_2.fetchall()))
# Response: 34

# Q3 - Select all orders that the Ship City is Rio de Janeiro or Reims?
# Query:
query_3 = new_cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro' OR ShipCity = 'Reims'")
print(query_3.fetchall())
# Response: print(query_3.fetchall())


# Q4 - Select all of the entries where the Company name has a z or a Z in the table of Customers
# Query:
# query_4 = new_cursor.execute("SELECT * FROM Customers WHERE CompanyName LIKE %z%")
# print(query_4.fetchall())
# Response:
#
# Q5 - We need to update all of our FAX information! This Day and age it is a must! 😅😅😅 Find me the Name of All of the companies that we do not have their FAX numbers! I would also like to know with whom I need to speak with, their contact numbers and what city they are base in.
# Query:
#
# Response:
#
# Q6 - Ahh there you are! My prize ⭐⭐SPARTANTS⭐⭐! MY MARES AND MY STALLIONS! We need to re-target all of our Customers is Paris! Get me information on these clients.
# Query:
#
# Response: