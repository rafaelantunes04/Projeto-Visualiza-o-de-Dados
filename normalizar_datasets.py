import pandas as pd
import re

INPUT_DIR  = "./data/processed/"
OUTPUT_DIR = "./"

TERRITORY_COL = "Territórios"
year_pattern  = re.compile(r"^(\d{4})")

FICHEIROS = [
    "Dataset 0-14.csv",
    "Dataset 15-24.csv",
    "Dataset 25-49.csv",
    "Dataset 50-59.csv",
    "Dataset 60-74.csv",
    "Dataset 75-84.csv",
    "Dataset 85+.csv",
]

for ficheiro in FICHEIROS:
    print(f"\n[A processar] {ficheiro}")
    df = pd.read_csv(INPUT_DIR + ficheiro)

    grupos_por_ano: dict[str, list[str]] = {}
    for col in df.columns:
        if col == TERRITORY_COL:
            continue
        m = year_pattern.match(col)
        if m:
            grupos_por_ano.setdefault(m.group(1), []).append(col)

    resultado = pd.DataFrame({TERRITORY_COL: df[TERRITORY_COL]})
    for ano in sorted(grupos_por_ano):
        resultado[ano] = df[grupos_por_ano[ano]].sum(axis=1)

    resultado.to_csv(OUTPUT_DIR + ficheiro, index=False)

    anos = [c for c in resultado.columns if c != TERRITORY_COL]
    print(f"Guardado: {OUTPUT_DIR}{ficheiro}")

print("\nConcluído!")
