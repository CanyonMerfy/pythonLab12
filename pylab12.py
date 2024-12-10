import math
import turtle

class Planet:
    def __init__(self, name, mass, position_y, position_x, velocity_x, velocity_y, color="black"):
        self.name = name
        self.mass = mass
        self.x_pos = position_x
        self.y_pos = position_y
        self.x_vel = velocity_x
        self.y_vel = velocity_y
        self.color = color

        # graphics
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color(self.color)
        # positioning
        self.t.penup()
        self.t.goto(self.x_pos, self.y_pos)
        self.t.pendown()


    def move(self, new_x_pos, new_y_pos):
        self.set_x_pos(new_x_pos)
        self.set_y_pos(new_y_pos)

        self.t.goto(new_x_pos, new_y_pos)

    def set_x_pos(self, new_x_pos):
        self.x_pos = new_x_pos

    def set_y_pos(self, new_y_pos):
        self.y_pos = new_y_pos

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_x_vel(self, new_x_vel):
        self.x_vel = new_x_vel

    def set_y_vel(self, new_y_vel):
        self.y_vel = new_y_vel

    def get_x_vel(self):
        return self.x_vel

    def get_y_vel(self):
        return self.y_vel



class Sun:
    def __init__(self, name, mass, position_x, position_y):
        self.name = name
        self.mass = mass
        self.pos_x = position_x
        self.pos_y = position_y

        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color("yellow")

        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()

    def set_x_pos(self, new_x_pos):
        self.pos_x = new_x_pos

    def set_y_pos(self, new_y_pos):
        self.pos_y = new_y_pos

    def get_x_pos(self):
        return self.pos_x

    def get_y_pos(self):
        return self.pos_y

    def get_mass(self):
        return self.mass



class SolarSystem:
    def __init__(self, sun, planets):
        self.sun = sun
        self.planets = planets

    def add_sun(self, sun):
        self.sun = sun

    def add_planet(self):
        pass

    def show_planets(self):
        for planet in self.planets:
            print(planet.name, planet.x_pos, planet.y_pos, planet.x_vel, planet.y_vel)

    def move_planets(self):
        gravity = .1
        dt = 0.001

        for planet in self.planets:
            planet.move(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel())

            dist_x = self.sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

            acc_x = gravity * self.sun.get_mass() * dist_x / new_distance ** 3
            acc_y = gravity * self.sun.get_mass() * dist_y / new_distance ** 3

            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)


class Simulation:
    def __init__(self, ss, width, height, num_periods):
        self.solar_system = ss
        self.width = width
        self.height = height
        self.periods = num_periods

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width, height=self.height)
        self.t.clear()

    def run(self):
        for period in range(0, self.periods):
            self.solar_system.show_planets()
            self.solar_system.move_planets()




the_sun = Sun("SOL", 10000000, 0.0, 0.0)
#solar_system.add_sun(the_sun)

earth = Planet("EARTH", 1, 0.0, 25, 5.0, 200.0, "green")
#solar_system.add_planet(earth)

mars = Planet("MARS", .1, 0.0, 62, 10.0, 125.0, "red")
#solar_system.add_planet(mars)

solar_system = SolarSystem(the_sun, [earth, mars])
simulation = Simulation(solar_system, 500, 500, 2000)

while True:
    simulation.run()