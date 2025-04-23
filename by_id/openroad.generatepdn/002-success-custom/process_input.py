import os
import json
import fnmatch
import subprocess

__truefile__ = os.path.realpath(__file__)
__truedir__ = os.path.dirname(os.path.abspath(__file__))


def process_input(state_in, config, step_cls, pdk_root):
    state_in_parsed = json.loads(open(state_in).read())
    config_parsed = step_cls._load_config_from_file(config, pdk_root)

    def_in = state_in_parsed["def"]
    odb_out = state_in_parsed["odb"]

    corner = config_parsed["DEFAULT_CORNER"]

    tlef_list = []
    for pattern, file in config_parsed["TECH_LEFS"].items():
        if fnmatch.fnmatch(corner, pattern):
            tlef_list.append(file)
            break

    lef_reads = ""
    extra_lefs = config_parsed["EXTRA_LEFS"] or []
    macros_lefs = []
    if config_parsed["MACROS"]:
        macros_lefs = [
            lef
            for macro in config_parsed["MACROS"].keys()
            for lef in config_parsed["MACROS"][macro].lef
        ]
    lefs = tlef_list + config_parsed["CELL_LEFS"] + extra_lefs + macros_lefs
    lefs = filter(lambda x: x != "__librelane_dummy_path", lefs)
    for lef in lefs:
        lef_reads += f"read_lef {lef}; "

    with open("openroad_def2gds.tcl", "w", encoding="utf8") as f:
        f.write(f"{lef_reads} read_def {def_in}; write_db {odb_out};")

    subprocess.check_output(
        ["openroad", "-exit", "openroad_def2gds.tcl"],
        stderr=subprocess.STDOUT,
    )

    return state_in, config_parsed
