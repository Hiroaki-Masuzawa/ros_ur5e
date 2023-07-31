#!/usr/bin/env python3
from irsl_choreonoid_ros.RobotInterface import RobotInterface
import time
import math

if __name__ == "__main__":
    ri = RobotInterface("ur5_robot_robotinterface.yaml")
    time.sleep(1.0) # for connection 
    robot_model = ri.copyRobotModel()
    av = robot_model.angleVector()
    av[1] = math.radians(-45)
    av[2] = math.radians(-45)
    ri.sendAngleVector(av, 5.0)
    time.sleep(1.0)
