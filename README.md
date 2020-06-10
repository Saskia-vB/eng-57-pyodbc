# Connecting Python with DB

This class will allow our python to easily connect with our DB.

## Package
To do so, we will use a package (external to python standard library) call PYODBC.
It's like a class but when we say import it first looks at standard library then a repository that has all those abstractions/OOP.
This package abstracts our connections to the DB.

## Method
- Cursor is a method that represents a database cursor. 
- Manages the context of a fetch operation 
- Cursors created from the same connection are not isolated (changes done by one cursors are immediately visible to other cursors)
- OOP: a method is a function that belongs to a object and a parameter/attribute of an object is a characterisitc, a variable that belongs to the object.
- It keeps state: so like a stack of data, once it fetches one that one is 'removed' and it goes on to the next row.

syntax: 
query_result = cursor.execute('SELECT * FROM Products')
print(query_result.fetchone())
data_point_card = query_result.fetchone()
- behaves like an iterable list, organised with index
print(data_point_card[1])
- behave like OOP object (to complete)

- Get all the rows:
- syntax : print(query_result.fetchall())
- bad because of the quantity of data

all_results_list = query_result.fetchall()

for data in all_results_list:
    print(data.ProductName, data.UnitPrice)

# PYODBC and OOP

We are looking into the PYODBC package. 

1)
And we are going ot use the package to make a OOP module that abstracts our interaction with the NW DB. Starting with the connection.  
2)
And then further abstract the interaction with specific Tables. 

3)
Finally, where appropriate we will use the CRUD design to build methods. 

# CRUD
## Create
## READ
### READ one
### READ all on parameter
## Update
## Delete

    
