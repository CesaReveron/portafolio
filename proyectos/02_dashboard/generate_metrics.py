import pandas as pd
import json
import os

df = pd.read_csv('proyectos/01_eda/data/dataset_cleaned.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

dashboard_data = {
    "summary": {
        "total_records": int(len(df)),
        "avg_value": round(float(df['valor'].mean()), 2),
        "error_rate": round(float((df['estado'] == 'Error').mean() * 100), 2),
        "avg_response_time": round(float(df['tiempo_respuesta'].mean()), 2)
    },
    "by_category": df['categoria'].value_counts().to_dict(),
    "avg_by_category": df.groupby('categoria')['valor'].mean().round(2).to_dict(),
    "by_region": df['region'].value_counts().to_dict(),
    "avg_by_region": df.groupby('region')['valor'].mean().round(2).to_dict(),
    "by_status": df['estado'].value_counts().to_dict(),
    "monthly_labels": [],
    "monthly_values": []
}

monthly = df.set_index('timestamp').resample('ME')['valor'].mean()
for idx, val in monthly.items():
    dashboard_data["monthly_labels"].append(idx.strftime('%b %Y'))
    dashboard_data["monthly_values"].append(round(float(val), 2))

output_path = 'proyectos/02_dashboard/data/metrics.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(dashboard_data, f, indent=2)

print(f"Datos para dashboard guardados en: {output_path}")
print(f"Total categorías: {len(dashboard_data['by_category'])}")
print(f"Meses de datos: {len(dashboard_data['monthly_labels'])}")