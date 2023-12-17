import os
import subprocess


def handle(step, exception):
    assert exception is not None, "Uninstantiated macro did not raise exception"
    result = subprocess.call(
        [
            "grep",
            "-E",
            "Declared macros not instantiated in design",
            os.path.join(step.step_dir, "odb-manualmacroplacement.log"),
        ],
    )
    assert result == 0, "did not print appropriate message"
