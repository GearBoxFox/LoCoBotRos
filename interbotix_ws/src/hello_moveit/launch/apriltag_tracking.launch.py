from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    OpaqueFunction
)
from launch.substitutions import (
    LaunchConfiguration,
    PathJoinSubstitution,
)

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterFile, ParameterValue
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):

    locobot_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('interbotix_xslocobot_control'),
                'launch',
                'xslocobot_control.launch.py'
            ]),
        ]),
        launch_arguments={
            'robot_model': 'locobot_wx200',
            'robot_name': 'locobot',
            'use_camera': 'true'
        }.items()
    )

    apriltag_node = Node(
        package="apriltag_ros",
        executable="apriltag_node",
        namespace=('locobot', '/camera'),
        parameters=[
            ParameterFile(
                param_file=PathJoinSubstitution([
                        FindPackageShare('hello_moveit'),
                        'config',
                        'apriltag.yaml'
                    ]),
                    allow_substs=True,
            )
        ],
        remappings=[
            ('/locobot/camera/camera_info', '/locobot/camera/camera/color/camera_info'),
            ('/locobot/camera/image_rect', '/locobot/camera/camera/color/image_raw')
        ]
    )

    seeker_node = Node(
        package="hello_moveit",
        executable="hello_moveit"
    )

    return [
        locobot_control,
        apriltag_node,
        seeker_node
    ]

def generate_launch_description():
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            'robot_name',
            default_value='locobot',
            description='name of the robot (could be anything but defaults to `locobot`).',
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'rs_camera_pointcloud_enable',
            default_value='true',
            choices=('true', 'false'),
            description="enables the RealSense camera's pointcloud.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'rs_camera_logging_level',
            default_value='info',
            choices=('debug', 'info', 'warn', 'error', 'fatal'),
            description='set the logging level for the realsense2_camera launch include.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'rs_camera_output_location',
            default_value='screen',
            choices=('screen', 'log'),
            description='set the logging location for the realsense2_camera launch include.',
        )
    )
    # Weird ones that I still need
    declared_arguments.append(
        DeclareLaunchArgument(
            'rs_camera_align_depth',
            default_value='false',
            choices=('true', 'false'),
            description=(
                'whether to publish topics with the depth stream aligned with the color stream.'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'rs_depth_module_profile',
            default_value='640,480,30',
            description='profile for the depth module stream, in `<width>,<height>,<fps>`.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'rs_camera_initial_reset',
            default_value='false',
            choices=('true', 'false'),
            description=(
                'On occasions the RealSense camera is not closed properly and due to firmware '
                'issues needs to reset. If set to `true`, the device will reset prior to usage.'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'rs_rbg_camera_profile',
            default_value='640,480,30',
            description='profile for the rbg camera image stream, in `<width>,<height>,<fps>`.',
        )
    )

    return LaunchDescription(declared_arguments + [OpaqueFunction(function=launch_setup)])

