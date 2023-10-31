import subprocess


def handle(step):
    result = subprocess.call(
        ["klayout", "-zz", step.state_out["mag_gds"]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    assert result == 0, "Couldn't open generated GDS."
