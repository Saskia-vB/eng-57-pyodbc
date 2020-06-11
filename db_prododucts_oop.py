from db_connection_OOP import MSDBconnection

class DBProduct_table(MSDBconnection):

    def get_by_id(self,id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID =' + str(id)).fetchone()

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








# results = db_product_table().sql_query('SELECT * FROM Products')

# while True:
#     row : results.fetchone()
#
#     if row == None:
#         break
#     print