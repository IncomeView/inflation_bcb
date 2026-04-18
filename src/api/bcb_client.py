import time
from typing import Any, Dict, List

import requests

from src.utils.logging import get_logger

logger = get_logger(__name__)


class BCBClient:
    BASE_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"

    DEFAULT_TIMEOUT = 10  # segundos
    DEFAULT_RETRIES = 5
    DEFAULT_BACKOFF = 2  # segundos base

    @staticmethod
    def _build_url(codigo_serie: int, data_inicial: str, data_final: str) -> str:
        return (
            BCBClient.BASE_URL.format(codigo=codigo_serie)
            + f"?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
        )

    @staticmethod
    def fetch(
        codigo_serie: int,
        data_inicial: str,
        data_final: str,
        retries: int = DEFAULT_RETRIES,
        backoff: int = DEFAULT_BACKOFF,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> List[Dict[str, Any]]:

        url = BCBClient._build_url(codigo_serie, data_inicial, data_final)
        logger.info(
            f"Iniciando requisição ao SGS | Série={codigo_serie} | "
            f"Período={data_inicial} → {data_final}"
        )

        last_error = None

        for attempt in range(1, retries + 1):
            try:
                logger.info(f"[Tentativa {attempt}] Chamando URL: {url}")
                response = requests.get(url, timeout=timeout)

                if response.status_code != 200:
                    msg = f"[Tentativa {attempt}] Status {response.status_code} ao chamar SGS"
                    logger.warning(msg)
                    last_error = RuntimeError(msg)
                else:
                    text = response.text.strip()

                    if not text:
                        msg = f"[Tentativa {attempt}] Resposta vazia do SGS"
                        logger.warning(msg)
                        last_error = RuntimeError(msg)

                    elif text.startswith("<"):
                        msg = f"[Tentativa {attempt}] HTML recebido em vez de JSON"
                        logger.warning(msg)
                        last_error = RuntimeError(msg)

                    else:
                        try:
                            data = response.json()

                            if isinstance(data, dict):
                                msg = f"[Tentativa {attempt}] JSON inesperado (dict) recebido"
                                logger.warning(msg)
                                last_error = RuntimeError(msg)
                            else:
                                return data

                        except Exception as e:
                            msg = f"[Tentativa {attempt}] Erro ao decodificar JSON: {e}"
                            logger.error(msg)
                            last_error = RuntimeError(msg)

            except requests.Timeout:
                msg = f"[Tentativa {attempt}] Timeout ao chamar SGS"
                logger.error(msg)
                last_error = RuntimeError(msg)

            except requests.RequestException as e:
                msg = f"[Tentativa {attempt}] Erro de rede ao chamar SGS: {e}"
                logger.error(msg)
                last_error = RuntimeError(msg)

            sleep_time = backoff * attempt
            logger.info(f"Aguardando {sleep_time}s antes da próxima tentativa...")
            time.sleep(sleep_time)

        logger.error(f"Falha após {retries} tentativas | URL: {url}")
        raise last_error or RuntimeError(f"Falha ao obter dados do SGS: {url}")

    def get_series(self, codigo_serie: int, data_inicial: str, data_final: str):
        return self.fetch(codigo_serie, data_inicial, data_final)
