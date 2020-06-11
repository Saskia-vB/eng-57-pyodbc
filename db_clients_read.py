
from db_connection_OOP import MSDBconnection
from db_clients_oop import DBClientstable

class ReadClients(MSDBconnection):
    def get_one(self):
        return self.sql_query('SELECT * FROM Customers').fetchone()


    def get_all(self, contact_name=None):
        result_list = []
        if contact_name == None:
            q_result = self.sql_query('SELECT * FROM Customers')
        else:
            q_result = self.sql_query(f"SELECT * FROM Customers WHERE ContactName LIKE '%{contact_name}%'")
        while True:
            row = q_result.fetchone()
            if row == None:
                break
            result_list.append(row)
        return result_list

