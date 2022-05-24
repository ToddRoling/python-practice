from main.shipping_packages import minimal_number_of_packages


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
