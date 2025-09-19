from src.main import *
from unittest.mock import patch, MagicMock
import pytest


# Testa se a função retorna a mensagem esperada
@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello Word"}


# Testa se a função retorna número aleatório corretamente (simulado)
@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=987654):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatório": 987654}


# Testa se obter_clima retorna dados corretos quando a cidade existe
@pytest.mark.asyncio
async def test_obter_clima_sucesso():
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "name": "Curitiba",
        "main": {"temp": 25, "humidity": 82},
        "weather": [{"description": "céu limpo"}]
    }
    with patch("src.main.requests.get", return_value=fake_response):
        result = await obter_clima("Curitiba")

    assert result == {
        "cidade": "Curitiba",
        "temperatura": 25,
        "descricao": "céu limpo",
        "umidade": 82
    }


# Testa se obter_clima lança HTTPException quando a cidade não existe
@pytest.mark.asyncio
async def test_obter_clima_falha():
    fake_response = MagicMock()
    fake_response.status_code = 404
    fake_response.json.return_value = {"message": "city not found"}

    with patch("src.main.requests.get", return_value=fake_response):
        with pytest.raises(HTTPException) as exc_info:
            await obter_clima("CidadeInvalida")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Cidade não encontrada"


# Testa se a URL da API contém a cidade e a chave corretamente
@pytest.mark.asyncio
async def test_url_chamada_clima():
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "name": "Paris",
        "main": {"temp": 22, "humidity": 61},
        "weather": [{"description": "nublado"}]
    }
    with patch("src.main.requests.get", return_value=fake_response) as mock_get:
        await obter_clima("Paris")
        args,kwargs = mock_get.call_args
        assert "Paris" in args[0]
        assert "appid=" in args[0]