# Connecting Python with DB

This class will allow our python to easily connect with our DB.

## Package
To do so, we will use a package (external to python standard library) call PYODBC.

This package abstracts our connections to the DB.

## Method
- Cursor is a method that represents a database cursor. 
- Manages the context of a fetch operation 
- Cursors created from the same connection are not isolated (changes done by one cursors are immediately visible to other cursors)

It keeps state.

syntax: query_result = cursor.execute('SELECT * FROM Products')
print(query_result.fetchone())
print(query_result.fetchall())

all_results_list = query_result.fetchall()

for data in all_results_list:
    print(data.ProductName, data.UnitPrice)