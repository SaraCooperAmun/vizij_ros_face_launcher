from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    package_dir = get_package_share_directory('vizij_ros_face_launcher')
    script = os.path.join(
        package_dir,
        'scripts',
        'launch-vizij-face.sh'
    )

    return LaunchDescription([
        Node(
            package='vizij_face_bridge',
            executable='bridge',
            output='screen'
        ),

        ExecuteProcess(
            cmd=['bash', script],
            output='screen'
        ),
    ])
