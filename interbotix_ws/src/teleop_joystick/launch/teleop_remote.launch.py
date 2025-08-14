from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterFile

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

    joy_params = ParameterFile(
        param_file=PathJoinSubstitution([
            FindPackageShare('teleop_joystick'),
            'config',
            'joystick.config.yaml',
        ]),
        allow_substs=True,
    )

    joy_twist_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        parameters=[joy_params],
        remappings=[
            ('/joy', '/joy_cmds'),
            ('/cmd_vel', '/locobot/commands/velocity')
        ]
    )

    return LaunchDescription([joy_node, joy_twist_node, teleop_control_node])