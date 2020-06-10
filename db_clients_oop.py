import pyodbc
from db_connection_OOP import MSDBconnection

class DBClientstable(MSDBconnection):

## Hard coded
    # def create_client(self):
    #     q_result = self.sql_query("INSERT INTO Customers VALUES ('ZEIR', 'Saskia's shop', 'Saskia vB', 'Founder', '4    Privet Drive', 'Leavesden', 'NULL', 'WD25 7LR', 'UK', '24535', '24564756'")
    #     return q_result

    def create_entry(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax):
        return self.sql_query(f"""INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)
    VALUES (f{CustomerID}, '{CompanyName}', {ContactName}, {ContactTitle},'{Address}', {City}, {Region}, {PostalCode}, {Country}, {Phone}, {Fax})""")

clients_table = DBClientstable()
# print(clients_table.create_entry('ZHRJ', 'Carrefour', 'Jean-Charles', 'Manager', '4 Privet drive', 'London', 'Greater London', 'XK121HZ', 'UK', '790097483', '7299302'))