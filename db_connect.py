import pyodbc

# 1) DB server connection variables

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# 2) establishing the connection
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# print(connection)

# 3) make a cursor (this keeps state)
cursor = connection.cursor()

# print(cursor)
query_result = cursor.execute('SELECT * FROM Products')

# print(query.fetchall())
# rows = []
# while True:
#     row = cursor.fetchone()
#     rows.append(row)
#     if row == None:
#         break
#     print(row)
# print(rows[0])

# the better way of getting out all your data
# while True:
# # use our query results or cursor with query results and
# # fetch one at time and
# # do whatever we want/need with that data point - print it? get out the price? add a discount?
# # stop the iteration when there is no more data
# # -> or when the date point is None (python)/null (SQL)
#     row = query_result.fetchone()
#     if row == None:
#         break
#     print('NOW ONLY:', float(row.UnitPrice) * 1.25)


# fetchmany when you know how many rows

print(cursor.fetchmany(30))

# the way you fetch data will have an impact on performance and price at the end of the month
