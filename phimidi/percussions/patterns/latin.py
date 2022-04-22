
def son_clave(length, kick, tick, ride):
    length = int(length)
    b = int(length/16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90)
        kick.set_hit(1 * b, velocity=60)

    tick.set_hit(3 * b, velocity=90)
    tick.set_hit(3 * b, velocity=90)
    tick.set_hit(4 * b, velocity=90)
    tick.set_hit(2 * b, velocity=90)
    tick.set_hit(4 * b, velocity=90)

    ride.set_hits(length, 16)

def rhumba(length, kick, tick, ride):
    length = int(length)
    b = int(length/16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90)
        kick.set_hit(1 * b, velocity=60)

    tick.set_hit(3 * b, velocity=90)
    tick.set_hit(4 * b, velocity=90)
    tick.set_hit(3 * b, velocity=90)
    tick.set_hit(2 * b, velocity=90)
    tick.set_hit(4 * b, velocity=90)

    ride.set_hits(length, 16)

def bossa_nova(length, kick, tick, ride):
    length = int(length)
    b = int(length/16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90)
        kick.set_hit(1 * b, velocity=60)

    tick.set_hit(3 * b, velocity=90)
    tick.set_hit(3 * b, velocity=90)
    tick.set_hit(4 * b, velocity=90)
    tick.set_hit(3 * b, velocity=90)
    tick.set_hit(3 * b, velocity=90)

    ride.set_hits(length, 16)

