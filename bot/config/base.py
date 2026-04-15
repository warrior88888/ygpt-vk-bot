from typing import Annotated, Literal

from pydantic import Field

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

PortInt = Annotated[int, Field(gt=0, le=65535)]

local_ips = ["127.0.0.1", "localhost", "0.0.0.0"]
