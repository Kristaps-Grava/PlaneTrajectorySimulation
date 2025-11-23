# Visualisation class that is responsible for plotting trajectories
#
# November 2025
# Kristaps Grava (c)


import matplotlib.pyplot as plt

class Visualise:
  def __init__(self):
    pass

  def plot_trajectory(self, sim1_x, sim1_y, sim2_x, sim2_y, sim3_x, sim3_y, sim4_x, sim4_y, sim5_x, sim5_y):

    plt.figure(figsize=(6, 6))
    plt.plot(sim1_x, sim1_y, marker='o', label="0 deg")
    plt.plot(sim2_x, sim2_y, marker='o', label="5 deg")
    plt.plot(sim3_x, sim3_y, marker='o', label="10 deg")
    plt.plot(sim4_x, sim4_y, marker='o', label="15 deg")
    plt.plot(sim5_x, sim5_y, marker='o', label="20 deg")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.title("Trajectory")
    plt.grid(True)
    plt.axis("equal")  # keeps the aspect ratio sane
    plt.ylim(0,5)
    plt.legend()
    plt.show()

  def print_parameters(self, physics):
    # print(physics.plane_ref_acceleration)
    print(f"Velocity: {physics.plane_ref_velocity}")
    print(f"Lift Force: {physics.plane_ref_lift}")
    print(f"Gravity Force: {physics.plane_ref_gravity}")
    print(f"Drag Force: {physics.plane_ref_drag}")
    print(f"Total Force: {physics.net_force}")
    print(f"Acceleration: {physics.plane_ref_acceleration}")
    print(f"Position: {physics.position}")
    print("\n")