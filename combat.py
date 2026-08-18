def melee(target):
    target.hit_points -= 10
    return target.hit_points

def ranged(target):
    target.hit_points -= 5
    return target.hit_points   

def spell (target):
    target.hit_points -= 7.5
    return target.hit_points

