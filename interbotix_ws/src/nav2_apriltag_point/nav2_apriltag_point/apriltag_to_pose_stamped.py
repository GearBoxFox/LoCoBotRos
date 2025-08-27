import rclpy
from rclpy.node import Node
from rclpy.time import Time

from apriltag_msgs.msg import AprilTagDetectionArray, AprilTagDetection
from geometry_msgs.msg import PoseStamped

from tf2_ros import TransformException
from tf2_ros import TransformListener, Buffer

class ApriltagToPoseStamped(Node):

    def __init__(self):
        super().__init__('apriltag_to_pose_stamped')

        self.publisher = self.create_publisher(PoseStamped, 'updated_goal', 10)
        self.tf_buffer = Buffer()
        self.subscriber = TransformListener(self.tf_buffer, self)

        # create a timer that handles updates
        self.timer = self.create_timer(10 / 1000, self.timer_callback)

        # the parent frame is the camera
        self.parent_frame = "camera_color_optical_frame"
        self.child_frame = "tag36h11:0"

    def timer_callback(self):
        pose = PoseStamped()

        # make sure our header is correct
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = self.parent_frame

        try:
            # get the latest transform
            tranform = self.tf_buffer.lookup_transform(
                self.parent_frame,
                self.child_frame,
                Time()
            )

            # copy the pose from the transform to the stamped pose
            pose.pose.position.x = tranform.transform.translation.x
            pose.pose.position.y = tranform.transform.translation.y
            pose.pose.position.z = tranform.transform.translation.z

            pose.pose.orientation = tranform.transform.rotation

            self.publisher.publish(pose)
        except TransformException:
            self.get_logger().info("Some expection happened")

def main(args=None):
    rclpy.init(args=args)

    apriltag_to_pose_stamped = ApriltagToPoseStamped()

    rclpy.spin(apriltag_to_pose_stamped)

    apriltag_to_pose_stamped.destroy_node()
    rclpy.shutdown

if __name__ == '__main__':
    main()