from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder

def generate_launch_description():

    robot_model_launch_arg = LaunchConfiguration('robot_model')
    robot_name_launch_arg = LaunchConfiguration('robot_name')
    arm_model_launch_arg = LaunchConfiguration('arm_model')
    robot_description_launch_arg = LaunchConfiguration('robot_description')

    
    robot_description = {
        'robot_description': ParameterValue(robot_description_launch_arg, value_type=str)
    }

    config_path = PathJoinSubstitution([
        FindPackageShare('interbotix_xslocobot_moveit'),
        'config',
    ])

    robot_description_semantic = {
        'robot_description_semantic':
            construct_interbotix_xslocobot_semantic_robot_description_command(
                robot_model=robot_model_launch_arg.perform(context),
                config_path=config_path
            ),
    }

    kinematics_config = PathJoinSubstitution([
        FindPackageShare('interbotix_xslocobot_moveit'),
        'config',
        'kinematics.yaml',
    ])

    ompl_planning_pipeline_config = {
        'move_group': {
            'planning_plugin':
                'ompl_interface/OMPLPlanner',
            'request_adapters':
                'default_planner_request_adapters/AddTimeOptimalParameterization '
                'default_planner_request_adapters/FixWorkspaceBounds '
                'default_planner_request_adapters/FixStartStateBounds '
                'default_planner_request_adapters/FixStartStateCollision '
                'default_planner_request_adapters/FixStartStatePathConstraints',
            'start_state_max_bounds_error':
                0.1,
        }
    }

    ompl_planning_pipeline_yaml_file = load_yaml(
        'interbotix_xslocobot_moveit', 'config/ompl_planning.yaml'
    )
    ompl_planning_pipeline_config['move_group'].update(ompl_planning_pipeline_yaml_file)

    controllers_config = load_yaml(
        'interbotix_xslocobot_moveit',
        f'config/controllers/{arm_model_launch_arg.perform(context)}_controllers.yaml'
    )

    config_joint_limits = load_yaml(
        'interbotix_xslocobot_moveit',
        f'config/joint_limits/{arm_model_launch_arg.perform(context)}_joint_limits.yaml'
    )

    joint_limits = {
        'robot_description_planning': config_joint_limits,
    }

    moveit_controllers = {
        'moveit_simple_controller_manager':
            controllers_config,
        'moveit_controller_manager':
            'moveit_simple_controller_manager/MoveItSimpleControllerManager',
    }

    trajectory_execution_parameters = {
        'moveit_manage_controllers': True,
        'trajectory_execution.allowed_execution_duration_scaling': 1.2,
        'trajectory_execution.allowed_goal_duration_margin': 0.5,
        'trajectory_execution.allowed_start_tolerance': 0.01,
    }

    planning_scene_monitor_parameters = {
        'publish_planning_scene': True,
        'publish_geometry_updates': True,
        'publish_state_updates': True,
        'publish_transforms_updates': True,
        'publish_robot_description': True,
        'publish_robot_description_semantic': True,
    }

    sensor_parameters = {
        'sensors': [''],
    }

    remappings = [
        (
            f'{robot_name_launch_arg.perform(context)}/get_planning_scene',
            f'/{robot_name_launch_arg.perform(context)}/get_planning_scene'
        ),
        (
            '/arm_controller/follow_joint_trajectory',
            f'/{robot_name_launch_arg.perform(context)}/arm_controller/follow_joint_trajectory'
        ),
        (
            '/gripper_controller/follow_joint_trajectory',
            f'/{robot_name_launch_arg.perform(context)}/gripper_controller/follow_joint_trajectory'
        ),
    ]

    # MTC Demo node
    pick_place_demo = Node(
        package="mtc_tutorial",
        executable="mtc_node",
        output="screen",
        parameters=[
            {
                'planning_scene_monitor_options': {
                    'robot_description':
                        'robot_description',
                    'joint_state_topic':
                        f'{robot_name_launch_arg.perform(context)}/joint_states',
                },
                'use_sim_time': use_sim_time_param,
            },
            robot_description,
            robot_description_semantic,
            kinematics_config,
            ompl_planning_pipeline_config,
            trajectory_execution_parameters,
            moveit_controllers,
            planning_scene_monitor_parameters,
            joint_limits,
            sensor_parameters,
        ],
    )

    return LaunchDescription([pick_place_demo])