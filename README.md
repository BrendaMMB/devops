# 🏍️ Netshoes Marketplace - Cadastro de Produtos via API

Este projeto automatiza o cadastro de produtos no Marketplace da Netshoes utilizando Python e a API oficial do ambiente **sandbox**.

---

## 📦 Funcionalidades

- Leitura de produtos a partir de um arquivo CSV
- Cadastro completo via API:
  - Produto
  - Preço
  - Estoque
- Geração automática de log de execução (`log_erros_cadastro.csv`) registrando:
  - Timestamp da execução
  - SKU
  - Ação realizada (Produto, Preço, Estoque)
  - Status (sucesso ou erro)
  - Código de resposta HTTP e detalhes
- Delay configurável para aguardar a criação do produto no backend antes de cadastrar preço e estoque
- Separação segura de credenciais e parâmetros via `config.json`
- Tratamento de erros e conversões de tipo automáticas (float/int)
- Compatível com estrutura recomendada da Netshoes

---

## 🐂️ Estrutura esperada do CSV

**Exemplo de cabeçalho:**

```
sku,productGroup,department,productType,brand,name,description,color,gender,manufacturerCode,size,eanIsbn,height,width,depth,weight,image1,image2,attribute_name,attribute_value,listPrice,salePrice,stockQuantity
```

**Exemplo de linha de produto:**

```
BR_9084102_35,9084102,Casual,Botas,Beira Rio,Bota Feminina Cano Baixo Beira Rio 9084102,"Conheça a bota feminina...",Preto,Mulher,790000000000,35,790000000000,11,25,30,0.87,https://link1.jpg,https://link2.jpg,Indicado para,Dia a Dia,199.99,199.99,15
```

---

## 🔧 Configuração

1. Crie um arquivo `config.json` na raiz do projeto com o seguinte conteúdo:

```json
{
  "client_id": "SUA_CLIENT_ID_AQUI",
  "access_token": "SEU_ACCESS_TOKEN_AQUI",
  "base_url": "https://sandboxapi-marketplace.netshoes.com.br",
  "delay_seconds": 15,
  "produtos_csv_path": "../produtos.csv"
}
```

| Chave              | Descrição |
|:------------------|:----------|
| `client_id`         | Seu identificador de cliente da Netshoes |
| `access_token`      | Seu token de acesso à API |
| `base_url`          | URL base do ambiente (sandbox ou produção) |
| `delay_seconds`     | Tempo em segundos para aguardar após o cadastro do produto antes de cadastrar preço/estoque |
| `produtos_csv_path` | Caminho relativo para o arquivo `produtos.csv` |

> ⚠️ **Este arquivo não deve ser versionado!** Ele está incluído no `.gitignore`.  
> Para referência da equipe, utilize o arquivo `config.example.json`.

---

## ▶️ Como executar

1. Certifique-se de que você tem o Python instalado (versão 3.7 ou superior)
2. Instale as dependências necessárias:

```bash
pip install requests
```

3. Execute o script principal:

```bash
python src/main.py
```

> O script processará o CSV indicado no `config.json`, cadastrando os produtos, seus preços e estoques automaticamente, e gerando o log detalhado da execução.

---

## 📋 Requisitos

- Python 3.7 ou superior
- Biblioteca `requests` (instalável via pip)
- Acesso às credenciais da API Netshoes Marketplace (client_id e access_token)

---

## 🛡️ Aviso

⚠️ **Nunca envie o arquivo `config.json` para repositórios públicos!**  
Ele contém informações sensíveis de autenticação.

✔️ O `.gitignore` já está configurado para ignorar esse arquivo.  
✔️ Utilize `config.example.json` como base para compartilhar o formato do arquivo de configuração.

---

## 📈 Log de Execução (`log_erros_cadastro.csv`)

Durante a execução, um arquivo `log_erros_cadastro.csv` é gerado contendo:

| Timestamp           | SKU           | Ação    | Status  | Detalhes                          |
|:-------------------|:-------------|:---------|:-------|:---------------------------------|
| 2025-04-27 13:02:01 | BR_9084103_36 | Produto  | sucesso | Status 202 |
| 2025-04-27 13:02:16 | BR_9084103_36 | Preço    | sucesso | Status 202 |
| 2025-04-27 13:02:17 | BR_9084103_36 | Estoque  | sucesso | Status 202 |

Isso permite fácil rastreabilidade de toda a operação.

---
