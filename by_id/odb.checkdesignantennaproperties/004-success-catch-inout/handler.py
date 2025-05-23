from pprint import pformat
import yaml


def handle(step):
    expected = [{"cell": "spm", "inout": ["x[0]"], "input": [], "output": []}]
    with open(step.get_report_path()) as f:
        data = yaml.load(f, yaml.Loader)
        assert (
            data == expected
        ), f"Expected {pformat(expected)} but found {pformat(data)}"
