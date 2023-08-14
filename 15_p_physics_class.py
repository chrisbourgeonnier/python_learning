# A converter for temperatures in °C and °F: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  print(f_temp, c_temp)
  return round(c_temp, 1)
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  print(c_temp, f_temp)
  return round(f_temp)
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Physics calculations
# given variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Calculating the force of a GE train
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Calculating the energy supplied by a bomb
def get_energy(mass, c = 3 * 10**8):
  return mass * c**2
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Defining the work of a train over a given distance
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " of work over " + str(train_distance))