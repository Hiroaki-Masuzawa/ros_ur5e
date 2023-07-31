### sample for IKWrapper
import irsl_choreonoid.robot_util as ru
import irsl_choreonoid.cnoid_util as cu
import irsl_choreonoid.cnoid_base as cb
import numpy as np

##
joints = [
    "shoulder_link",
    "upper_arm_link",
    "forearm_link",
    "wrist_1_link",
    "wrist_2_link",
    "wrist_3_link",
]
body_file = "file:///userdir/ur5_robot_sample/ur5_robot_r.body"
##
if cu.isInChoreonoid():
    ## on choreonoid
    bi = cb.loadRobotItem(cu.parseURL(body_file))
    bd = bi.body
else:
    ## on console
    bd = cu.loadRobot(cu.parseURL(body_file))

## ru.IKWrapper(instance-of-body, target-link(name, id, link))
## use_joints : optional, list of using joint(name, id, joint)
ik = ru.IKWrapper(bd, "wrist_3_link", use_joints=joints)


tgtorg = ik.getEndEffector()  ## target coordinates
tgt = ik.getEndEffector().translate(np.array([0.05, 0, 0.05]))  ## moved target

## solve inverse-kinematics
## inverseKinematics(target-coords)
## constraint : 'xyzRPY' or [1, 1, 1, 1, 1, 1], 'xyz' is just position(3-axis), 'xyzRPY' is for 6-axis
## add_noise : noise [rad], noise is added to joints before solving IK
## debug: True or False, print debug message
succ, _iter = ik.inverseKinematics(tgt, debug = True, constraint = 'xyzRPY', add_noise=0.4)
ik.flush()
print('original: {}\n  target: {}\n  solved: {}'.format(tgtorg, tgt, ik.endEffector))

ik.resetPose() ## reset to initial-pose
ik.flush()

