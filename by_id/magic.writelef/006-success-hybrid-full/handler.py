import subprocess


def handle(step):
    assert step.config["MAGIC_WRITE_FULL_LEF"] is True
    with open("run_openroad.tcl", "w") as f:
        f.write(f"read_lef {step.config['TECH_LEFS']['nom_*']}\n")
        f.write(f"read_lef {step.state_out['lef']}\n")
    result = subprocess.run(
        ["openroad", "-exit", "run_openroad.tcl"], capture_output=True
    )

    print(result.stdout.decode("utf-8"))
    assert "ERROR (LEFPARS" not in result.stdout.decode(
        "utf-8"
    ), "Error encounted during reading {step.state_out['lef']}"
