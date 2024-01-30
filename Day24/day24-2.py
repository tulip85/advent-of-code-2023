from sympy import symbols
from sympy import solve
from sympy import Eq

X, Y, Z = 0, 1, 2


speed_x, speed_y, speed_z = symbols('speed_x,speed_y,speed_z')
pos_x, pos_y, pos_z = symbols(
    'pos_x,pos_y,pos_z', positive=True, integer=True)


def add_functions_to_solve(pos, speed, system):
    system.append(Eq((pos[X] - pos_x) * (speed_y - speed[Y]),
                  (pos[Y] - pos_y) * (speed_x-speed[X])))
    system.append(Eq((pos[X] - pos_x) * (speed_z - speed[Z]),
                  (pos[Z] - pos_z) * (speed_x-speed[X])))


functions_to_solve = []
for line in open("Day24/input1.in"):
    pos, speed = line.strip().split('@')
    add_functions_to_solve(list(map(int, pos.split(','))), list(
        map(int, speed.split(','))), functions_to_solve)

solution = solve(functions_to_solve, [
    speed_x, pos_x, speed_y, pos_y, speed_z, pos_z])

print("Adding positions, part 2 result: ",
      solution[0][1]+solution[0][3]+solution[0][5])
