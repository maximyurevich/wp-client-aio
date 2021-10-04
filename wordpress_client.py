"""Wordpress REST API Client."""
import json
import logging
from typing import Optional, Union

import aiohttp
from aiohttp.client import ClientSession
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)


class WordpressRestApiClient:
    """Wordpress REST API Client."""

    url: str

    def __init__(self, url, user, password) -> None:
        """Set Wordpress url, user and password.

        Args:
            url: Wordpress REST API url
            user: Wordpress username
            password: Wordpreess password
        """
        self.url = url
        self.auth = aiohttp.BasicAuth(user, password)

    async def get(
        self,
        client: ClientSession,
        /, *,
        endpoint: Union[str, int] = ""
    ) -> str:
        """GET method.

        Args:
            endpoint (Optional[int], optional): endpoint url
        """
        async with client.get(
                f"{self.url}/{endpoint}",
                auth=self.auth) as resp:
            response = await resp.json()
            logging.info(json.dumps(response, indent=4))
            return response

    async def post(
        self,
        client: ClientSession,
        /, *,
        payload: dict[str, str]
    ) -> str:
        """POST method.

        Args:
            payload (dict[str, str]): dictionary payload for POST method
        """
        async with client.post(
            f"{self.url}",
            json=payload,
            auth=self.auth
        ) as resp:
            response = await resp.json()
            logging.info(response)
            return response

    async def patch(
        self,
        client: ClientSession,
        /, *,
        endpoint: Optional[Union[str, int]],
        payload: dict[str, str]
    ) -> str:
        """PATCH method.

        Args:
            endpoint (int): endpoint for PATCH method
            payload (dict[str, str]): dictionary payload for PATCH method
        Returns:

        """
        async with client.patch(
            f"{self.url}/{endpoint}",
            json=payload,
            auth=self.auth
        ) as resp:
            response = await resp.json()
            logging.info(response)
            return response

    async def put(
        self,
        client: ClientSession,
        /, *,
        endpoint: Optional[Union[str, int]],
        payload: dict[str, str]
    ) -> str:
        """PUT method.

        Args:
            endpoint (int): endpoint for PUT method
            payload (dict[str, str]): dictionary payload for PUT method
        """
        async with client.put(
            f"{self.url}/{endpoint}",
            json=payload,
            auth=self.auth
        ) as resp:
            response = await resp.json()
            logging.info(response)
            return response

    async def delete(
            self,
            client: ClientSession,
            /, *,
            endpoint: Optional[Union[str, int]]) -> str:
        """DELETE method.

        Args:
            endpoint (int): endpoint for DELETE method
        """
        async with client.delete(
            f"{self.url}/{endpoint}",
            auth=self.auth
        ) as resp:
            response = await resp.json()
            logging.info(response)
            return response
