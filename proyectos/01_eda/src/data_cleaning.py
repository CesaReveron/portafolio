import pandas as pd
import numpy as np
import os

def clean_data(input_path, output_path=None):
    df = pd.read_csv(input_path)

    print(f"Registros iniciales: {len(df)}")

    df_clean = df.drop_duplicates()
    print(f"Después de eliminar duplicados: {len(df_clean)}")

    df_clean = df_clean.dropna()
    print(f"Después de eliminar nulos: {len(df_clean)}")

    Q1 = df_clean["valor"].quantile(0.25)
    Q3 = df_clean["valor"].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df_clean[(df_clean["valor"] < lower) | (df_clean["valor"] > upper)]
    print(f"Outliers detectados: {len(outliers)}")

    df_clean = df_clean[(df_clean["valor"] >= lower) & (df_clean["valor"] <= upper)]
    print(f"Después de eliminar outliers: {len(df_clean)}")

    df_clean["valor"] = df_clean["valor"].round(2)
    df_clean["timestamp"] = pd.to_datetime(df_clean["timestamp"])

    if output_path:
        df_clean.to_csv(output_path, index=False)
        print(f"Datos limpios guardados en: {output_path}")

    return df_clean

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(script_dir), "data")
    input_path = os.path.join(data_dir, "dataset.csv")
    output_path = os.path.join(data_dir, "dataset_cleaned.csv")

    df = clean_data(input_path, output_path)
    print("\nResumen de datos limpios:")
    print(df.describe())