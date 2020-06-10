from db_connection_OOP import MSDBconnection

class Create_Product(MSDBconnection):

    def insert_product(self, ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued) VALUES {ProductID}, '{ProductName}', {SupplierID}, {CategoryID}, '{QuantityPerUnit}', {UnitsInStock}, {UnitsOnOrder}, {ReorderLevel}, {Discontinued}""")

