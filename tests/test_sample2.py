import sys
import os
sys.path.append((os.path.join(os.path.dirname(__file__), '..')))
from hw2_debugging_fixed import merge_sort
def test_case():
    test_array = [0,-2,5,6,6,3,32,33,12,11,-1,1,1,1,1,6,-33,2,3.6,5,2.8,10,11]
    assert merge_sort(test_array) == [-33,-2,-1,0, 1, 1, 1, 1, 2, 2.8, 3, 3.6, 5, 5, 6, 6, 6, 10, 11, 11, 12, 32, 33]