import pytest
from alien import main

alien_testcases = [
    ("Inputs/alien01.txt","Hello World"),
    ("Inputs/alien02.txt","Hi, Hello"),
]

@pytest.mark.parametrize("filename, output",alien_testcases)
def test_alien(filename,output):
    assert main(filename) == output