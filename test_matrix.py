import pytest
from matrix import main

matrix_testcases = [
    ("Inputs/matrix01.txt", [[190,  330,  330,  330,  250], [690,  1200, 1200, 1200, 910], [880,  1560, 1560, 1560, 1200], [1030, 1860, 1860, 1860, 1450], [530,  990,  990,  990,  790]])
]

@pytest.mark.parametrize("filename, output",matrix_testcases)
def test_matrix(filename,output):
    assert main(filename) == output