import os

from typing import List, Optional, Tuple
from decimal import Decimal

from openlane.steps.odb import OdbpyStep
from openlane.config import Variable
from openlane.steps import TclStep


class VerifyStep(OdbpyStep):
    id = "Verify"
    name = "Verify"

    config_vars = [
        Variable(
            "FP_OBSTRUCTIONS",
            Optional[List[Tuple[Decimal, Decimal, Decimal, Decimal]]],
            "Obstructions applied at floorplanning stage. These affect row generation and hence affects cells placement.",
            units="µm",
        ),
    ]

    def get_script_path(self):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), "verify-odb.py")

    def get_command(self) -> List[str]:
        command = super().get_command()
        for obstruction in self.config["FP_OBSTRUCTIONS"]:
            command.append("--obstructions")
            command.append(TclStep.value_to_tcl(obstruction))
        return command

    def get_subcommand(self) -> List[str]:
        return []
