from math import sqrt


def body_surface(mass:int):
    result1 = mass * 4
    result2 = mass + 90
    print(f"{result1=} {result2=}")
    return result1 / result2

def mosteller(mass:int, height:int):
    return sqrt((height*mass)/3600)

def imc(mass:int, height:int):
    return mass/((height/100)**2)

def dehydration_calc(fast_hours:int, NB:int):
    return fast_hours/NB

def deficit_millilitres(weight:int, dehydration:int):
    return weight * 25 * 10

# def unsensible_losses(loss_in_millilitres):
#     if loss_in_millilitres
