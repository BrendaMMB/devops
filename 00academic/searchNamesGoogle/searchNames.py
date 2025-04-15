from configApi import api_key, cx
from googleapiclient.discovery import build
import datetime


def google_search(api_key, cx, query, start_index=1):
    service = build("customsearch", "v1", developerKey=api_key)

    try:
        # Obtém a data atual e formata no formato YYYY-MM-DD
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        result = service.cse().list(
            q=f'{query} daterange:..{today}',
            cx=cx,
            start=start_index
        ).execute()

        items = result.get("items", [])

        if not items:
            print("Nenhum resultado encontrado.")
        else:
            for item in items:
                print(f'Título: {item["title"]}\nLink: {item["link"]}\n\n')

        # Se houver mais resultados, faça uma chamada recursiva com o próximo índice de início
        if "queries" in result and "nextPage" in result["queries"]:
            next_start_index = result["queries"]["nextPage"][0]["startIndex"]
            google_search(api_key, cx, query, start_index=next_start_index)

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    # Substitua 'SuaChaveDeAPI' e 'SeuCX' pelos valores corretos
    # api_key = "SuaChaveDeAPI"
    # cx = "SeuCX"
    query = input("Digite a palavra-chave de pesquisa: ")

    google_search(api_key, cx, query)
