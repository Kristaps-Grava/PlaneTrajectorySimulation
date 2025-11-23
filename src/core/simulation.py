# Simulation class that is responisble for interacting with Physics
# class to perform the calculations
#
# November 2025
# Kristaps Grava (c)


from core.physics import Physics


class Simulation:
  def __init__(self, launch_angle):
    self.physics = Physics(launch_angle)
    self.x_history = []
    self.y_history = []

  def run(self):
    while self.physics.position[1] > 0:
      self.physics.calculate_drag()
      self.physics.calculate_lift()
      self.physics.calculate_gravity()
      self.physics.calculate_net_force()
      self.physics.motion_dynamics()
      self.x_history.append(self.physics.position[0])
      self.y_history.append(self.physics.position[1])