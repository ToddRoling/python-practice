LARGE_PACKAGE_SIZE = 5


def minimal_number_of_packages(item_count, available_large_packages, available_small_packages):

    if item_count < 0 or available_large_packages < 0 or available_small_packages < 0:
        return -1

    ideal_large_package_count = int(item_count / LARGE_PACKAGE_SIZE)
    ideal_small_package_count = int(item_count % LARGE_PACKAGE_SIZE)

    large_package_deficit = ideal_large_package_count - available_large_packages
    additional_small_packages = 0

    if large_package_deficit > 0:
        large_package_count = available_large_packages
        additional_small_packages = large_package_deficit * LARGE_PACKAGE_SIZE
    else:
        large_package_count = ideal_large_package_count

    small_package_count = ideal_small_package_count + additional_small_packages
    small_package_deficit = small_package_count - available_small_packages

    if small_package_deficit > 0:
        return -1
    return large_package_count + small_package_count


def test_minimal_number_of_packages():
    assert minimal_number_of_packages(109, 5, 100) == 89
    assert minimal_number_of_packages(409, 5, 100) == -1
    assert minimal_number_of_packages(10, 5, 100) == 2
    assert minimal_number_of_packages(10, 5, -100) == -1
    assert minimal_number_of_packages(-10, 5, -100) == -1
    assert minimal_number_of_packages(-10, 5, 100) == -1
    assert minimal_number_of_packages(-10, -5, 100) == -1
    assert minimal_number_of_packages(10, -5, 100) == -1
    assert minimal_number_of_packages(96846, 55, 777) == -1
    assert minimal_number_of_packages(96846, 55, 7777) == -1
    assert minimal_number_of_packages(96846, 19000, 1846) == 20846
    assert minimal_number_of_packages(9685, 19000, 1846) == 1937
    assert minimal_number_of_packages(5000, 19000, 0) == 1000
    assert minimal_number_of_packages(5000, 0, 19000) == 5000
    assert minimal_number_of_packages(5000, 0, 0) == -1
    assert minimal_number_of_packages(0, 0, 0) == 0
    assert minimal_number_of_packages(0, 50, 50) == 0
    assert minimal_number_of_packages(8888888888888, 555555555, 5555555555555555) == 8886666666668
