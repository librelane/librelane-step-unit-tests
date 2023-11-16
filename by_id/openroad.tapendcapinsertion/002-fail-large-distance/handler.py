import re


def handle(step, exception, caplog):
    endcap_pattern = r".*Inserted +(\d+) +endcaps."
    log = open(step.get_log_path()).readlines()  # caplog is empty ?
    endcap_count = [
        re.match(endcap_pattern, line).group(1)
        for line in log
        if re.match(endcap_pattern, line)
    ]
    assert int(endcap_count[0]) > 0, "Didn't insert endcap cells"

    tapcell_pattern = r".*Inserted +(\d+) +tapcells."
    log = open(step.get_log_path()).readlines()  # caplog is empty ?
    tapcell_count = [
        re.match(tapcell_pattern, line).group(1)
        for line in log
        if re.match(tapcell_pattern, line)
    ]
    assert int(tapcell_count[0]) == 0, "Inserted tapcells cells"
