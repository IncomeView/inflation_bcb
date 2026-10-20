# validate.py


def validate_df(
    df,
    required_cols=None,
    allow_empty=False,
):
    if required_cols:
        missing = [c for c in required_cols if c not in df.columns]

        if missing:
            raise ValueError(f"Missing columns: {missing}")

    if not allow_empty and df.empty:
        raise ValueError("DataFrame está vazio.")

    if df.duplicated().any():
        print("Aviso: DataFrame contém duplicatas.")

    return True
