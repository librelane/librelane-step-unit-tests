import os
import subprocess


def handle(step, test):
    assert (
        step.state_out.metrics["synthesis__check_error__count"] == 1
    ), f"Expected 1 synthesis__check_error__count but found: {step.state_out.metrics['synthesis__check_error__count']}"
    if "synlig" in test:
        result = subprocess.call(
            ["grep", "UHDM", os.path.join(step.step_dir, "yosys-synthesis.log")],
        )
        assert result == 0, "Synlig was not used in the synthesis process"
