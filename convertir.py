import pandas as pd
import json
import gzip
import os

# ── Configuración ──────────────────────────────────────────
ARCHIVO_ENTRADA = "distrital_web.xlsx"   # debe estar en la misma carpeta que este script
ARCHIVO_SALIDA  = "datos.json"
ARCHIVO_GZ      = "datos.json.gz"
# ───────────────────────────────────────────────────────────

print("Leyendo Excel… (puede tardar unos segundos)")
df = pd.read_excel(ARCHIVO_ENTRADA, engine="openpyxl")

# Limpiar: quitar filas completamente vacías
df = df.dropna(how="all")

# Convertir NaN a None para que JSON los convierta en null
df = df.where(pd.notnull(df), None)

print(f"Filas: {len(df):,}  |  Columnas: {len(df.columns)}")

# Exportar JSON normal
data = df.to_dict(orient="records")
with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

size_json = os.path.getsize(ARCHIVO_SALIDA) / 1024 / 1024
print(f"datos.json generado → {size_json:.1f} MB")

# Exportar JSON comprimido (.gz) — opción más liviana
with open(ARCHIVO_SALIDA, "rb") as f_in:
    with gzip.open(ARCHIVO_GZ, "wb", compresslevel=9) as f_out:
        f_out.write(f_in.read())

size_gz = os.path.getsize(ARCHIVO_GZ) / 1024 / 1024
print(f"datos.json.gz generado → {size_gz:.1f} MB")
print("¡Listo! Sube datos.json.gz (o datos.json) a GitHub.")
