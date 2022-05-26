def print_pyramid(height, building_block):

    space = ' ' * len(building_block)

    for i in range(height):
        spaces = space * (height - i - 1)
        blocks = building_block * (i * 2 + 1)
        print(spaces + blocks)
