# dtypes.py

DTYPES = {
    "date": "datetime64[ns]",
    "indice": "float",
    "nIndice": "float",
    "acumulado": "float",
    "acumulado12m": "float",
    "peso": "float",
    "category": "string",
    "category_name": "string",
    "value": "float",
}


def apply_dtypes(df):
    for col, dtype in DTYPES.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)
    return df
