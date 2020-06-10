# 1)
# And we are going ot use the package to make a OOP module that abstracts our interaction with the NW DB. Starting with the connection.

import pyodbc
from db_connection_OOP import MSDBconnection

class DBClientstable(MSDBconnection):

    def get_clients(self):
        return self.sql_query('SELECT * FROM Customers')

# print(clients_table.get_clients())

    # def create_client(self):
    #     q_result = self.sql_query("INSERT INTO Customers VALUES ('ZEIR', 'Saskia's shop', 'Saskia vB', 'Founder', '4    Privet Drive', 'Leavesden', 'NULL', 'WD25 7LR', 'UK', '24535', '24564756'")
    #     return q_result

    def create_entry(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, ReorderLevel, Discontinued):
        return self.sql_query(f"""INSERT INTO Customers (ProductID, ProductName,    SupplierID, CategoryID, QuantityPerUnit, UnitsInStock, UnitsOnOrder,    ReorderLevel, Discontinued)
    VALUES (f{ProductID}, '{ProductName}', {SupplierID}, {CategoryI D},'{QuantityPerUnit}', {UnitsInStock}, {UnitsOnOrder}, {ReorderLevel}, {Discontinued})""")

clients_table = DBClientstable()
# 2)
# And then further abstract the interaction with specific Tables.
#
# 3)
# Finally, where appropriate we will use the CRUD design to build methods.
