import subprocess


def handle(step):
    print(step.state_out["spef"])
    for corner in ["nom", "min", "max"]:
        spef_file = step.state_out["spef"][f"{corner}_*"]
        with open("run_sta.tcl", "w") as f:
            lib = step.config["LIB"]["*_tt_025C_1v80"][0]
            f.write(
                f"""
                read_liberty {lib}
                read_verilog {step.state_out['nl']}
                read_verilog ./spm.nl.v
                link_design manual_macro_placement_test
                read_spef {spef_file}
                read_spef -path spm_inst_0 ./spm.{corner}.spef
                read_spef -path spm_inst_1 ./spm.{corner}.spef
                report_parasitic_annotation -report_unannotated > out.log
                """
            )

        result = subprocess.run(["sta", "-exit", "run_sta.tcl"], capture_output=True)

        if result.stderr:
            for line in result.stderr.decode("utf-8").split("\n"):
                print(line)
        assert result.returncode == 0, f"Error encounted during reading {spef_file}"
        result = subprocess.run(
            [
                "openroad",
                "-exit",
                "-python",
                "./disconnected.py",
                step.state_out["odb"],
                "--unannotated-file",
                "out.log",
            ],
            capture_output=True,
        )

        if result.stderr:
            for line in result.stderr.decode("utf-8").split("\n"):
                print(line)
        assert result.returncode == 0, "Some nets were not properly annotated"
