import requests
import json
import csv

# Carregar config.json
with open('config.json') as f:
    config = json.load(f)

CLIENT_ID = config["client_id"]
ACCESS_TOKEN = config["access_token"]
BASE_URL = config["base_url"]

def cadastrar_produto(produto):
    url = f"{BASE_URL}/v2/products"
    headers = {
        "client_id": CLIENT_ID,
        "access_token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    # Monta o payload do produto com base dos produtos.csv
    payload = {
        "sku": produto["sku"],
        "productGroup": produto["productGroup"],
        "department": produto["department"],
        "productType": produto["productType"],
        "brand": produto["brand"],
        "name": produto["name"],
        "description": produto["description"],
        "color": produto["color"],
        "gender": produto["gender"],
        "manufacturerCode": produto["manufacturerCode"],
        "size": produto["size"],
        "eanIsbn": produto["eanIsbn"],
        "height": float(produto["height"]),
        "width": float(produto["width"]),
        "depth": float(produto["depth"]),
        "weight": float(produto["weight"]),
        "images": [
            {"url": produto["image1"]},
            {"url": produto["image2"]}
        ],
        "attributes": [
            {
                "name": produto["attribute_name"],
                "values": [produto["attribute_value"]]
            }
        ]
    }

    # Envia requisição da API
    response = requests.post(url, headers=headers, json=payload)

    # Resultado com sucesso é 202 neste caso
    if response.status_code in [202]:
        print(f"✅ Produto com SKU {produto['sku']} cadastrado com sucesso.")
    else:
        print(f"❌ Erro ao cadastrar SKU {produto['sku']}: {response.status_code}")
        print(response.text)

# Processa todos os produtos do CSV
def processar_produtos_csv(caminho_csv):
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for linha in reader:
            cadastrar_produto(linha)

# Execução
if __name__ == "__main__":
    processar_produtos_csv("produtos.csv")
