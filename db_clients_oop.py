# 1)
# And we are going ot use the package to make a OOP module that abstracts our interaction with the NW DB. Starting with the connection.

import pyodbc
from db_connection_OOP import MSDBconnection

class DBClientstable(MSDBconnection):

    def get_clients(self):
        return self.sql_query('SELECT * FROM Customers')

clients_table = DBClientstable()
print(clients_table.get_clients())

    def create_client(self, client_name):
        q_result = self.sql_query("INSERT INTO Customers VALUES ('ZEIR', 'Saskia's shop', 'Saskia vB', 'Founder', '4 Privet Drive', 'Leavesden', 'NULL', 'WD25 7LR', 'UK', '24535', '24564756'")
        return 


# 2)
# And then further abstract the interaction with specific Tables.
#
# 3)
# Finally, where appropriate we will use the CRUD design to build methods.
