def validate_df(df, required_cols):
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if df.empty:
        raise ValueError("DataFrame está vazio.")

    # opcional: validar duplicatas
    if df.duplicated().any():
        print("Aviso: DataFrame contém duplicatas.")
