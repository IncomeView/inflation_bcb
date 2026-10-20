# ipca_taxonomia.py

# ==========================================================
# TAXONOMIA ECONÔMICA
# ==========================================================

ALIMENTACAO_DOMICILIO = "ALIMENTACAO_DOMICILIO"
ALIMENTACAO_FORA = "ALIMENTACAO_FORA"
BENS_INDUSTRIAIS = "BENS_INDUSTRIAIS"
SERVICOS = "SERVICOS"
MONITORADOS = "MONITORADOS"


# ==========================================================
# TAXONOMIA CIDADÃ
# ==========================================================

MERCADO = "MERCADO"
MORADIA = "MORADIA"
TRANSPORTE = "TRANSPORTE"
SAUDE = "SAUDE"
EDUCACAO = "EDUCACAO"
COMUNICACAO = "COMUNICACAO"
LAZER = "LAZER"
VESTUARIO = "VESTUARIO"
CASA = "CASA"
SERVICOS_PESSOAIS = "SERVICOS_PESSOAIS"

# ==========================================================
# CLASSIFICAÇÃO PADRÃO POR SUBGRUPO
# ==========================================================

CLASSIFICACAO_SUBGRUPOS = {
    "11": {
        "bloco_macro": ALIMENTACAO_DOMICILIO,
        "categoria_cidada": MERCADO,
    },
    "12": {
        "bloco_macro": ALIMENTACAO_FORA,
        "categoria_cidada": ALIMENTACAO_FORA,
    },
    "21": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": MORADIA,
    },
    "22": {
        "bloco_macro": MONITORADOS,
        "categoria_cidada": MORADIA,
    },
    "31": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": CASA,
    },
    "32": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": CASA,
    },
    "33": {
        "bloco_macro": SERVICOS,
        "categoria_cidada": CASA,
    },
    "41": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": VESTUARIO,
    },
    "42": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": VESTUARIO,
    },
    "43": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": VESTUARIO,
    },
    "44": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": VESTUARIO,
    },
    "51": {
        "bloco_macro": SERVICOS,
        "categoria_cidada": TRANSPORTE,
    },
    "61": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": SAUDE,
    },
    "62": {
        "bloco_macro": SERVICOS,
        "categoria_cidada": SAUDE,
    },
    "63": {
        "bloco_macro": BENS_INDUSTRIAIS,
        "categoria_cidada": SAUDE,
    },
    "71": {
        "bloco_macro": SERVICOS,
        "categoria_cidada": SERVICOS_PESSOAIS,
    },
    "72": {
        "bloco_macro": SERVICOS,
        "categoria_cidada": LAZER,
    },
    "81": {
        "bloco_macro": SERVICOS,
        "categoria_cidada": EDUCACAO,
    },
    "91": {
        "bloco_macro": SERVICOS,
        "categoria_cidada": COMUNICACAO,
    },
}


# ==========================================================
# EXCEÇÕES POR SUBITEM
# ==========================================================

CLASSIFICACAO_SUBITENS = {
    # =====================================================
    # HABITAÇÃO
    # =====================================================
    "2101001": {
        "bloco_macro": SERVICOS,
    },
    "2101002": {
        "bloco_macro": SERVICOS,
    },
    "2101012": {
        "bloco_macro": SERVICOS,
    },
    "2101004": {
        "bloco_macro": MONITORADOS,
    },
    "2103042": {
        "bloco_macro": SERVICOS,
    },
    # =====================================================
    # TRANSPORTE
    # =====================================================
    "5101001": {
        "bloco_macro": MONITORADOS,
    },
    "5101004": {
        "bloco_macro": MONITORADOS,
    },
    "5101011": {
        "bloco_macro": MONITORADOS,
    },
    "5104001": {
        "bloco_macro": MONITORADOS,
    },
    "5104002": {
        "bloco_macro": MONITORADOS,
    },
    "5104003": {
        "bloco_macro": MONITORADOS,
    },
    "5104005": {
        "bloco_macro": MONITORADOS,
    },
    "5102004": {
        "bloco_macro": MONITORADOS,
    },
    "5102001": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "5102020": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "5102053": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "5102007": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "5102009": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "5102010": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    # =====================================================
    # SAÚDE
    # =====================================================
    "6203001": {
        "bloco_macro": MONITORADOS,
    },
    # =====================================================
    # LAZER
    # =====================================================
    "7201010": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "7201019": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "7201020": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "7201023": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "7201067": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "7202041": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    # =====================================================
    # EDUCAÇÃO
    # =====================================================
    "8102001": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "8102004": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "8102007": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "8102008": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "8103001": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    "8103014": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
    # =====================================================
    # COMUNICAÇÃO
    # =====================================================
    "9101019": {
        "bloco_macro": BENS_INDUSTRIAIS,
    },
}


def get_taxonomia(subitem_id: str) -> dict | None:
    codigo = str(subitem_id)
    subgrupo = codigo[:2]
    base = CLASSIFICACAO_SUBGRUPOS.get(subgrupo)

    if not base:
        return None

    taxonomia = base.copy()
    excecao = CLASSIFICACAO_SUBITENS.get(codigo)

    if excecao:
        taxonomia.update(excecao)

    return taxonomia


def get_bloco_macro(subitem_id: str):
    item = get_taxonomia(subitem_id)

    if item:
        return item["bloco_macro"]

    return None


def get_categoria_cidada(subitem_id: str):
    item = get_taxonomia(subitem_id)

    if item:
        return item["categoria_cidada"]

    return None
