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
    if macros := config_parsed["MACROS"]:
        for _, info in macros.items():
            for lef in info.lef:
                macros_lefs.append(lef)

    lefs = tlef_list + config_parsed["CELL_LEFS"] + extra_lefs + macros_lefs
    lefs = filter(lambda x: x != "__openlane_dummy_path", lefs)
    for lef in lefs:
        lef_reads += f"read_lef {lef}; "

    guides_read = ""
    if os.path.exists("guides"):
        guides_read = "read_guides guides; "

    with open("openroad_def2odb.tcl", "w", encoding="utf8") as f:
        f.write(f"{lef_reads} read_def {def_in}; {guides_read} write_db {odb_out};")

    try:
        subprocess.check_output(
            ["openroad", "-exit", "openroad_def2odb.tcl"],
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        raise e from None

    return state_in, config_parsed
