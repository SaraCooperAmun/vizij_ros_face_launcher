from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    package_dir = get_package_share_directory(
        'vizij_ros_face_launcher'
    )

    script = os.path.join(
        package_dir,
        'scripts',
        'launch-vizij-face.sh'
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            'face_asset',
            default_value='emy.glb',
            description='GLB filename in demo-ros4hri/public/assets'
        ),
        DeclareLaunchArgument(
            'robot_ip',
            default_value='localhost',#'192.168.50.201',
            description='Robot IP address'
        ),
        DeclareLaunchArgument(
            'vizij_repo_dir',
            default_value='/home/emorobcare/vizij_project/vizij-web',
            description='Path to the Vizij web repository'
        ),

        Node(
            package='vizij_face_bridge',
            executable='bridge',
            output='screen'
        ),

        ExecuteProcess(
            cmd=['bash', script],
            additional_env={
                'VIZIJ_REPO_DIR': LaunchConfiguration('vizij_repo_dir'),
                'VIZIJ_FACE_ASSET': LaunchConfiguration('face_asset'),
                'VITE_FACE_WS_URL': [
                    'ws://',
                    LaunchConfiguration('robot_ip'),
                    ':9001'
                ],
            },
            output='screen'
        ),
    ])