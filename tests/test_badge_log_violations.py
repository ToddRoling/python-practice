from src.pythonpractice.badge_log_violations import get_badge_log_violations


def test_get_badge_log_violations_0():
    badge_records_0 = [
        ["Martha", "exit"],
        ["Paul", "enter"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "enter"],
        ["Paul", "enter"],
        ["Curtis", "exit"],
        ["Curtis", "enter"],
        ["Paul", "exit"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "exit"],
        ["Paul", "enter"],
        ["Paul", "enter"],
        ["Martha", "exit"]
    ]
    actual_result = get_badge_log_violations(badge_records_0)
    expected_result = {"Curtis", "Paul"}, {"Martha", "Curtis"}
    assert actual_result == expected_result


def test_get_badge_log_violations_1():
    badge_records_1 = [["Paul", "enter"], ["Paul", "enter"], ["Paul", "exit"]]
    actual_result = get_badge_log_violations(badge_records_1)
    expected_result = {"Paul"}, set()
    assert actual_result == expected_result


def test_get_badge_log_violations_2():
    badge_records_2 = [["Paul", "enter"], ["Paul", "exit"], ["Paul", "exit"]]
    actual_result = get_badge_log_violations(badge_records_2)
    expected_result = set(), {"Paul"}
    assert actual_result == expected_result


def test_get_badge_log_violations_3():
    badge_records_3 = [
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Paul", "exit"],
        ["Paul", "enter"],
        ["Martha", "enter"],
        ["Martha", "exit"]
    ]
    actual_result = get_badge_log_violations(badge_records_3)
    expected_result = {"Paul"}, {"Paul"}
    assert actual_result == expected_result


def test_get_badge_log_violations_4():
    badge_records_4 = [
        ["Paul", "enter"],
        ["Paul", "exit"]
    ]
    actual_result = get_badge_log_violations(badge_records_4)
    expected_result = set(), set()
    assert actual_result == expected_result


def test_get_badge_log_violations_5():
    badge_records_5 = [
        ["Paul", "enter"],
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Paul", "exit"]
    ]
    actual_result = get_badge_log_violations(badge_records_5)
    expected_result = {"Paul"}, {"Paul"}
    assert actual_result == expected_result


def test_get_badge_log_violations_6():
    badge_records_6 = [
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Paul", "exit"],
        ["Paul", "enter"]]
    actual_result = get_badge_log_violations(badge_records_6)
    expected_result = {"Paul"}, {"Paul"}
    assert actual_result == expected_result
