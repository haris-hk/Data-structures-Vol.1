import pytest
from sorting import main

sorting_testcases = [
    ("Inputs/sorting01.txt", [10, 13, 22, 39, 46, 48, 55, 99] ),
    ("Inputs/sorting02.txt",[13, 96, 534, 777, 875, None, None, None, None, None]),
    ("Inputs/sorting03.txt", [None, None, None, None, None] )

]

@pytest.mark.parametrize("filename, output",sorting_testcases)
def test_sorting(filename,output):
    assert main(filename) == output