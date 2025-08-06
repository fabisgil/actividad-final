import unittest
import actividad_de_clase 

class TestGestionDispositivos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nuevo_dispositivo = {
            "nombre": "TestDevice",
            "ip": "192.168.0.1",
            "tipo": "Switch"
        }
        print("\n Agregando dispositivo de prueba...")
        response = actividad_de_clase.requests.post(actividad_de_clase.API_BASE, json=cls.nuevo_dispositivo)
        assert response.status_code == 201, f"Error creando dispositivo: {response.text}"
        cls.device_id = response.json()["_id"]

    def test_1_listar_dispositivos(self):
        print(" Test: listar dispositivos")
        dispositivos = actividad_de_clase.listar_dispositivos()
        self.assertIsInstance(dispositivos, list)
        self.assertGreaterEqual(len(dispositivos), 1)

    def test_2_actualizar_dispositivo(self):
        print(" Test: actualizar dispositivo")
        data_actualizada = {
            "nombre": "DispositivoEditado",
            "ip": "192.168.0.2",
            "tipo": "Router"
        }
        actividad_de_clase.actualizar_dispositivo(self.device_id, data_actualizada)

        dispositivos = actividad_de_clase.listar_dispositivos()
        actualizado = next((d for d in dispositivos if d["_id"] == self.device_id), None)
        self.assertIsNotNone(actualizado)
        self.assertEqual(actualizado["ip"], "192.168.0.2")

    def test_3_eliminar_dispositivo(self):
        print(" Test: eliminar dispositivo")
        actividad_de_clase.eliminar_dispositivo(self.device_id)
        dispositivos = actividad_de_clase.listar_dispositivos()
        ids = [d["_id"] for d in dispositivos]
        self.assertNotIn(self.device_id, ids)

if __name__ == '__main__':
    unittest.main()