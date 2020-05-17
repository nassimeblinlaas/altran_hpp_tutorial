from hpp.corbaserver.fleche import Robot
robot = Robot ('fleche')
robot.setJointBounds ("root_joint", [-70, 4.375, -5, 4.375, -5, 7])
from hpp.corbaserver import ProblemSolver
ps = ProblemSolver (robot)
from hpp.gepetto import ViewerFactory
vf = ViewerFactory (ps)
q_init = robot.getCurrentConfig ()
q_goal = q_init [::]
q_init [0:2] = [-60, -4]
vf.loadObstacleModel ("iai_maps", "ville1", "ville1_link")
v = vf.createViewer()

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)

ps.addPathOptimizer ("RandomShortcut")

print (ps.solve ())

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)

ps.addPathOptimizer ("RandomShortcut")
from hpp.gepetto import PathPlayer
pp = PathPlayer (v)
pp.displayPath(1)
#pp (0)

import json
a = ps.getWaypoints(1)
with open('roadmap.txt', 'w') as f:
    for i in a[0]:
        json.dump(i, f)
        f.write("\n")

