from database.models.collection import NewCollection
from database.models.client import Client


def test_valid_collection():
    client = Client(
        id="64b8f0f5e1d3f2a5c6b7d8e7",
        nombre="Model User",
        email="modeluser@example.com",
        telefono="1231231234",
    )
    collection = NewCollection(
        cliente_id=client.id,
        tarjeta_id="64b8f0f5e1d3f2a5c6b7d8ea",
        monto=100.0,
        fecha_intento="2023-08-01T12:00:00Z",
        status="approved",
        codigo_motivo="00",
        reembolsado=False,
        fecha_reembolso=None,
        nombre="Test Collection",
        descripcion="Test Description",
    )
    assert collection.cliente_id == client.id
    assert collection.nombre == "Test Collection"
    assert collection.descripcion == "Test Description"
