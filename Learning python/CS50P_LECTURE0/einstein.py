#Asking user for mass
mass = float(input("Enter the mass in kilograms? "))

def energy(mass):
    #Calculating the energy using Einstein's equation E=mc^2
    E = mass * (3 * 10**8)**2
    return E

print(energy(mass))