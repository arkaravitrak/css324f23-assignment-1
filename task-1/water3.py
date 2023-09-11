def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0,1] == 4 
def successors(s):
    x, y, z = s
    #Try to pour from one to another  
    t = 5 - y
    if x > 0 and z > 0 and t > 0:
         # x -> y
        if x > t :
            yield ((x - t, 5, z), t)
        elif z > t:
            yield ((x, 5 , ))
    if z > 
    t = 8 - x

    t = 3 - z
    if z > 0 and t > 0:
        if z > t:
            yield ((3, z-t ),t)
        else:
             yield (())
