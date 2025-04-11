from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable
import launch.actions
import launch_ros.actions


def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='false')
    return LaunchDescription([
        launch_ros.actions.Node(
            package='slam_gmapping', 
            executable='slam_gmapping', 
            output='screen', 
            parameters=[{'use_sim_time':use_sim_time}]
        ),
        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_odom_base_link',
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link'],
            output='screen'
        ),

        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_base_link_velodyne',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'velodyne'],
            output='screen'
        ),
    ])
