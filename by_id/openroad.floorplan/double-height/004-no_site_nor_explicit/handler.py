import os
import subprocess


def handle(step, exception):
    result = subprocess.call(
        [
            "grep",
            "-E",
            f"ROW\\s*+\\w+\\s*unithddbl",
            os.path.join(step.step_dir, "spm.def"),
        ],
    )
    assert result == 1, "double-height rows magically created"
