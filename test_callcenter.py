import pytest
from callcenter import main

alien_testcases = [
    ("Inputs/callcenter01.txt",[('A', 0, 2, 0), ('B', 0, 3, 0), ('C', 0, 2, 0), ('D', 0, 3, 0), ('E', 0, 5, 0), ('F', 2, 5, 2), ('G', 2, 4, 2), ('H', 10, 14, 0)]),
    ("Inputs/callcenter02.txt",[('A', 0, 2, 0), ('B', 0, 3, 0), ('C', 0, 2, 0), ('D', 2, 5, 2), ('E', 2, 7, 2), ('F', 3, 6, 3), ('G', 5, 7, 5), ('H', 10, 14, 0)]),
]

@pytest.mark.parametrize("filename, output",alien_testcases)
def test_alien(filename,output):
    assert main(filename) == output