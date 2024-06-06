import json
import random

# config2.json faylını oxumaq
with open('config2.json', 'r') as file:
    config = json.load(file)

# IP-ünvanını 192.168.42.0 alt şəbəkəsinə dəyişdirin
ip_octet = random.randint(1, 254)  # 192.168.42.1-192.168.42.254 aralığında təsadüfi IP
config['ip_address'] = f'192.168.42.{ip_octet}'

# Yaddaş məlumatını 2048 MB-a dəyişdirin
config['memory'] = 2048

# Yönləndirilmiş portlar haqqında məlumat əlavə edin
config['port_forwarding'] = {
    'guest_port': 35729,
    'host_port': 35729
}

# Saytlardan biri üçün administrator məlumatlarını dəyişdirin
config['sites'][0]['administrator'] = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'password': 'securepassword123',
    'about': 'I am a fictional character created for demonstration purposes.'
}

# Yeni my_config.json faylını yaradın
with open('my_config.json', 'w') as file:
    json.dump(config, file, indent=4)

print("Yeni my_config.json faylı yaradıldı.")
