from pathlib import Path

import pkg_resources
from pydantic import BaseSettings


class LocalConfig(BaseSettings):
    # Provide a path to the book server files. The leading underscore prevents environment variables from affecting this value. See the `docs <https://pydantic-docs.helpmanual.io/usage/models/#automatically-excluded-attributes>`_, which don't say this explicitly, but testing confirms it.
    _book_server_path: str = str(
        Path(pkg_resources.resource_filename("rsptx.book_server_api", "")).absolute()
    )


local_settings = LocalConfig()
