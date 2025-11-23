from core.physics import Physics
from visualise.visualise import Visualise
import config

physics0 = Physics(config, config.launch_angle[0])
physics1 = Physics(config, config.launch_angle[1])
physics2 = Physics(config, config.launch_angle[2])
physics3 = Physics(config, config.launch_angle[3])
physics4 = Physics(config, config.launch_angle[4])

visualise = Visualise()
position_history = []


# For the first angle
while physics0.position[1] > 0:
  physics0.calculate_drag()
  physics0.calculate_lift()
  physics0.calculate_gravity()
  physics0.calculate_net_force()
  physics0.motion_dynamics()
  visualise.add_position0(physics0.position[0], physics0.position[1])

# For the second angle
while physics1.position[1] > 0:
  physics1.calculate_drag()
  physics1.calculate_lift()
  physics1.calculate_gravity()
  physics1.calculate_net_force()
  physics1.motion_dynamics()
  visualise.add_position1(physics1.position[0], physics1.position[1])

# For the third angle
while physics2.position[1] > 0:
  physics2.calculate_drag()
  physics2.calculate_lift()
  physics2.calculate_gravity()
  physics2.calculate_net_force()
  physics2.motion_dynamics()
  visualise.add_position2(physics2.position[0], physics2.position[1])

# For the fourth angle
while physics3.position[1] > 0:
  physics3.calculate_drag()
  physics3.calculate_lift()
  physics3.calculate_gravity()
  physics3.calculate_net_force()
  physics3.motion_dynamics()
  visualise.add_position3(physics3.position[0], physics3.position[1])

# For the fifth angle
while physics4.position[1] > 0:
  physics4.calculate_drag()
  physics4.calculate_lift()
  physics4.calculate_gravity()
  physics4.calculate_net_force()
  physics4.motion_dynamics()
  visualise.add_position4(physics4.position[0], physics4.position[1])

visualise.plot_trajectory()