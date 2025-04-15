# 🛒 Netshoes Marketplace - Cadastro de Produtos via API

Este projeto automatiza o cadastro de produtos no Marketplace da Netshoes utilizando Python e a API oficial do ambiente **sandbox**.

---

## 📦 Funcionalidades

- Leitura de produtos a partir de um arquivo CSV
- Envio de dados completos para a API (nome, descrição, imagens, atributos, etc.)
- Separação segura de credenciais via `config.json`
- Compatível com estrutura recomendada da Netshoes

---

## 🗂️ Estrutura esperada do CSV

Exemplo de cabeçalho:

```
sku,productGroup,department,productType,brand,name,description,color,gender,manufacturerCode,size,eanIsbn,height,width,depth,weight,image1,image2,attribute_name,attribute_value
```

Exemplo de linha:

```
BR_9084102_35,9084102,Casual,Botas,Beira Rio,Bota Feminina Cano Baixo Beira Rio 9084102,"Conheça a bota feminina...",Preto,Mulher,790000000000,35,790000000000,11,25,30,0.87,https://link1.jpg,https://link2.jpg,Indicado para,Dia a Dia
```

---

## 🔧 Configuração

1. Crie um arquivo `config.json` na raiz do projeto com o seguinte conteúdo:

```json
{
  "client_id": "SUA_CLIENT_ID_AQUI",
  "access_token": "SEU_ACCESS_TOKEN_AQUI",
  "base_url": "https://sandboxapi-marketplace.netshoes.com.br"
}
```

> ⚠️ **Este arquivo não deve ser versionado!** Ele está incluído no `.gitignore`.  
> Para referência da equipe, use o arquivo `config.example.json`.

---

## ▶️ Como executar

1. Certifique-se de que você tem o Python instalado (versão 3.7 ou superior)
2. Instale as dependências:

```bash
pip install requests
```

3. Execute o script principal:

```bash
python cadastrar_produtos_netshoes.py
```

---

## 📋 Requisitos

- Python 3.7 ou superior
- Biblioteca `requests` (instalável via pip)

---

## 🛡️ Aviso

⚠️ **Nunca envie o arquivo `config.json` para repositórios públicos!**  
Ele contém dados sensíveis como seu token de acesso e identificador de cliente.

✔️ O `.gitignore` já está configurado para ignorar esse arquivo.  
✔️ Sempre utilize `config.example.json` como base para compartilhar o formato do arquivo com outras pessoas.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
