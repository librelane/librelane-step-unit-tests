import odb
import json
import sys

args = sys.argv[1:]
db = odb.dbDatabase.create()
odb.read_db(db, args[0])

spm_macro = json.loads(args[1])

block = db.getChip().getBlock()
dbu = block.getDefUnits()
insts = {inst.getName(): inst for inst in block.getInsts()}

orientation_as_r = {"N": "R0", "S": "R180"}

for instance, info in spm_macro["instances"].items():
    assert (
        insts[instance].getPlacementStatus() == "FIRM"
    ), f"{instance} not placed properly"
    assert tuple([v / dbu for v in insts[instance].getLocation()]) == tuple(
        info["location"]
    ), f"{instance} not placed at the correct location"
    assert (
        insts[instance].getOrient() == orientation_as_r[info["orientation"]]
    ), f"{instance} not placed with the correct orientation"
