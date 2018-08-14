def is_inside(xy, xy_wh):
    if xy[0] < xy_wh[0]:
        return False
    elif xy[1] < xy_wh[1]:
        return False
    elif xy[0] > xy_wh[0] + xy_wh[2]:
        return False
    elif xy[1] > xy_wh[1] + xy_wh[3]:
        return False
    else:
        return True

print(is_inside([100, 120], [140, 60, 100, 200]))
print(is_inside([200, 120], [140, 60, 100, 200]))
