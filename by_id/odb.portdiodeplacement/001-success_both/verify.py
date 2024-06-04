import os
from typing import List, Literal

from openlane.steps.odb import OdbpyStep
from openlane.config import Variable


class VerifyStep(OdbpyStep):
    id = "Verify"
    name = "Verify"

    config_vars = [
        Variable(
            "DIODE_ON_PORTS",
            Literal["none", "in", "out", "both"],
            "Always insert diodes on ports with the specified polarities.",
            default="none",
        )
    ]

    def get_script_path(self):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), "verify-odb.py")

    def get_command(self) -> List[str]:
        command = super().get_command()
        command += ["--polarity", self.config["DIODE_ON_PORTS"]]
        return command

    def get_subcommand(self) -> List[str]:
        return []
