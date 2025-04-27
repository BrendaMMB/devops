from src.createdProducts import cadastrar_produto
from unittest.mock import patch
import pytest

def test_cadastrar_produto():
    assert cadastrar_produto(produto) == {f"✅ Produto com SKU {produto['sku']} cadastrado com sucesso."}

