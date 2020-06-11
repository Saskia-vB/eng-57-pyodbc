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
```python
import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
```

1)
And we are going ot use the package to make a OOP module that abstracts our interaction with the NW DB. Starting with the connection.

```python
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```
2)
And then further abstract the interaction with specific Tables. 

```python
    def _establish_connection(self):
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        return connection

    # open to SQL injections
    def sql_query(self, sql_string):
        # call method to filter out DROP table and DELETE * and only allow certain SQL queries
        return self.cursor.execute(sql_string)
```
3)
Finally, where appropriate we will use the CRUD design to build methods. 

# CRUD
## Create
```python
class Create_Product(MSDBconnection):

    def insert_product(self, ProductName, SupplierID, CategoryID, QuantityPerUnit,
                        UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductName, SupplierID, CategoryID,QuantityPerUnit,
                                UnitsInStock, UnitsOnOrder,ReorderLevel, Discontinued)
                                VALUES ('{ProductName}', {SupplierID}, {CategoryID}, '{QuantityPerUnit}',
                                {UnitsInStock}, {UnitsOnOrder}, {ReorderLevel},{Discontinued})""").commit
```
## READ
### READ one
```python
  def get_by_id(self,id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID =' + str(id)).fetchone()
```
### READ all on parameter
```python
# this also allows to search according to product_name
 def get_all(self, product_name=None):
        result_list = []

        if product_name == None:
            q_result = self.sql_query('SELECT * FROM Products')
        else:
            q_result = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{product_name}%'")
        while True:
            row = q_result.fetchone()
            if row == None:
                break
            result_list.append(row)
        return result_list

```
## Update
## Delete

# Run the code:
```python
products_table = Create_Product()
print(products_table.insert_product('Chai', 1, 2, 'half doz', 4.0, 6, 7, 5))

product_table = DBProduct_table()
print(product_table.get_by_id(1))

print(product_table.get_all('Chef'))
```

    
