# 02 Programa que lea en una variable una velocidad en km/h y la transforme a m/s.

# print("Please enter velocity in km/h: \n")


def kmh_to_ms(velocity_kmh):
    velocity_kmh = float(velocity_kmh)
    velocity_ms = round(velocity_kmh * (1000 / 3600), 3)
    return velocity_ms


# print(f"\n Velocity in m/s is: {kmh_to_ms(120)} \n")
