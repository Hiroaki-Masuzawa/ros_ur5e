#!/usr/bin/env python3
from irsl_choreonoid_ros.RobotInterface import RobotInterface
import time
import math

import irsl_choreonoid.robot_util as ru
import numpy as np

if __name__ == "__main__":
    ri = RobotInterface("ur5_robot_robotinterface.yaml")
    time.sleep(1.0)  # for connection

    # get Robot model
    robot_model = ri.copyRobotModel()

    #get joint name list
    joints = [
        robot_model.getJoint(i).getName() for i in range(robot_model.getNumJoints())
    ]
    # set IK Wrapper
    ik = ru.IKWrapper(robot_model, "wrist_3_link", use_joints=joints)

    # set current angle vector
    ik.angleVector(ri.robot.angleVector())

    tgtorg = ik.getEndEffector()  ## target coordinates
    tgt = ik.getEndEffector().translate(np.array([0.05, 0, 0.05]))  ## moved target
    succ, _iter = ik.inverseKinematics(
        tgt, debug=True, constraint="xyzRPY", add_noise=0.4
    )

    if succ:
        av = ik.angleVector()
        # print(ik.currentAngleVector(), av)
        print('original: {}\n  target: {}\n  solved: {}'.format(tgtorg, tgt, ik.endEffector))
        ri.sendAngleVector(av, 5.0)
        time.sleep(5.0)
