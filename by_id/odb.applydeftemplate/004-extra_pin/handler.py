import os
import subprocess


def handle(step, exception):
    assert exception is not None, "An extra pin did not raise an exception"
    result = subprocess.call(
        [
            "grep",
            "not found in template layout, but found in design layout",
            os.path.join(step.step_dir, "odb-applydeftemplate.log"),
        ]
    )
    assert result == 0, "An extra pin did not report the correct error"
