# from ex11_is_inside import is_inside

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


test = is_inside([200, 120], [140, 60, 100, 200])

print(test)

if test == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")



##
hcn = {
    'x' : 140,
    'y' : 60,
    'width': 100,
    'height' :200
}
for key, value in hcn.items():
    print(key, value ,sep="=",end = " \t")
print()

xy_wh = [140,60,100,200]
x = int(input("X = "))
y = int(input("Y = "))
xy =[x,y]

test = is_inside(xy,xy_wh)

if test == True:
    print("X = {} & Y = {}  is inside a rectangle {}".format(x, y, xy_wh))
else:
    print("X = {} & Y = {} not is inside a rectangle {}".format(x, y, xy_wh))
    
