import matplotlib.pyplot as plt


class Visualise:
  def __init__(self):
    self.x_history0 = []
    self.y_history0 = []
    self.x_history1 = []
    self.y_history1 = []
    self.x_history2 = []
    self.y_history2 = []
    self.x_history3 = []
    self.y_history3 = []
    self.x_history4 = []
    self.y_history4 = []

  def add_position0(self, x, y):
    self.x_history0.append(x)
    self.y_history0.append(y)

  def add_position1(self, x, y):
    self.x_history1.append(x)
    self.y_history1.append(y)

  def add_position2(self, x, y):
    self.x_history2.append(x)
    self.y_history2.append(y)

  def add_position3(self, x, y):
    self.x_history3.append(x)
    self.y_history3.append(y)

  def add_position4(self, x, y):
    self.x_history4.append(x)
    self.y_history4.append(y)

  def plot_trajectory(self):

    plt.figure(figsize=(6, 6))
    plt.plot(self.x_history0, self.y_history0, marker='o', label="0 deg")
    plt.plot(self.x_history1, self.y_history1, marker='o', label="5 deg")
    plt.plot(self.x_history2, self.y_history2, marker='o', label="10 deg")
    plt.plot(self.x_history3, self.y_history3, marker='o', label="15 deg")
    plt.plot(self.x_history4, self.y_history4, marker='o', label="20 deg")
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