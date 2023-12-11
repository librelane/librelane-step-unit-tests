import os
import subprocess

from openlane.common import get_script_dir


def handle(step):
    print(step.state_out["spef"])

    env = os.environ.copy()
    env[
        "PYTHONPATH"
    ] = f"{env.get('PYTHONPATH', '')}:{os.path.join(get_script_dir(), 'odbpy')}"
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
        result = subprocess.run(
            [
                "openroad",
                "-exit",
                "-python",
                "./disconnected.py",
                step.state_out["odb"],
                "--unannotated-file",
                "out.log",
            ],
            stderr=subprocess.STDOUT,
            env=env,
        )
        print(result.stdout)
        assert result.returncode == 0, "Some nets were not properly annotated"
