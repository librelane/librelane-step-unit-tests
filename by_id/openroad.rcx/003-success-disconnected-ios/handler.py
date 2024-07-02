import os
import subprocess
from typing import List

from openlane.common import get_script_dir
from openlane.steps.odb import OdbpyStep
from openlane.steps.step import StepError


class CheckDisconnectedStep(OdbpyStep):
    id = "CheckDisconnected"
    name = "Check Disconnected"
    config_vars = []

    outputs = []

    def get_script_path(self):
        return os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "disconnected.py"
        )

    def get_command(self) -> List[str]:
        return super().get_command() + [
            "--unannotated-file",
            "out.log",
        ]

    def get_subcommand(self) -> List[str]:
        return []


def handle(step):
    print(step.state_out["spef"])

    env = os.environ.copy()
    env["PYTHONPATH"] = (
        f"{env.get('PYTHONPATH', '')}:{os.path.join(get_script_dir(), 'odbpy')}"
    )
    for corner in ["nom", "min", "max"]:
        print(f"--- Corner {corner} --- ")
        spef_file = step.state_out["spef"][f"{corner}_*"]
        with open("run_sta.tcl", "w") as f:
            f.write(
                open("run_sta.tcl.tpl")
                .read()
                .format(
                    lib=step.config["LIB"]["*_tt_025C_1v80"][0],
                    nl=step.state_out["nl"],
                    spef_file=spef_file,
                    corner=corner,
                )
            )

        print("=== Running STA ===")
        result = subprocess.run(
            ["sta", "-exit", "run_sta.tcl"],
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
        print(result.stdout)
        assert result.returncode == 0, f"Error encounted during reading {spef_file}"

        print("=== Running Check ===")
        check_exception = None
        try:
            step = CheckDisconnectedStep(step.config, step.state_out)
            step.start(step_dir=os.path.join(".", corner), _no_rule=True)
        except StepError as e:
            check_exception = e
        assert check_exception is None, "Some nets were not properly annotated"
