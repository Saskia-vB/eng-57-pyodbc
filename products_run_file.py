from db_products_crum import Create_Product
from db_prododucts_oop import DBProduct_table

products_table = Create_Product()
print(products_table.insert_product('Chai', 1, 2, 'half doz', 4.0, 6, 7, 5))

product_table = DBProduct_table()
print(product_table.get_by_id(1))

print(product_table.get_all('Chef'))