# =====================================
# generator=datazen
# version=3.2.3
# hash=839bb5a1117906e2660782d19b940f49
# =====================================

"""
A module aggregating package commands.
"""

# third-party
from vcorelib.args import CommandRegister as _CommandRegister

# internal
from conntextual.commands.client import add_client_cmd
from conntextual.commands.ui import add_ui_cmd


def commands() -> list[tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "client",
            "attempt to connect a client to a remote session",
            add_client_cmd,
        ),
        (
            "ui",
            "run a user interface for runtimepy applications",
            add_ui_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
