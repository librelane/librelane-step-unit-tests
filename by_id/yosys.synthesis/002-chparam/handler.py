import os
import json
import subprocess


def handle(step, test):
    json_path = os.path.join(step.step_dir, "parameterized_mux.nl.v.json")
    object = json.load(open(json_path))
    assert (
        len(object["modules"]["parameterized_mux"]["ports"]["A"]["bits"]) == 16
    ), "chparam did not work properly"

    if "synlig" in test:
        result = subprocess.call(
            ["grep", "UHDM", os.path.join(step.step_dir, "yosys-synthesis.log")]
        )
        assert result == 0, "Synlig was not used in the synthesis process"
