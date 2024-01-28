def is_intersecting(new_circle, group):
    if len(group) == 0:  # for first circle
        return True
    for circle in group:
        if ((circle[0] - new_circle[0]) ** 2 + (circle[1] - new_circle[1]) ** 2) ** (1 / 2) <= new_circle[2] + circle[2]:
            return True
    return False


def main():
    number_of_circles = int(input())
    intersecting_groups = [[]]

    for times in range(number_of_circles):
        new_circle = [int(x) for x in input().split()]
        print("( {} {} ) rad: {}".format(new_circle[0], new_circle[1], new_circle[2]))
        has_group = False
        for group in intersecting_groups:
            if is_intersecting(new_circle, group):
                group.append(new_circle)
                has_group = True
        if not has_group:
            new_group = [new_circle]
            intersecting_groups.append(new_group)

    total = 0
    for group in intersecting_groups:
        left = min([circle[0] - circle[2] for circle in group])
        right = max([circle[0] + circle[2] for circle in group])
        up = max([circle[1] + circle[2] for circle in group])
        down = min([circle[1] - circle[2] for circle in group])
        total += (right - left) * (up - down)
    print("Total rect area: {}".format(total))


main()
