import json

file_path = r"C:\Users\eldos\PYTHON\Lab1\Lab4\JSON\sample-data.json"

with open(file_path, "r") as file:
    data = json.load(file)

interfaces = data["imdata"]  # Получаем список интерфейсов

print("Interface Status")
print("=" * 80)
print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for imdata in interfaces:
    attributes = imdata.get("l1PhysIf", {}).get("attributes", {})  # Извлекаем атрибуты
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "N/A")  # В JSON, скорее всего, ключ 'descr', а не 'description'
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")

    print("{:<50} {:<15} {:<10} {:<10}".format(dn, description, speed, mtu))
