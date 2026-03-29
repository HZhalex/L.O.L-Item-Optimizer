# Quay lui nhánh cận (Hoàng Văn Hưng)
from models.item import Item
from utils.timer import Timer


def _upper_bound(level: int, current_gold: int, current_power: float,
                 sorted_items: list[Item], max_gold: int) -> float:
    """
    Tính cận trên (upper bound) bằng ý tưởng Fractional Knapsack.
    Từ level hiện tại, tham lam nhét phân số item còn lại để ước lượng
    giá trị tối đa có thể đạt được.
    """
    bound = current_power
    remaining_gold = max_gold - current_gold
    n = len(sorted_items)

    j = level
    while j < n and sorted_items[j].gold <= remaining_gold:
        remaining_gold -= sorted_items[j].gold
        bound += sorted_items[j].power
        j += 1

    # Nhét phân số item tiếp theo (nếu còn)
    if j < n:
        bound += sorted_items[j].power * (remaining_gold / sorted_items[j].gold)

    return bound


def solve(items: list[Item], max_gold: int) -> dict:
    """
    Trả về dict:
    {
        "selected_items": list[Item],  # Danh sách trang bị được chọn
        "total_power":    float,       # Tổng Sức Mạnh đạt được
        "gold_used":      int,         # Tổng Vàng đã dùng
        "gold_remaining": int,         # Vàng còn dư
        "exec_time_ms":   float,       # Thời gian thực thi (mili-giây)
    }
    """
    timer = Timer()
    timer.start()

    n = len(items)

    # Xử lý biên: không có item hoặc ngân sách = 0
    if n == 0 or max_gold <= 0:
        exec_time = timer.stop()
        return {
            "selected_items": [],
            "total_power":    0.0,
            "gold_used":      0,
            "gold_remaining": max_gold,
            "exec_time_ms":   exec_time,
        }

    # 1) Tiền xử lý: sắp xếp item theo ratio (power/gold) giảm dần
    #    Giữ lại chỉ số gốc để truy vết
    indexed_items = list(enumerate(items))  # (original_index, item)
    indexed_items.sort(key=lambda x: x[1].ratio(), reverse=True)

    sorted_items = [item for _, item in indexed_items]
    original_indices = [idx for idx, _ in indexed_items]

    # 2) DFS với pruning (dùng stack tường minh tránh tràn đệ quy)
    #    Mỗi node trên stack: (level, current_gold, current_power, selected_flags)
    best_power = 0.0
    best_selected = []

    # Stack khởi tạo: bắt đầu từ level 0, chưa chọn gì
    stack = [(0, 0, 0.0, [])]

    while stack:
        level, current_gold, current_power, selected = stack.pop()

        # Nếu đã duyệt hết tất cả item → kiểm tra cập nhật nghiệm
        if level == n:
            if current_power > best_power:
                best_power = current_power
                best_selected = selected[:]
            continue

        # Tính cận trên cho nhánh hiện tại
        bound = _upper_bound(level, current_gold, current_power,
                             sorted_items, max_gold)

        # Pruning: nếu bound <= best_power thì bỏ nhánh
        if bound <= best_power:
            continue

        # Nhánh KHÔNG chọn item ở level hiện tại (đẩy vào stack trước → xử lý sau)
        stack.append((level + 1, current_gold, current_power, selected))

        # Nhánh CHỌN item ở level hiện tại
        item = sorted_items[level]
        new_gold = current_gold + item.gold
        if new_gold <= max_gold:
            new_power = current_power + item.power
            new_selected = selected + [level]
            # Cập nhật nghiệm tốt nhất ngay khi tìm thấy
            if new_power > best_power:
                best_power = new_power
                best_selected = new_selected[:]
            stack.append((level + 1, new_gold, new_power, new_selected))

    # 3) Truy vết: chuyển các chỉ số sorted về item gốc
    selected_items = [items[original_indices[i]] for i in best_selected]
    gold_used = sum(item.gold for item in selected_items)

    exec_time = timer.stop()

    return {
        "selected_items": selected_items,
        "total_power":    best_power,
        "gold_used":      gold_used,
        "gold_remaining": max_gold - gold_used,
        "exec_time_ms":   exec_time,
    }