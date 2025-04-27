import requests
import json
import csv
import os
import time
from datetime import datetime

# Carrega as configurações de client_id, access_token e base_url
with open('../config.json') as f:
    config = json.load(f)

CLIENT_ID = config["client_id"]
ACCESS_TOKEN = config["access_token"]
BASE_URL = config["base_url"]
DELAY_SECONDS = config.get("delay_seconds", 15)
PRODUTOS_CSV_PATH = config.get("produtos_csv_path", "../produtos.csv")  # padrão se não achar

# Nome do arquivo de log
LOG_CSV = "../log_cadastro.csv"


# Inicializa o log para futuras análises
def inicializar_log():
    if not os.path.exists(LOG_CSV):
        with open(LOG_CSV, mode='w', newline='', encoding='utf-8') as log_file:
            writer = csv.writer(log_file)
            writer.writerow(["Timestamp", "SKU", "Acao", "Status", "Detalhes"])


# Registra erro no log
# Registra no log (sucesso ou erro)
def registrar_log(sku, acao, status, detalhes="-"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_CSV, mode='a', newline='', encoding='utf-8') as log_file:
        writer = csv.writer(log_file)
        writer.writerow([timestamp, sku, acao, status, detalhes])


# Função para cadastrar produto via API
def cadastrar_produto(produto):
    url = f"{BASE_URL}/v2/products"
    headers = {
        "client_id": CLIENT_ID,
        "access_token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

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

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 202:
            print(f"✅ Produto SKU {produto['sku']} cadastrado com sucesso.")
            return {"sku": produto['sku'], "status": "sucesso", "detalhes": f"Status {response.status_code}"}
        elif response.status_code == 409:
            print(f"ℹ️ Produto SKU {produto['sku']} já existe.")
            return {"sku": produto['sku'], "status": "erro",
                    "detalhes": f"Status {response.status_code}: {response.text}"}
        else:
            print(f"❌ Erro ao cadastrar SKU {produto['sku']}: {response.status_code}")
            print(response.text)
            return {"sku": produto['sku'], "status": "erro",
                    "detalhes": f"Status {response.status_code}: {response.text}"}

    except requests.RequestException as e:
        print(f"🚨 Erro de conexão ao cadastrar SKU {produto['sku']}: {e}")
        return {"sku": produto['sku'], "status": "erro_conexao", "detalhes": str(e)}


# Função para cadastrar preço
def cadastrar_preco(produto):
    url = f"{BASE_URL}/v2/products/{produto['sku']}/prices"
    headers = {
        "client_id": CLIENT_ID,
        "access_token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    try:
        list_price = float(produto["listPrice"])
        sale_price = float(produto["salePrice"])
    except (ValueError, TypeError) as e:
        # Se não conseguir converter, já loga o erro
        print(f"❌ Erro ao converter preço para SKU {produto['sku']}: {e}")
        return {"sku": produto['sku'], "status": "erro_conversao_preco", "detalhes": str(e)}

    payload = {
        "listPrice": list_price,
        "salePrice": sale_price
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 202:
            print(f"✅ Preço para SKU {produto['sku']} cadastrado com sucesso.")
            return {"sku": produto['sku'], "status": "sucesso", "detalhes": f"Status {response.status_code}"}
        elif response.status_code == 409:
            print(f"ℹ️ Preço já cadastrado para SKU {produto['sku']}.")
            return {"sku": produto['sku'], "status": "erro", "detalhes": f"Status {response.status_code}: "
                                                                         f"{response.text}"}
        else:
            print(f"❌ Erro ao cadastrar preço SKU {produto['sku']}: {response.status_code}")
            print(response.text)
            return {"sku": produto['sku'], "status": "erro_preco", "detalhes": f"Status {response.status_code}: "
                                                                               f"{response.text}"}

    except requests.RequestException as e:
        print(f"🚨 Erro de conexão ao cadastrar preço SKU {produto['sku']}: {e}")
        return {"sku": produto['sku'], "status": "erro_conexao_preco", "detalhes": str(e)}


# Função para cadastrar estoque
def cadastrar_estoque(produto):
    url = f"{BASE_URL}/v2/products/{produto['sku']}/stocks"
    headers = {
        "client_id": CLIENT_ID,
        "access_token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    try:
        available = int(produto["stockQuantity"])
    except (ValueError, TypeError) as e:
        print(f"❌ Erro ao converter estoque para SKU {produto['sku']}: {e}")
        return {"sku": produto['sku'], "status": "erro_conversao_estoque", "detalhes": str(e)}

    payload = {
        "available": available
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 202:
            print(f"✅ Estoque para SKU {produto['sku']} cadastrado com sucesso.")
            return {"sku": produto['sku'], "status": "sucesso", "detalhes": f"Status {response.status_code}"}
        elif response.status_code == 409:
            print(f"ℹ️ Estoque já cadastrado para SKU {produto['sku']}.")
            return {"sku": produto['sku'], "status": "erro", "detalhes": f"Status {response.status_code}: "
                                                                         f"{response.text}"}
        else:
            print(f"❌ Erro ao cadastrar estoque SKU {produto['sku']}: {response.status_code}")
            print(response.text)
            return {"sku": produto['sku'], "status": "erro_estoque", "detalhes": f"Status {response.status_code}: "
                                                                                 f"{response.text}"}

    except requests.RequestException as e:
        print(f"🚨 Erro de conexão ao cadastrar estoque SKU {produto['sku']}: {e}")
        return {"sku": produto['sku'], "status": "erro_conexao_estoque", "detalhes": str(e)}


# Processa todos os produtos do CSV
def processar_produtos_csv(caminho_csv):
    inicializar_log()

    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for linha in reader:
            resultado_produto = cadastrar_produto(linha)

            # Verifica o status do cadastro do produto
            if resultado_produto["status"] == "sucesso":
                # Produto criado novo ➔ aguarda
                print(
                    f"⏳ Aguardando {DELAY_SECONDS} segundos para o SKU {linha['sku']} estar disponível no servidor...")
                time.sleep(DELAY_SECONDS)

            elif resultado_produto["status"] == "erro" and "already exists" in resultado_produto["detalhes"]:
                # Produto já existe ➔ apenas continua
                print(f"ℹ️ SKU {linha['sku']} já existe, seguindo para preço e estoque.")

            else:
                # Erro real ➔ registra e pula
                registrar_log(resultado_produto["sku"], resultado_produto["status"], resultado_produto["detalhes"])
                continue

            # Agora sempre tenta cadastrar preço e estoque
            resultado_preco = cadastrar_preco(linha)
            if resultado_preco["status"] != "sucesso":
                registrar_log(resultado_preco["sku"], resultado_preco["status"], resultado_preco["detalhes"])

            resultado_estoque = cadastrar_estoque(linha)
            if resultado_estoque["status"] != "sucesso":
                registrar_log(resultado_estoque["sku"], resultado_estoque["status"], resultado_estoque["detalhes"])


# Execução principal
if __name__ == "__main__":
    caminho_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), PRODUTOS_CSV_PATH))
    processar_produtos_csv(caminho_csv)
