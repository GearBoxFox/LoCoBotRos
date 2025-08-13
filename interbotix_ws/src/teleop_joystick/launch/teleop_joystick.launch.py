from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, DeclareLaunchArgument)
from launch.substitutions import (PathJoinSubstitution, LaunchConfiguration)
from launch.conditions import (UnlessCondition)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument("use_remote", default_value="false")
    )

    use_remote = LaunchConfiguration("use_remote")

    joy_node = Node(
        package='joy',
        executable='joy_node',
        remappings=[
            ('/joy', '/joy_cmds')
        ],
        condition=UnlessCondition(use_remote)
    )

    teleop_control_node = Node(
        package='teleop_joystick',
        executable='teleop_joystick',
        condition=UnlessCondition(use_remote)
    )

    joy_twist_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        remappings=[
            ('/joy', '/joy_cmds'),
            ("/cmd_vel", "/locobot/commands/velocity")
        ],
        condition=UnlessCondition(use_remote)
    )

    locobot_control_launch = IncludeLaunchDescription(
        PathJoinSubstitution([
            FindPackageShare('interbotix_xslocobot_control'),
            'launch',
            'xslocobot_control'
        ]),
        launch_arguments={
            "robot_model": "locobot_wx200",
            "use_camera": "true",
        }.items(),
    )

    moveit_launch = IncludeLaunchDescription(
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

    return LaunchDescription([joy_node, teleop_control_node, joy_twist_node, locobot_control_launch])