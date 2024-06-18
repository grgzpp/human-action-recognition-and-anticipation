import math

import numpy as np

from iiwaPy3.iiwaPy3 import iiwaPy3

class RobotController:

    global T_rob_cam    
    T_rob_cam = np.array([[-0.0053, -0.7168, 0.6972, 136.9033],
                          [-0.9998, -0.0109, -0.0188, -279.9348],
                          [0.0211, -0.6972, -0.7166, 553.7002],
                          [0.0, 0.0, 0.0, 1.0]])

    def __init__(self):
        self.robot = None
        self.is_connected = False
        self.is_moving = False
        self.is_delivering = False
        self.is_at_home_pos = False
        
    def connect(self):
        self.robot = iiwaPy3("172.31.1.147", trans=(0.0, 0.0, 272.0, 0.0, 0.0, -math.pi/6))
        self.is_connected = True
    
    def disconnect(self):
        self.robot.close()
        self.robot = None
        self.is_connected = False

    def cam_to_robot_transform(self, P_cam):
        return np.array(np.dot(T_rob_cam, P_cam), dtype=np.float32)

    def get_current_pose_cartesian(self):
        return self.robot.getEEFPos()
    
    def get_current_pose_joints(self):
        return self.robot.getJointsPos()

    def check_workspace(self, x, y, z):
        return 370 <= x <= 700 and -300 <= y <= 30 and 20 <= z <= 250
    
    def move_to_home_pose(self):
        self.is_at_home_pos = True
        home_pose = [0, 0, 0, -math.pi / 2, 0, math.pi / 2, -math.pi/6]
        self.robot.movePTPJointSpace(home_pose, [0.1])
    
    def move_cartesian(self, x, y, z, x_offset=0.0, y_offset=0.0, z_offset=0.0, speed=30):
        self.is_at_home_pos = False
        pose_cartesian = self.robot.getEEFPos()
        pose_cartesian[0] = x + x_offset
        pose_cartesian[1] = y + y_offset
        pose_cartesian[2] = z + z_offset
        self.robot.movePTPLineEEF(pose_cartesian, [speed])

    def shift_cartesian_rel_base(self, x_shift=0.0, y_shift=0.0, z_shift=0.0, speed=30):
        self.is_at_home_pos = False
        shift = [x_shift, y_shift, z_shift]
        self.robot.movePTPLineEefRelBase(shift, [speed])

    def shift_cartesian_rel_tool(self, x_shift=0.0, y_shift=0.0, z_shift=0.0, speed=30):
        self.is_at_home_pos = False
        shift = [x_shift, y_shift, z_shift]
        self.robot.movePTPLineEefRelEef(shift, [speed])

    def move_joints(self, joint_movements, speed=0.1):
        self.is_at_home_pos = False
        self.robot.movePTPJointSpace(joint_movements, [speed])

    def open_gripper(self):
        self.robot.setPin1Off()
        self.robot.setPin11On()

    def close_gripper(self):
        self.robot.setPin11Off()
        self.robot.setPin1On()
