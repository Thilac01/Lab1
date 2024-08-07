q = float(input('Enter the applied load per unit area (pressure): '))
r = float(input('Enter the radius of the circular loaded area: '))
z = float(input('Enter the depth below the center of the loaded area: '))

s = q*(1-1/(((r**2/z**2)+1)**(3/2)))

print(f" vertical stress is {s:8.3f}")