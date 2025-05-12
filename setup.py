# =====================================
# generator=datazen
# version=3.2.3
# hash=ab7a1a8c9f2c61e4a441d1d5c7ea1dd8
# =====================================

"""
conntextual - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from conntextual_bootstrap.setup import setup  # type: ignore

# internal
from conntextual import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughn@libre-embedded.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.12",
        "3.13",
    ],
}
setup(
    pkg_info,
    author_info,
)
