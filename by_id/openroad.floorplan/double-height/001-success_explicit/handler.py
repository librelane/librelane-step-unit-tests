import os
import subprocess


def handle(step):
    result = subprocess.call(
        [
            "grep",
            "-E",
            "ROW\\s*+\\w+\\s*unithddbl",
            os.path.join(step.step_dir, "spm.def"),
        ],
    )
    assert result == 0, "could not create double-height rows properly"
