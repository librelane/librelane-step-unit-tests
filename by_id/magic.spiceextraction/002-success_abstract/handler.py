import subprocess


def handle(step):
    spice_output = step.state_out["spice"]
    cmd = ["grep", "Black-box entry subcircuit for spm abstract view", spice_output]
    result = subprocess.run(cmd)
    assert result.returncode == 0, "Magic did not black-box cell spm"
    cmd = [
        "grep",
        "Black-box entry subcircuit for sky130_fd_sc_hd__clkbuf_2 abstract view",
        spice_output,
    ]
    result = subprocess.run(cmd)
    assert (
        result.returncode == 0
    ), "Magic did not black-box cell sky130_fd_sc_hd__clkbuf_2"
