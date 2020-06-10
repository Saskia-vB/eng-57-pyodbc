import pyodbc

class MSDBconnection():
    # should establish connection with any DB we have in MSsql
    def __init__(self, database='Northwind'):
        # 1) DB server connection variables
        self.server = 'databases2.spartaglobal.academy'
        self.database = database
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.conn = self._establish_connection()
        self.cursor = self.conn.cursor()
    # 2) establishing the connection
    def _establish_connection(self):
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        return connection

    # open to SQL injections
    def sql_query(self, sql_string):
        # call method to filter out DROP table and DELETE * and only allow certain SQL queries
        return self.cursor.execute(sql_string)


nwind = MSDBconnection()
print(nwind.sql_query('SELECT * FROM Products'))

results = nwind.sql_query('SELECT * FROM Products')