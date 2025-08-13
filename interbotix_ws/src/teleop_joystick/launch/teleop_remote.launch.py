from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    joy_node = Node(
        package='joy',
        executable='joy_node',
        remappings=[
            ('/joy', '/joy_cmds'),
        ]
    )

    teleop_control_node = Node(
        package='teleop_joystick',
        executable='teleop_joystick'
    )

    joy_params = os.path.join(get_package_share_directory('articubot_one'),'config','joystick.yaml')

    joy_twist_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        remappings=[
            ('/joy', '/joy_cmds'),
            ('/cmd_vel', '/locobot/commands/velocity')
        ]
    )

    return LaunchDescription([joy_node, joy_twist_node, teleop_control_node])