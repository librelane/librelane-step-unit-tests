import re
import subprocess


def handle(step):

    for spef_file in step.state_out["spef"].values():
        with open("run_openroad.tcl", "w") as f:
            f.write(f"read_lef {step.config['TECH_LEFS']['nom_*']}\n")
            lib = step.config["LIB"]["*_tt_025C_1v80"][0]
            f.write(f"read_liberty {lib}\n")
            for lef in step.config["CELL_LEFS"]:
                f.write(f"read_lef {lef}\n")
            f.write(f"read_def {step.state_out['def']}\n")
            f.write(f"read_spef {spef_file}\n")
            f.write("report_parasitic_annotation -report_unannotated > out.log\n")

        result = subprocess.run(
            ["openroad", "-exit", "run_openroad.tcl"], capture_output=True
        )

        assert result.returncode == 0, f"Error encounted during reading {spef_file}"
        unannotated_pattern = r"Found (\d+).*unannotated.*"
        log = open("out.log").readlines()
        matches = [
            re.match(unannotated_pattern, line).group(1)
            for line in log
            if re.match(unannotated_pattern, line)
        ]
        expected = ["0", "0"]
        assert matches == expected, f"Found unannotated nets during reading {spef_file}"
