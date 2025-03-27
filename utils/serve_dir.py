# Created on 27/03/2025, 15:23
# Contributors:
#    INITIAL AUTHORS - initial API and implementation and/or initial documentation
#        :author:  Vincent Drouet
#    OTHER AUTHORS   - MACROSCOPIC CHANGES
"""A script that serves a the current directory over HTTP with a CORS header.

The files in the directory can be accessed from the JupyterLite tab.
For instance, to install a local wheel:
    import piplite
    await piplite.install("http://localhost:<port>/path/to/the/file.whl")
"""

from __future__ import annotations

import os
from argparse import ArgumentParser
from argparse import Namespace
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from http.server import test
from logging import getLogger
from pathlib import Path

LOGGER = getLogger(__name__)


class CORSRequestHandler(SimpleHTTPRequestHandler):  # noqa: D101
    def end_headers(self) -> None:  # noqa: D102
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleHTTPRequestHandler.end_headers(self)


def read_args() -> Namespace:
    """Parse the command-line arguments."""
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default=8000,
        help="The port on which to serve the directory (8000 by default).",
    )
    return parser.parse_args()


def serve():
    """Serve a directory."""
    args = read_args()
    test(
        CORSRequestHandler,
        HTTPServer,
        port=args.port,
    )


if __name__ == "__main__":
    serve()
