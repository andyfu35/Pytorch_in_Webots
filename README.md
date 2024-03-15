# About
I'm making a project about how to use Ros2 in Webots with python. I want to record it because of my poor memory.


# Getting started
    
Build a Ros2 workspace    
```
mkdir /ros2_ws/src
```
```
cd /ros2_ws
```
```
source /opt/ros/foxy/setup.bash
```
```
colcon build
```
```
source install/setup.bash 
```
```
cd /src
```
```
ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name `my_robot_driver` `my_package` --dependencies rclpy geometry_msgs webots_ros2_driver
```
