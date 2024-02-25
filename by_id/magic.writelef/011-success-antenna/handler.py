import subprocess


def handle(step):
    expected_count = 35

    lef = step.state_out["lef"]
    subprocess_result = subprocess.run(
        ["grep", "ANTENNAGATEAREA", lef], stdout=subprocess.PIPE, encoding="utf-8"
    )
    assert subprocess_result.returncode == 0, "Output LEF has no ANTENNAGATEAREA"
    property_count = subprocess_result.stdout.count("ANTENNAGATEAREA")
    assert (
        property_count == expected_count
    ), f"Expected {expected_count} ANTENNAGATEAREA but found {property_count}"
