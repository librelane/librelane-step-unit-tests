from pprint import pformat
import yaml


def handle(step):
    expected = [{"cell": "spm", "inout": [], "input": [], "output": ["p"]}]
    with open(step.get_report_path()) as f:
        data = yaml.load(f, yaml.Loader)
        assert (
            data == expected
        ), f"Expected {pformat(expected)} but found {pformat(data)}"
