import random

ip_address = [random.randint(0, 255) for _ in range(4)]

message = "{0}.{1}.{2}.{3}".format(ip_address[0], ip_address[1], ip_address[2], ip_address[3])

print(f"IP-адрес: {message}")
