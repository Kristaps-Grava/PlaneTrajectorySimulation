# Python Script for Calculating Optimal Launch Angle
#
# November 2025
# Kristaps Grava (c)


from core.simulation import Simulation
from visualise.visualise import Visualise


visualise = Visualise()

sim1 = Simulation(0)
sim2 = Simulation(5)
sim3 = Simulation(10)
sim4 = Simulation(15)
sim5 = Simulation(20)

sim1.run()
sim2.run()
sim3.run()
sim4.run()
sim5.run()

visualise.plot_trajectory(sim1.x_history, sim1.y_history,
                          sim2.x_history, sim2.y_history,
                          sim3.x_history, sim3.y_history,
                          sim4.x_history, sim4.y_history,
                          sim5.x_history, sim5.y_history)