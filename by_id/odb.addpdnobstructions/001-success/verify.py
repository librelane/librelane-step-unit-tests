import os

from typing import List

from openlane.steps.odb import AddPDNObstructions


class VerifyStep(AddPDNObstructions):
    id = "Verify"
    name = "Verify"

    def get_script_path(self):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), "verify-odb.py")

    def get_subcommand(self) -> List[str]:
        return []
