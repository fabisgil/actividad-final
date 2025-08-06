import requests
import json

API_BASE = "https://crudcrud.com/api/db52c8d20eb04dc2ad691a3a601f2f4f/devices"

def agregar_dispositivo(data):
    response = requests.post(API_BASE, json=data)
    if response.status_code == 201:
        print(" Dispositivo agregado:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f" Error ({response.status_code}): {response.text}")

def listar_dispositivos():
    response = requests.get(API_BASE)
    if response.status_code == 200:
        dispositivos = response.json()
        print("📋 Dispositivos registrados:")
        for d in dispositivos:
            print(json.dumps(d, indent=2))
        return dispositivos
    else:
        print(f" Error ({response.status_code}): {response.text}")
        return []

def actualizar_dispositivo(device_id, data):
    url = f"{API_BASE}/{device_id}"
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(" Dispositivo actualizado correctamente.")
    else:
        print(f" Error ({response.status_code}): {response.text}")

def eliminar_dispositivo(device_id):
    url = f"{API_BASE}/{device_id}"
    response = requests.delete(url)
    if response.status_code == 200 or response.status_code == 204:
        print("Dispositivo eliminado correctamente.")
    elif response.status_code == 404:
        print(" Dispositivo no encontrado.")
    else:
        print(f"Error ({response.status_code}): {response.text}")

if __name__ == "__main__":
    nuevo = {
        "nombre": "RouterDemo01",
        "ip": "10.0.0.1",
        "tipo": "Router"
    }
    agregar_dispositivo(nuevo)

    dispositivos = listar_dispositivos()

    if dispositivos:
        primer_id = dispositivos[0]['_id']
        actualizado = {
            "nombre": "RouterDemo01-Actualizado",
            "ip": "10.0.0.99",
            "tipo": "Router"
        }
        actualizar_dispositivo(primer_id, actualizado)

    # 4. Eliminar el primero si existe
    if dispositivos:
        eliminar_dispositivo(primer_id)
