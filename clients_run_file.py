from db_clients_read import ReadClients

clients = ReadClients()

print(clients.get_one())

print(clients.get_all('Maria'))

# print(clients_table.create_entry('ZHRJ', 'Carrefour', 'Jean-Charles', 'Manager', '4 Privet drive', 'London', 'Greater London', 'XK121HZ', 'UK', '790097483', '7299302'))