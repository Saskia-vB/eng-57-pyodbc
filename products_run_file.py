from db_products_crum import Create_Product

products_table = Create_Product()
print(products_table.insert_product(2, 'Chai', 2, 5, '5 by 5', 6, 5, 3, '0'))