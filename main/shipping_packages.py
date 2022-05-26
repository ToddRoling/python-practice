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

