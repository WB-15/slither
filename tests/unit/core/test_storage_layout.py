import json
from pathlib import Path
from subprocess import PIPE, Popen
from solc_select import solc_select
from slither import Slither

TEST_DATA_DIR = Path(__file__).resolve().parent / "test_data"
STORAGE_TEST_ROOT = Path(TEST_DATA_DIR, "storage_layout")


def test_storage_layout():
    # the storage layout has not yet changed between solidity versions so we will test with one version of the compiler
    solc_select.switch_global_version("0.8.10", always_install=True)
    test_item = Path(STORAGE_TEST_ROOT, "storage_layout-0.8.10.sol").as_posix()

    sl = Slither(test_item, solc_force_legacy_json=False, disallow_partial=True)

    with Popen(["solc", test_item, "--storage-layout"], stdout=PIPE) as process:
        for line in process.stdout:  # parse solc output
            if '{"storage":[{' in line.decode("utf-8"):  # find the storage layout
                layout = iter(json.loads(line)["storage"])
                while True:
                    try:
                        for contract in sl.contracts:
                            curr_var = next(layout)
                            var_name = curr_var["label"]
                            sl_name = contract.variables_as_dict[var_name]
                            slot, offset = contract.compilation_unit.storage_layout_of(
                                contract, sl_name
                            )
                            assert slot == int(curr_var["slot"])
                            assert offset == int(curr_var["offset"])
                    except StopIteration:
                        break
                    except KeyError as e:
                        print(f"not found {e} ")
