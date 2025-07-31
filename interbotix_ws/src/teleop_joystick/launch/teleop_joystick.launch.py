from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, DeclareLaunchArguement)
from launch.substitutions import (PathJoinSubstitution, LaunchConfiguration)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # parameters
    DeclareLaunchArguement("use_camera", )

    joy_node = Node(
        package='joy',
        executable='joy_node',
        remappings=[
            ('/joy', '/joy_cmds')
        ]
    )

    teleop_control_node = Node(
        package='teleop_joystick',
        executable='teleop_joystick'
    )

    joy_twist_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        remappings=[
            ('/joy', '/joy_cmds')
        ]
    )

    moveit_node = IncludeLaunchDescription(
        PathJoinSubstitution([
            FindPackageShare('interbotix_xslocobot_moveit'),
            'launch',
            'xslocobot_moveit'
        ]),
        launch_arguments={
            "robot_model": "locobot_wx200",
            "use_camera": "True",
        }
    )

    return LaunchDescription([joy_node, teleop_control_node, joy_twist_node])