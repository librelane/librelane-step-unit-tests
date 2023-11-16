# Copyright 2023 Efabless Corporation
#
# This file is part of the DFFRAM Memory Compiler.
# See https://github.com/Cloud-V/DFFRAM for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import namedtuple

from openlane.scripts.odbpy.reader import click_odb, click


@click.option("--unannotated-file")
@click.command()
@click_odb
def main(reader, unannotated_file):
    Net = namedtuple("Net", "name bterms")
    BTerm = namedtuple("BTerm", "name type")

    db = reader.db
    block = db.getChip().getBlock()
    nets = block.getNets()

    file_content = []
    with open(unannotated_file, "r") as f:
        file_content = f.readlines()

    reported_nets = [
        line.rstrip().lstrip() for line in file_content if line.startswith(" ")
    ]
    matched_nets = [
        Net(
            name=net.getName(),
            bterms=[
                BTerm(bterm.getName(), bterm.getIoType()) for bterm in net.getBTerms()
            ],
        )
        for net in nets
        if (net.getName() in reported_nets) and net.getITerms() is not []
    ]
    if len(matched_nets) == len(reported_nets):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
