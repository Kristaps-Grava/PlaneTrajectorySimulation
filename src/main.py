from core.simulation import Simulation
from visualise.visualise import Visualise
import config

visualise = Visualise()

sim1 = Simulation(config, 0)
sim2 = Simulation(config, 5)
sim3 = Simulation(config, 10)
sim4 = Simulation(config, 15)
sim5 = Simulation(config, 20)

sim1.run()
sim2.run()
sim3.run()
sim4.run()
sim5.run()

print(sim1.x_history)
visualise.plot_trajectory(sim1.x_history, sim1.y_history,
                          sim2.x_history, sim2.y_history,
                          sim3.x_history, sim3.y_history,
                          sim4.x_history, sim4.y_history,
                          sim5.x_history, sim5.y_history,)