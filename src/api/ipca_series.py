import pandas as pd

from src.api.sidra_client import sidra_query


def get_ipca_grupo(grupo_codigo: int, periodo: str = "all"):
    """
    Retorna a série histórica de um grupo do IPCA.
    Tabela 1419, variável 63 (variação mensal).
    Classificação 315 = grupos do IPCA.
    """
    return sidra_query(
        tabela=1419,
        variavel=63,
        periodo=periodo,
        classificacao={"315": grupo_codigo},
    )


def get_ipca_geral(periodo: str = "all") -> pd.DataFrame:
    """
    Retorna a série histórica completa do IPCA geral (SIDRA 1737).

    Variáveis:
        63    = variação mensal        -> indice
        2266  = número-índice          -> nIndice
        69    = acumulado no ano       -> acumulado
        2265  = acumulado em 12 meses  -> acumulado12m
    """

    tabela = 1737

    df_63 = sidra_query(tabela=tabela, variavel=63, periodo=periodo)
    df_2266 = sidra_query(tabela=tabela, variavel=2266, periodo=periodo)
    df_69 = sidra_query(tabela=tabela, variavel=69, periodo=periodo)
    df_2265 = sidra_query(tabela=tabela, variavel=2265, periodo=periodo)

    # renomear colunas
    df_63 = df_63.rename(columns={"valor": "indice"})
    df_2266 = df_2266.rename(columns={"valor": "nIndice"})
    df_69 = df_69.rename(columns={"valor": "acumulado"})
    df_2265 = df_2265.rename(columns={"valor": "acumulado12m"})

    # merge pela coluna periodo
    df = (
        df_63[["periodo", "indice"]]
        .merge(df_2266[["periodo", "nIndice"]], on="periodo", how="left")
        .merge(df_69[["periodo", "acumulado"]], on="periodo", how="left")
        .merge(df_2265[["periodo", "acumulado12m"]], on="periodo", how="left")
    )

    # converter periodo -> datetime
    df["date"] = pd.to_datetime(df["periodo"], format="%Y%m")

    df = df.sort_values("date").reset_index(drop=True)

    return df[["date", "indice", "nIndice", "acumulado", "acumulado12m"]]
