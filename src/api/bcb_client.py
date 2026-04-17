import time
import requests
from typing import Any, Dict, List


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

#        Faz requisição à API do BCB (SGS) com:
#        - timeout
#        - retry com backoff exponencial
#        - detecção de HTML
#        - validação de JSON
#        Retorna SEMPRE uma lista de dicionários (ou lança RuntimeError).

        url = BCBClient._build_url(codigo_serie, data_inicial, data_final)
        last_error = None
        for attempt in range(1, retries + 1):
            try:
                response = requests.get(url, timeout=timeout)

                # Status HTTP diferente de 200
                if response.status_code != 200:
                    msg = (f"[Tentativa {attempt}] Status {response.status_code} ao chamar SGS: {url}")
                    print(msg)
                    last_error = RuntimeError(msg)
                else:
                    text = response.text.strip()

                    # Resposta vazia
                    if not text:
                        msg = f"[Tentativa {attempt}] SGS retornou resposta vazia: {url}"
                        print(msg)
                        last_error = RuntimeError(msg)

                    # HTML em vez de JSON
                    elif text.startswith("<"):
                        msg = f"[Tentativa {attempt}] SGS retornou HTML em vez de JSON: {url}"
                        print(msg)
                        last_error = RuntimeError(msg)

                    else:
                        # Tenta interpretar como JSON
                        try:
                            data = response.json()

                            # Garantir que seja lista
                            if isinstance(data, dict):
                                # SGS normalmente retorna lista; se vier dict, algo estranho aconteceu
                                msg = (f"[Tentativa {attempt}] JSON inesperado (dict) recebido do SGS: {url}")
                                print(msg)
                                last_error = RuntimeError(msg)
                            else:
                                return data

                        except Exception as e:
                            msg = f"[Tentativa {attempt}] Erro ao decodificar JSON do SGS: {e}"
                            print(msg)
                            last_error = RuntimeError(msg)

            except requests.Timeout:
                msg = f"[Tentativa {attempt}] Timeout ao chamar SGS: {url}"
                print(msg)
                last_error = RuntimeError(msg)

            except requests.RequestException as e:
                msg = f"[Tentativa {attempt}] Erro de rede ao chamar SGS: {e}"
                print(msg)
                last_error = RuntimeError(msg)

            # Se chegou aqui, falhou nesta tentativa → espera e tenta de novo
            sleep_time = backoff * attempt
            print(f"Aguardando {sleep_time}s antes da próxima tentativa...")
            time.sleep(sleep_time)

        # Se todas as tentativas falharem, levanta o último erro registrado
        raise last_error or RuntimeError(f"Falha ao obter dados do SGS: {url}")
