"""Test Branch and Bound - Hoàng Văn Hưng"""
import sys
sys.path.insert(0, '.')
from models.item import Item
from algorithms.branch_and_bound import solve


def test_basic():
    items = [
        Item('Vo Cuc Kiem', 3400, 80),
        Item('Mu Phu Thuy', 3600, 120),
        Item('Giap Mau', 2900, 60),
        Item('Giay Nhanh', 1100, 30),
        Item('Kiem Sat Thu', 3200, 90),
    ]
    r = solve(items, 7000)
    print(f"[Basic] power={r['total_power']}, gold={r['gold_used']}, "
          f"remaining={r['gold_remaining']}, items={[i.name for i in r['selected_items']]}, "
          f"time={r['exec_time_ms']:.4f}ms")
    # Kiem tra: Mu Phu Thuy(3600,120) + Kiem Sat Thu(3200,90) = 6800 gold, 210 power
    assert r['total_power'] == 210.0
    assert r['gold_used'] == 6800
    assert r['gold_remaining'] == 200


def test_zero_gold():
    items = [Item('A', 100, 50)]
    r = solve(items, 0)
    print(f"[W=0] power={r['total_power']}, items={r['selected_items']}")
    assert r['total_power'] == 0.0
    assert r['selected_items'] == []
    assert r['gold_remaining'] == 0


def test_empty_items():
    r = solve([], 10000)
    print(f"[Empty] power={r['total_power']}, items={r['selected_items']}")
    assert r['total_power'] == 0.0
    assert r['selected_items'] == []
    assert r['gold_remaining'] == 10000


def test_all_fit():
    items = [
        Item('A', 1000, 50),
        Item('B', 2000, 80),
        Item('C', 1500, 60),
    ]
    r = solve(items, 100000)
    print(f"[AllFit] power={r['total_power']}, gold={r['gold_used']}, "
          f"items={[i.name for i in r['selected_items']]}")
    assert r['total_power'] == 190.0
    assert r['gold_used'] == 4500


def test_single_item_fits():
    items = [Item('X', 500, 100)]
    r = solve(items, 500)
    print(f"[Single] power={r['total_power']}, items={[i.name for i in r['selected_items']]}")
    assert r['total_power'] == 100.0
    assert r['gold_used'] == 500


def test_single_item_no_fit():
    items = [Item('X', 500, 100)]
    r = solve(items, 499)
    print(f"[NoFit] power={r['total_power']}, items={r['selected_items']}")
    assert r['total_power'] == 0.0


def test_performance():
    """Test voi 30 items de dam bao khong bi vong lap vo han."""
    import random
    random.seed(42)
    items = [Item(f'Item_{i}', random.randint(500, 5000), random.randint(20, 200))
             for i in range(30)]
    r = solve(items, 15000)
    print(f"[Perf-30] power={r['total_power']}, gold={r['gold_used']}, "
          f"items={len(r['selected_items'])}, time={r['exec_time_ms']:.4f}ms")
    assert r['total_power'] > 0
    assert r['gold_used'] <= 15000
    assert r['exec_time_ms'] < 10000  # phai chay duoi 10 giay


if __name__ == '__main__':
    test_basic()
    test_zero_gold()
    test_empty_items()
    test_all_fit()
    test_single_item_fits()
    test_single_item_no_fit()
    test_performance()
    print("\n=== ALL TESTS PASSED ===")
