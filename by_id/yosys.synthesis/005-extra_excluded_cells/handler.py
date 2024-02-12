import os
import json
import shutil
import subprocess


def handle(step, test):
    json_path = os.path.join(step.step_dir, "parameterized_mux.nl.v.json")
    object = json.load(open(json_path))
    for cell_data in object["modules"]["parameterized_mux"]["cells"].values():
        assert not cell_data["type"].startswith(
            "sky130_fd_sc_hd__mux2_"
        ), "EXTRA_EXCLUDED_CELLS did not work properly"

    if "synlig" in test:
        result = subprocess.call(
            ["grep", "UHDM", os.path.join(step.step_dir, "yosys-synthesis.log")]
        )
        assert result == 0, "Synlig was not used in the synthesis process"
