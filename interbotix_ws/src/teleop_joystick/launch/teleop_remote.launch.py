from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
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

    return LaunchDescription([joy_node, joy_twist_node, teleop_control_node])