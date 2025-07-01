import os
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    robot_model_path = get_package_share_directory('robot_description')
    xacro_file = os.path.join(robot_model_path, 'urdf', 'robot.urdf.xacro')
    rviz_config_file = os.path.join(robot_model_path, 'config', 'view.rviz')  # <-- Ensure this file exists

    # Convert XACRO to URDF
    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    params = {'robot_description': doc.toxml()}

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[params],
    )

    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        output="screen",
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        output="screen",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["-d", rviz_config_file],
        output="screen"
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        joint_state_publisher_gui,
        rviz_node,
    ])
