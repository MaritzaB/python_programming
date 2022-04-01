# 02 Programa que lea en una variable una velocidad en km/h y la transforme a m/s.

print("Please enter velocity in km/h: \n")

velocity_kmh = float(input())

velocity_ms = velocity_kmh * (1000 / 3600)

print(f"\n Velocity in m/s is: {velocity_ms} \n")
