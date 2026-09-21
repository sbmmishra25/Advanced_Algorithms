from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    spec = spec_from_file_location("algo", ROOT / rel)
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def test_sorting_catalog():
    m = load("02-searching-and-sorting/python/sorting_catalog.py")
    expected = sorted([5, 1, 4, 2, 8, 0, 2])
    for fn in [m.bubble_sort, m.insertion_sort, m.selection_sort, m.quick_sort, m.heap_sort]:
        a = [5, 1, 4, 2, 8, 0, 2]
        fn(a)
        assert a == expected
    assert m.merge_sort([5, 1, 4, 2, 8, 0, 2]) == expected
    assert m.counting_sort([5, 1, 4, 2, 8, 0, 2]) == expected
    assert m.radix_sort_nonnegative([170, 45, 75, 90, 802, 24, 2, 66]) == sorted([170,45,75,90,802,24,2,66])

def test_searching_catalog():
    m = load("02-searching-and-sorting/python/searching_catalog.py")
    a = [1, 3, 3, 5, 8, 13]
    assert m.linear_search(a, 5) == 3
    assert m.binary_search(a, 8) == 4
    assert m.lower_bound(a, 3) == 1
    assert m.upper_bound(a, 3) == 3
    assert m.quickselect(a[:], 2) == 3
