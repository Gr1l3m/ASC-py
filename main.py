# This is a sample Python script.
from asc_funcs.asc import body_surface, imc, body_surface_mosteller

if __name__ == '__main__':
    print(body_surface(60))
    print(body_surface_mosteller(60, 160))
    print(imc(60, 160))
