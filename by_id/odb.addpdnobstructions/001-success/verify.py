import os

from typing import List, Tuple

from openlane.steps.odb import OdbpyStep, AddPDNObstructions
from openlane.steps.step import MetricsUpdate, ViewsUpdate


class VerifyStep(OdbpyStep):
    id = "Verify"
    name = "Verify"

    config_vars = AddPDNObstructions.config_vars

    def get_script_path(self):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), "verify-odb.py")

    def get_subcommand(self) -> List[str]:
        return []

    def get_obstruction_variable(self):
        return self.config_vars[0]

    def get_command(self) -> List[str]:
        command = super().get_command()
        if obstructions := self.config[self.config_vars[0].name]:
            for obstruction in obstructions:
                command.append("--obstructions")
                command.append(obstruction)
        return command

    def run(self, state_in, **kwargs) -> Tuple[ViewsUpdate, MetricsUpdate]:
        f"{self.get_obstruction_variable().name} is not defined. Skipping {self.id}…"
        return super().run(state_in, **kwargs)
