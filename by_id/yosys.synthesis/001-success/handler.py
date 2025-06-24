import os
import subprocess


def handle(step, test):
    if "slang" in test:
        result = subprocess.call(
            ["grep", "SLANG frontend", os.path.join(step.step_dir, "yosys-synthesis.log")],
        )
        assert result == 0, "Slang was not used in the synthesis process"
