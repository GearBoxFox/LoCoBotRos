import math
import rclpy

import numpy as np

from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped

from locobot_kinematics.kinematics import Kinematics

from tf2_ros import TransformBroadcaster

def quaternion_from_euler(ai, aj, ak):
    ai /= 2.0
    aj /= 2.0
    ak /= 2.0
    ci = math.cos(ai)
    si = math.sin(ai)
    cj = math.cos(aj)
    sj = math.sin(aj)
    ck = math.cos(ak)
    sk = math.sin(ak)
    cc = ci*ck
    cs = ci*sk
    sc = si*ck
    ss = si*sk

    q = np.empty((4, ))
    q[0] = cj*sc - sj*cs
    q[1] = cj*ss + sj*cc
    q[2] = cj*cs - sj*sc
    q[3] = cj*cc + sj*ss

    return q

class KinematicsTest(Node):

    def __init__(self):
        super().__init__('kinematics_test_node')

        self.subscriber = self.create_subscription(JointState, '/locobot/joint_states', self.subscriber_callback, 1)
        self.tf_broadcaster = self.create_publisher(PoseStamped, '/locobot/kinematic_point', 10)

        self.kinematics = Kinematics()

    def subscriber_callback(self, msg: JointState):
        t = PoseStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "locobot/arm_base_link"

        transforms = self.kinematics.forward_kinematics(msg.position[2:7])
        full_transform = transforms[0] @ transforms[1] @ transforms[2] #@ transforms[3]
        print(f"{full_transform[0, 3]}, {full_transform[1, 3]}, {full_transform[2, 3]}")
        #print(full_transform)
        #print(msg.position[2:7])

        t.pose.position.x = full_transform[0, 3] / 100
        t.pose.position.y = full_transform[1, 3] / 100
        t.pose.position.z = full_transform[2, 3] / 100

        self.tf_broadcaster.publish(t)

def main():
    rclpy.init()
    node = KinematicsTest()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
