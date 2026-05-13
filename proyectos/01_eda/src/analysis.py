import pandas as pd
import numpy as np
import json
import os

def analyze_data(input_path, output_dir=None):
    df = pd.read_csv(input_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    stats = {
        "total_records": int(len(df)),
        "date_range": {
            "start": str(df["timestamp"].min()),
            "end": str(df["timestamp"].max())
        },
        "valor_stats": {
            "mean": round(float(df["valor"].mean()), 2),
            "median": round(float(df["valor"].median()), 2),
            "std": round(float(df["valor"].std()), 2),
            "min": round(float(df["valor"].min()), 2),
            "max": round(float(df["valor"].max()), 2)
        },
        "by_category": df["categoria"].value_counts().to_dict(),
        "by_region": df["region"].value_counts().to_dict(),
        "by_status": df["estado"].value_counts().to_dict(),
        "avg_by_category": df.groupby("categoria")["valor"].mean().round(2).to_dict(),
        "avg_by_region": df.groupby("region")["valor"].mean().round(2).to_dict(),
        "errors_count": int((df["estado"] == "Error").sum()),
        "error_rate": round(float((df["estado"] == "Error").mean() * 100), 2)
    }

    monthly = df.set_index("timestamp").resample("ME")["valor"].agg(["mean", "count"]).round(2)
    stats["monthly_trend"] = {
        str(idx.date()): {"mean": float(row["mean"]), "count": int(row["count"])}
        for idx, row in monthly.iterrows()
    }

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "analysis_results.json"), "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        print(f"Análisis guardado en: {output_dir}/analysis_results.json")

    print("\n=== RESUMEN DE ANÁLISIS ===")
    print(f"Total de registros: {stats['total_records']}")
    print(f"Rango de fechas: {stats['date_range']['start']} - {stats['date_range']['end']}")
    print(f"\nMétricas de valor:")
    print(f"  Media: {stats['valor_stats']['mean']}")
    print(f"  Mediana: {stats['valor_stats']['median']}")
    print(f"  Desviación estándar: {stats['valor_stats']['std']}")
    print(f"\nPor categoría: {stats['by_category']}")
    print(f"Por región: {stats['by_region']}")
    print(f"Estados: {stats['by_status']}")
    print(f"\nTasa de errores: {stats['error_rate']}%")

    return stats

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(script_dir), "data")
    input_path = os.path.join(data_dir, "dataset_cleaned.csv")
    output_dir = os.path.join(os.path.dirname(script_dir), "data")

    if os.path.exists(input_path):
        stats = analyze_data(input_path, output_dir)
    else:
        print("Ejecuta primero data_cleaning.py")