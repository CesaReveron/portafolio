import csv
import random
from datetime import datetime, timedelta

def generate_dataset(filename="dataset.csv", num_records=600):
    categorias = ["Electronica", "Mecanica", "Software", "Logistica", "Calidad"]
    estados = ["Activo", "Inactivo", "Error", "Mantenimiento"]
    regiones = ["Norte", "Sur", "Este", "Oeste", "Centro"]

    start_date = datetime(2025, 1, 1)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "timestamp", "categoria", "valor", "estado", "region", "tiempo_respuesta"])

        for i in range(1, num_records + 1):
            timestamp = start_date + timedelta(hours=i * 3)
            categoria = random.choice(categorias)
            estado = random.choice(estados)

            if estado == "Error":
                valor = random.uniform(0, 30)
            elif estado == "Inactivo":
                valor = random.uniform(0, 10)
            else:
                valor = random.uniform(20, 100)

            if random.random() < 0.03:
                valor += random.uniform(50, 100)

            region = random.choice(regiones)
            tiempo_respuesta = round(random.uniform(0.1, 15.0), 2)

            writer.writerow([
                i,
                timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                categoria,
                round(valor, 2),
                estado,
                region,
                tiempo_respuesta
            ])

    print(f"Dataset generado: {filename} con {num_records} registros")

if __name__ == "__main__":
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(script_dir), "data")
    os.makedirs(data_dir, exist_ok=True)
    output_path = os.path.join(data_dir, "dataset.csv")
    generate_dataset(output_path)