# Physics class that is responsible for calculating forces and
# applying the equations of motion
#
# November 2025
# Kristaps Grava (c)


import numpy as np
from math import sin, cos
import config
import math


class Physics:
  def __init__(self, launch_angle):
    #defining position
    self.angle_of_attack = 0
    self.plane_ref_acceleration = np.array(2, dtype=float)
    self.plane_ref_velocity = np.array([config.launch_velocity*cos(math.radians(launch_angle)),
                                        config.launch_velocity*sin(math.radians(launch_angle))])
    self.position = np.array([0, config.starting_height])

    #defining forces
    self.plane_ref_gravity = np.array(2, dtype=float)
    self.plane_ref_drag = np.array(2, dtype=float)
    self.plane_ref_lift = np.array(2, dtype=float)
    self.net_force = np.array(2, dtype=float)


  def calculate_drag(self):
    def sgn(x):
      if x > 0: return 1
      elif x < 0: return -1
      else: return 0

    self.plane_ref_drag =\
      np.array([-0.5*config.air_density*config.front_Cd*config.front_area*self.plane_ref_velocity[0]**2,
                -sgn(self.plane_ref_velocity[1])*0.5*config.air_density*config.bottom_Cd*config.bottom_area*self.plane_ref_velocity[1]**2])

  def calculate_lift(self):
    self.plane_ref_lift =\
      np.array([0, 0.5*1.29*config.wing_area*config.Cl*self.plane_ref_velocity[0]**2])

  def calculate_gravity(self):
    self.plane_ref_gravity =\
      np.array([-9.81*config.plane_mass*sin(self.angle_of_attack), -9.81*config.plane_mass*cos(self.angle_of_attack)])

  def calculate_net_force(self):
    self.net_force = self.plane_ref_drag + self.plane_ref_lift + self.plane_ref_gravity

  def rotation_dynamics(self):
    pass

  def motion_dynamics(self):
    self.plane_ref_acceleration = self.net_force / config.plane_mass
    self.plane_ref_velocity += self.plane_ref_acceleration * config.dt
    self.position += self.plane_ref_velocity * config.dt