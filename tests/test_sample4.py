import sys
import os
sys.path.append((os.path.join(os.path.dirname(__file__), '..')))
from hw2_debugging_fixed import merge_sort
def test_case():
    test_array = [1,2,3]
    assert merge_sort(test_array) == [1,2,3]