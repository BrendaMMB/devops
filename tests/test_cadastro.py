import pytest
from unittest.mock import patch
from src.createdProducts import cadastrar_produto, cadastrar_preco, cadastrar_estoque

# Exemplo de um produto fictício para teste
produto_exemplo = {
    "sku": "BR_0000_00",
    "productGroup": "0000",
    "department": "Test",
    "productType": "Sapato",
    "brand": "MarcaTeste",
    "name": "Produto Teste",
    "description": "Descrição Teste",
    "color": "Preto",
    "gender": "Unissex",
    "manufacturerCode": "12345",
    "size": "40",
    "eanIsbn": "1234567890123",
    "height": "10",
    "width": "20",
    "depth": "30",
    "weight": "1",
    "image1": "https://img1.com",
    "image2": "https://img2.com",
    "attribute_name": "Categoria",
    "attribute_value": "Teste",
    "listPrice": "199.99",
    "salePrice": "179.99",
    "stockQuantity": "10"
}

@patch("src.createdProducts.requests.post")
def test_cadastrar_produto_sucesso(mock_post):
    mock_post.return_value.status_code = 202

    resposta = cadastrar_produto(produto_exemplo)

    assert resposta["status"] == "sucesso"
    assert "Status 202" in resposta["detalhes"]

@patch("src.createdProducts.requests.post")
def test_cadastrar_preco_sucesso(mock_post):
    mock_post.return_value.status_code = 202

    resposta = cadastrar_preco(produto_exemplo)

    assert resposta["status"] == "sucesso"
    assert "Status 202" in resposta["detalhes"]

@patch("src.createdProducts.requests.post")
def test_cadastrar_estoque_sucesso(mock_post):
    mock_post.return_value.status_code = 202

    resposta = cadastrar_estoque(produto_exemplo)

    assert resposta["status"] == "sucesso"
    assert "Status 202" in resposta["detalhes"]
