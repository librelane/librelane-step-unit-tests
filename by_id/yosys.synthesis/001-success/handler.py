import os
import subprocess


def handle(step, test):
    if "synlig" in test:
        result = subprocess.call(
            ["grep", "UHDM", os.path.join(step.step_dir, "yosys-synthesis.log")],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        assert result == 0, "Synlig was not used in the synthesis process"
