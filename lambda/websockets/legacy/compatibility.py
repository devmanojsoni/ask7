from __future__ import annotations

import asyncio
import sys
from typing import Any, Dict


__all__ = ["asyncio_timeout", "loop_if_py_lt_38"]


if sys.version_info[:2] >= (3, 8):

    def loop_if_py_lt_38(loop: asyncio.AbstractEventLoop) -> Dict[str, Any]:
        """
        Helper for the removal of the loop argument in Python 3.10.

        """
        return {}

else:

    def loop_if_py_lt_38(loop: asyncio.AbstractEventLoop) -> Dict[str, Any]:
        """
        Helper for the removal of the loop argument in Python 3.10.

        """
        return {"loop": loop}


if sys.version_info[:2] >= (3, 11):
    from asyncio import timeout as asyncio_timeout  # noqa: F401
else:
    from .async_timeout import timeout as asyncio_timeout  # noqa: F401
