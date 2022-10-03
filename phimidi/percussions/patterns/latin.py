import phimidi as pm

def son_clave2(duration, perc: pm.Percussion, velocity_mod=0):
    '''3:2 pattern
    2 measures of eigth notes'''
    b = int(duration/16)
    pattern =  '5__3__5_'
    pattern += '__5_3___'
    for p in pattern:
        if p == '_':
            perc.set_rest(b)
        else:
            p = int(p)
            v = p * 12 + velocity_mod
            perc.set_hit(b, velocity=v)

    
def son_clave(length, kick, tick, ride, velocity_mod=0):
    length = int(length)
    b = int(length/16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90+velocity_mod)
        kick.set_hit(1 * b, velocity=60+velocity_mod)

    run = [3, 3, 4, 2, 4]
    for r in run:
        tick.set_hit(r * b, velocity=90+velocity_mod)

    ride.set_hits(length, 16, velocity=60+velocity_mod)

def rhumba(length, kick, tick, ride, velocity_mod=0):
    length = int(length)
    b = int(length/16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90+velocity_mod)
        kick.set_hit(1 * b, velocity=60+velocity_mod)

    #  tick.set_hit(3 * b, velocity=90)
    #  tick.set_hit(4 * b, velocity=90)
    #  tick.set_hit(3 * b, velocity=90)
    #  tick.set_hit(2 * b, velocity=90)
    #  tick.set_hit(4 * b, velocity=90)
    run = [3, 4, 3, 2, 4]
    for r in run:
        tick.set_hit(r * b, velocity=90+velocity_mod)

    ride.set_hits(length, 16, velocity=60+velocity_mod)

def bossa_nova(length, kick, tick, ride, velocity_mod=0):
    length = int(length)
    b = int(length/16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90+velocity_mod)
        kick.set_hit(1 * b, velocity=60+velocity_mod)

    run = [3, 3, 4, 3, 3]
    for r in run:
        tick.set_hit(r * b, velocity=90+velocity_mod)
    #  tick.set_hit(3 * b, velocity=90)
    #  tick.set_hit(3 * b, velocity=90)
    #  tick.set_hit(4 * b, velocity=90)
    #  tick.set_hit(3 * b, velocity=90)
    #  tick.set_hit(3 * b, velocity=90)

    ride.set_hits(length, 16, velocity=60+velocity_mod)

