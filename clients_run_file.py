from db_clients_read import ReadClients

clients = ReadClients()

print(clients.get_one())

print(clients.get_all())