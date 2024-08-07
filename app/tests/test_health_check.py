from fastapi import status
from httpx import AsyncClient

from app.main import app


async def test_health_check_status_code(client: AsyncClient) -> None:
    response = await client.get(
        app.url_path_for("health_check"),
    )

    assert response.status_code == status.HTTP_200_OK


async def test_health_check_response(client: AsyncClient) -> None:
    response = await client.get(
        app.url_path_for("health_check"),
    )

    assert response.json() == {"status": "ok"}
