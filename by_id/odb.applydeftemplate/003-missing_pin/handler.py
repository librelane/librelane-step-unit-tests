import os
import subprocess


def handle(step, exception):
    assert exception is not None, "A missing pin did not raise an exception"
    result = subprocess.call(
        [
            "grep",
            "not found in design layout, but found in template layout",
            os.path.join(step.step_dir, "odb-applydeftemplate.log"),
        ]
    )
    assert result == 0, "A missing pin did not print the correct error"
