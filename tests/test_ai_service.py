"""
Tests unitarios para el servicio de IA.
Usa mocks para evitar llamadas reales a la API de OpenAI.
"""

import pytest

import ai_service


class DummyChoice:
    """Mock para simular la estructura de Choice de OpenAI."""
    def __init__(self, content):
        self.message = type('M', (), {'content': content})


class DummyResponse:
    """Mock para simular la respuesta de la API de OpenAI."""
    def __init__(self, content):
        self.choices = [DummyChoice(content)]


class DummyChat:
    """Mock para simular el objeto chat de OpenAI."""
    def __init__(self, content):
        self._content = content

    def completions(self, **kwargs):
        # emulate the chain client.chat.completions.create(**params)
        return DummyResponse(self._content)


class DummyClient:
    """Mock principal del cliente OpenAI."""
    def __init__(self, api_key, content):
        self.api_key = api_key
        self.chat = type('C', (), {'completions': type('X', (), {'create': lambda *a, **k: DummyResponse(content)})})()


def test_no_api_key(monkeypatch):
    """
    Prueba el comportamiento cuando no hay API key configurada.
    Debe retornar un mensaje de error apropiado.
    """
    # Force client with no api_key
    monkeypatch.setattr(ai_service, 'client', DummyClient(api_key=None, content="- a\n- b"))
    res = ai_service.create_simple_tasks("Descripción")
    assert res == ["Error: OpenAI API key is not configured."]


def test_successful_parse(monkeypatch):
    """
    Prueba el parsing exitoso de la respuesta de la API.
    Verifica que las subtareas se extraen correctamente del formato con guiones.
    """
    content = "- Subtarea uno\n- Subtarea dos\n- Subtarea tres"
    # client with api key and returns content
    monkeypatch.setattr(ai_service, 'client', DummyClient(api_key='x', content=content))
    res = ai_service.create_simple_tasks("Descripción")
    assert isinstance(res, list)
    assert res == ["Subtarea uno", "Subtarea dos", "Subtarea tres"]


def test_api_exception(monkeypatch):
    """
    Prueba el manejo de errores cuando la API falla.
    Verifica que se devuelve un mensaje de error apropiado.
    """
    class BadClient:
        api_key = 'x'
        class chat:
            class completions:
                @staticmethod
                def create(**kwargs):
                    raise RuntimeError("API fallo")

    monkeypatch.setattr(ai_service, 'client', BadClient())
    res = ai_service.create_simple_tasks("Descripción")
    assert res and res[0].startswith("Error:")
