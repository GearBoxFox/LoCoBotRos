import math
import rclpy

import numpy as np

from rclpy.node import Node
from std_msgs.msg import ColorRGBA
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped, Point, Vector3
from visualization_msgs.msg import Marker

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
        self.tf_broadcaster = self.create_publisher(Marker, '/locobot/kinematic_point', 10)

        self.kinematics = Kinematics()

    def subscriber_callback(self, msg: JointState):
        t = Marker()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "locobot/arm_base_link"
        t.type = 4

        scale = Vector3()
        scale.x = 0.1
        scale.y = 0.1
        scale.z = 0.1
        t.scale = scale

        t.ns = "kinematic"
        t.action = 0

        c = ColorRGBA()
        c.r = 1.0
        c.b = 0.0
        c.g = 0.0
        c.a = 1.0

        t.color = c

        transforms = self.kinematics.forward_kinematics(msg.position[2:7])
        prev_transform = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        
        for i in range(3):
            prev_transform = prev_transform @ transforms[i]
            p = Point()
            p.x = prev_transform[0,3] / 100
            p.y = prev_transform[1,3] / 100
            p.z = prev_transform[2,3] / 100

            t.points.append(p)

        print(t.points)
        print("\n")
        self.tf_broadcaster.publish(t)

def main():
    rclpy.init()
    node = KinematicsTest()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
